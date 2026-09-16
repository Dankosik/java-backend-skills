#!/usr/bin/env python3
"""Validate eval inputs or prepare an isolated case; never invoke or grade a model."""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re

ROOT = Path(__file__).resolve().parents[1]


def digest(files):
    """Fingerprint names and bytes, independent of filesystem iteration order."""
    hashes = {name: hashlib.sha256(data).hexdigest()
              for name, data in sorted(files.items())}
    encoded = json.dumps(hashes, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest(), hashes


def text(value):
    return isinstance(value, str) and bool(value.strip())


def safe_path(name):
    if not isinstance(name, str) or not name or "\\" in name or ":" in name:
        raise ValueError(f"invalid fixture path: {name!r}")
    path = PurePosixPath(name)
    if (path.is_absolute() or any(p in ("", ".", "..") for p in name.split("/"))
            or any(p.startswith(".") for p in path.parts)
            or name == "prompt.txt"):
        raise ValueError(f"unsafe or reserved fixture path: {name}")
    return path


def pack_files(pack):
    """Copy only the existing standalone packaging contract, without following links."""
    skills = pack / "skills"
    if skills.is_symlink() or not skills.is_dir():
        raise ValueError("pack must contain a regular skills directory")
    files = {}
    for skill in sorted(skills.iterdir()):
        if (skill.is_symlink() or not skill.is_dir()
                or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill.name)
                or {p.name for p in skill.iterdir()} != {"SKILL.md", "LICENSE"}):
            raise ValueError(f"invalid standalone skill: {skill.name}")
        for name in ("SKILL.md", "LICENSE"):
            path = skill / name
            if path.is_symlink() or not path.is_file():
                raise ValueError(f"not a regular skill file: {path}")
            files[f"{skill.name}/{name}"] = path.read_bytes()
    if not files:
        raise ValueError("empty pack")
    return files


def validate_catalog(root):
    catalog = json.loads((root / "evals/cases.json").read_text(encoding="utf-8"))
    if not isinstance(catalog, dict) or catalog.get("version") != 1:
        raise ValueError("unsupported catalog version")
    known = {p.name for p in (root / "skills").iterdir() if p.is_dir()}
    seen, positive, negative = set(), set(), set()
    for group in ("routing", "cases"):
        entries = catalog.get(group)
        if not isinstance(entries, list) or not entries:
            raise ValueError(f"empty {group}")
        for entry in entries:
            if not isinstance(entry, dict):
                raise ValueError(f"invalid entry in {group}")
            ident = entry.get("id", "")
            if not isinstance(ident, str) or not re.fullmatch(r"[A-Z][0-9]{2}[PN]?", ident) or ident in seen:
                raise ValueError(f"invalid or duplicate id: {ident}")
            seen.add(ident)
            if not text(entry.get("prompt")):
                raise ValueError(f"missing prompt: {ident}")
            required = entry.get("required_any")
            forbidden = entry.get("forbidden", [])
            if any(not isinstance(v, list) or any(not isinstance(s, str) for s in v)
                   for v in (required, forbidden)):
                raise ValueError(f"invalid routing labels: {ident}")
            if not set(required + forbidden) <= known or set(required) & set(forbidden):
                raise ValueError(f"unknown or contradictory skill labels: {ident}")
            if group == "routing":
                if not required:
                    raise ValueError(f"routing probe needs a relevant alternative: {ident}")
                positive.update(required)
                negative.update(forbidden)
                continue
            for field in ("must", "fail"):
                values = entry.get(field)
                if not isinstance(values, list) or not values or not all(map(text, values)):
                    raise ValueError(f"missing {field} rubric: {ident}")
            files = entry.get("files")
            if not isinstance(files, dict) or not files:
                raise ValueError(f"missing frozen fixture: {ident}")
            paths = {safe_path(name) for name in files}
            for name, content in files.items():
                if not isinstance(content, str):
                    raise ValueError(f"fixture must be UTF-8 text: {ident}/{name}")
                if any(parent in paths for parent in PurePosixPath(name).parents):
                    raise ValueError(f"file/directory collision: {ident}/{name}")
    if positive != known or negative != known:
        raise ValueError("each skill needs positive and near-miss routing coverage")
    return catalog


def prepare(root, case_id, output, variant, host, pack=None, revision=None):
    if variant not in ("none", "prior", "candidate") or host not in ("codex", "claude"):
        raise ValueError("unknown variant or host")
    resolved_output = output.resolve()
    for source in (root, pack):
        if source is not None and resolved_output.is_relative_to(source.resolve()):
            raise ValueError("output must be outside the catalog and pack checkouts")
    catalog = validate_catalog(root)
    matches = [case for case in catalog["cases"] if case["id"] == case_id]
    if not matches:
        raise ValueError(f"unknown fixture case: {case_id}")
    case = matches[0]
    if variant == "none":
        if pack is not None or revision is not None:
            raise ValueError("no-pack control must not specify a pack")
        installed = {}
    else:
        if pack is None or not text(revision):
            raise ValueError("prior/candidate requires --pack and --revision")
        installed = pack_files(pack)
    fixture = {name: content.encode("utf-8") for name, content in case["files"].items()}
    fixture_hash, fixture_files = digest(fixture)
    pack_hash, _ = digest(installed)
    prompt = case["prompt"] + "\n"
    # No writes occur until all inputs have been validated. Never overwrite a run.
    output.mkdir(parents=False, exist_ok=False)
    workspace = output / "workspace"
    workspace.mkdir()
    for name, content in fixture.items():
        path = workspace / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    location = ".agents/skills" if host == "codex" else ".claude/skills"
    for name, data in installed.items():
        path = workspace / location / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    (workspace / "prompt.txt").write_text(prompt, encoding="utf-8")
    record = {
        "case": case_id, "variant": variant, "host": host,
        "pack_revision_label": revision,
        "pack_sha256": pack_hash if installed else None,
        "fixture_sha256": fixture_hash, "fixture_files": fixture_files,
        "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        "catalog_sha256": hashlib.sha256((root / "evals/cases.json").read_bytes()).hexdigest(),
        "required_any": case["required_any"], "must": case["must"], "fail": case["fail"],
        "outcome": "not_run", "selected_skills": "unobserved",
        "model": None, "settings_and_budget": None, "commands": [],
        "trace": None, "unverified": [], "observations": None,
    }
    (output / "record.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check")
    cmd = sub.add_parser("prepare")
    cmd.add_argument("case")
    cmd.add_argument("--output", required=True, type=Path)
    cmd.add_argument("--variant", choices=("none", "prior", "candidate"), required=True)
    cmd.add_argument("--host", choices=("codex", "claude"), required=True)
    cmd.add_argument("--pack", type=Path)
    cmd.add_argument("--revision")
    args = parser.parse_args()
    try:
        if args.command == "check":
            catalog = validate_catalog(ROOT)
            print(f"Validated {len(catalog['routing'])} routing probes and {len(catalog['cases'])} fixtures; no model evaluated")
        else:
            prepare(ROOT, args.case, args.output, args.variant, args.host, args.pack, args.revision)
            print(f"Prepared {args.output / 'workspace'}; outcome remains not_run")
    except (OSError, ValueError, TypeError) as error:
        parser.exit(1, f"error: {error}\n")


if __name__ == "__main__":
    main()
