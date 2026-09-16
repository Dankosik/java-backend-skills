# Maintaining this skill pack

This repository distributes instructions, not a Java application. Each of the
15 installed skills is independent: only `SKILL.md` and `LICENSE` are packaged
per skill. Keep essential task guidance there; maintainer docs are not installed
with standalone skills. Do not add mandatory skill chains or a new runtime tool.

For instruction changes, read the affected skill and its neighbors' descriptions,
then the relevant scenario in [docs/evaluation.md](docs/evaluation.md).
Use [docs/instruction-design.md](docs/instruction-design.md) for authoring or review,
and [evals/README.md](evals/README.md) when preparing model comparisons. Do not
load every reference for a wording-only change.

After skill or catalog changes, run `python scripts/evaluate.py check` and
`python scripts/distribution.py check` with the declared development dependencies.
For evaluator code, also run
`python -m unittest discover -s scripts/tests -p test_evaluate.py`.
Packaging changes use the existing distribution tests and installation smoke test;
CI retains the full release checks. Do not repeatedly install tools or rebuild
archives for prose-only edits. Record checks blocked by missing prerequisites.

`plugin.json` owns metadata; regenerate native manifests with
`python scripts/distribution.py sync` only when it changes. Preserve release pins
until a release exists. Do not publish releases or modify another repository as
part of an instruction edit. Preserve unrelated work and distinguish static
checks, fixture checks, human review, and actual model evaluation in the result.
