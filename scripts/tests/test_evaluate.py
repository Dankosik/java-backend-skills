"""Offline input/prepare tests, not tests of model behavior."""

import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("evaluate", ROOT / "scripts/evaluate.py")
evaluate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(evaluate)


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def prepare(self, name="run", **kwargs):
        return evaluate.prepare(ROOT, "E01", self.root / name,
                                kwargs.pop("variant", "none"),
                                kwargs.pop("host", "codex"), **kwargs)

    def changed_catalog(self, change):
        catalog = evaluate.validate_catalog(ROOT)
        change(catalog)
        (self.root / "evals").mkdir()
        (self.root / "evals/cases.json").write_text(json.dumps(catalog))
        (self.root / "skills").mkdir()
        for skill in (ROOT / "skills").iterdir():
            (self.root / "skills" / skill.name).mkdir()
        return self.root

    def test_catalog(self):
        catalog = evaluate.validate_catalog(ROOT)
        self.assertEqual(30, len(catalog["routing"]))
        self.assertEqual(8, len(catalog["cases"]))

    def test_duplicate_id_rejected(self):
        root = self.changed_catalog(lambda c: c["cases"].append(c["cases"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate"):
            evaluate.validate_catalog(root)

    def test_unknown_skill_rejected(self):
        root = self.changed_catalog(lambda c: c["routing"][0]["required_any"].append("invented"))
        with self.assertRaisesRegex(ValueError, "unknown"):
            evaluate.validate_catalog(root)

    def test_missing_negative_coverage_rejected(self):
        root = self.changed_catalog(lambda c: c["routing"][1].update(forbidden=[]))
        with self.assertRaisesRegex(ValueError, "near-miss"):
            evaluate.validate_catalog(root)

    def test_missing_rubric_rejected(self):
        root = self.changed_catalog(lambda c: c["cases"][0].update(must=[]))
        with self.assertRaisesRegex(ValueError, "rubric"):
            evaluate.validate_catalog(root)

    def test_unsafe_paths_rejected(self):
        for name in ("../outside", "/tmp/outside", "a/../../x", "a\\x", "C:/x",
                     ".agents/skills/x", "prompt.txt", "a//b", "a/./b", ""):
            with self.subTest(name=name), self.assertRaises(ValueError):
                evaluate.safe_path(name)

    def test_file_directory_collision_rejected(self):
        root = self.changed_catalog(lambda c: c["cases"][0]["files"].update({"a": "", "a/b": ""}))
        with self.assertRaisesRegex(ValueError, "collision"):
            evaluate.validate_catalog(root)

    def test_control_has_no_skills_and_no_evaluator_notes(self):
        record = self.prepare()
        workspace = self.root / "run/workspace"
        self.assertFalse((workspace / ".agents").exists())
        self.assertFalse((workspace / "record.json").exists())
        self.assertEqual("not_run", record["outcome"])
        self.assertIsNone(record["pack_sha256"])
        self.assertEqual([], record["commands"])

    def test_output_inside_source_rejected(self):
        root = self.changed_catalog(lambda c: None)
        with self.assertRaisesRegex(ValueError, "outside"):
            evaluate.prepare(root, "E01", root / "run", "none", "codex")
        self.assertFalse((root / "run").exists())

    def test_invalid_entry_rejected(self):
        root = self.changed_catalog(lambda c: c["cases"].append(None))
        with self.assertRaisesRegex(ValueError, "invalid entry"):
            evaluate.validate_catalog(root)

    def test_no_overwrite(self):
        self.prepare()
        with self.assertRaises(FileExistsError):
            self.prepare()
        self.assertEqual("not_run", json.loads((self.root / "run/record.json").read_text())["outcome"])

    def test_variants_share_prompt_and_fixture_bytes(self):
        control = self.prepare("none")
        prior = self.prepare("prior", variant="prior", pack=ROOT, revision="same-test-input")
        candidate = self.prepare("candidate", variant="candidate", pack=ROOT, revision="same-test-input")
        for record in (prior, candidate):
            self.assertEqual(control["fixture_sha256"], record["fixture_sha256"])
            self.assertEqual(control["prompt_sha256"], record["prompt_sha256"])
        self.assertEqual(prior["pack_sha256"], candidate["pack_sha256"])
        installed = list((self.root / "candidate/workspace/.agents/skills").glob("*/SKILL.md"))
        self.assertEqual(15, len(installed))

    def test_claude_placement(self):
        self.prepare(host="claude", variant="candidate", pack=ROOT, revision="test")
        self.assertEqual(15, len(list((self.root / "run/workspace/.claude/skills").glob("*/SKILL.md"))))
        self.assertFalse((self.root / "run/workspace/.agents").exists())

    def test_invalid_control_and_missing_revision_do_not_write(self):
        for args in ({"pack": ROOT}, {"variant": "prior", "pack": ROOT}):
            with self.subTest(args=args), self.assertRaises(ValueError):
                self.prepare(**args)
            self.assertFalse((self.root / "run").exists())

    def test_fingerprint_is_order_independent_and_content_sensitive(self):
        first = evaluate.digest({"a": b"x", "b": b"y"})[0]
        self.assertEqual(first, evaluate.digest({"b": b"y", "a": b"x"})[0])
        self.assertNotEqual(first, evaluate.digest({"a": b"z", "b": b"y"})[0])

    def test_symlink_skill_rejected(self):
        (self.root / "skills").mkdir()
        try:
            (self.root / "skills/link").symlink_to(ROOT / "skills/java-implement", target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks not supported by this test environment")
        with self.assertRaisesRegex(ValueError, "standalone"):
            evaluate.pack_files(self.root)

    @unittest.skipUnless(shutil.which("javac") and shutil.which("java"), "JDK unavailable; oracle sensitivity unverified")
    def test_known_boundary_mutant_fails_and_corrected_source_passes(self):
        self.prepare()
        workspace = self.root / "run/workspace"
        oracle = workspace / "BoundaryOracle.java"
        oracle.write_text('''public final class BoundaryOracle {
    public static void main(String[] args) {
        Eligibility e = new Eligibility();
        if (e.eligible(99)) throw new AssertionError("99");
        if (!e.eligible(100)) throw new AssertionError("boundary 100");
        if (!e.eligible(101)) throw new AssertionError("101");
    }
}
''')
        def run_oracle():
            compiled = subprocess.run(["javac", "--release", "17", "-d", "out",
                                       "Eligibility.java", "BoundaryOracle.java"],
                                      cwd=workspace, capture_output=True, text=True, timeout=20)
            self.assertEqual(0, compiled.returncode, compiled.stderr)
            return subprocess.run(["java", "-cp", "out", "BoundaryOracle"],
                                  cwd=workspace, capture_output=True, text=True, timeout=10)
        failed = run_oracle()
        self.assertNotEqual(0, failed.returncode)
        self.assertIn("AssertionError: boundary 100", failed.stderr)
        path = workspace / "Eligibility.java"
        path.write_text(path.read_text().replace("total > 100", "total >= 100"))
        passed = run_oracle()
        self.assertEqual(0, passed.returncode, passed.stderr)


if __name__ == "__main__":
    unittest.main()
