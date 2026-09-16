# Frozen evaluation inputs

This is author tooling, not an installed skill. Start with the comparison and
result protocol in [docs/evaluation.md](../docs/evaluation.md).

`cases.json` contains 30 natural-language routing probes (a positive and a
near-miss for each skill) and eight version-controlled task fixtures. Fixture
files are stored as UTF-8 strings in JSON and materialized byte-for-byte; this
keeps the prompt, files, and rubric in one reviewed change. Rubrics and routing
labels are evaluator-only data, not task instructions.

## What is actually executable

E01 and E19 have a small Java source/test workspace requiring a JDK that supports
`--release 17`, with no dependencies or services. The harness test independently
checks that the `> 100` mutant fails at 100 and `>= 100` passes. This establishes
oracle sensitivity, not that any agent wrote the fix or selected the right skill.
It is not a substitute for the Spring workspace comparison described under E01
in the larger protocol.

E03/E08 are review-only Java inputs. E06 is a reduced source-only SQL task with
explicitly unavailable target-engine verification, not a runnable persistence
integration. E17 covers an overlapping deployment migration; E18 uses labeled
payment pseudocode to expose concurrent and crash-window errors. E20 is a
spelling-only negative case in a Java workspace. These are judged against their
contracts and actual traces/diffs; compiling them is not a universal rubric.

## Offline preparation

Python 3.12+ standard library is sufficient; preparation never contacts a model,
installs software, executes fixture instructions, or runs a shell command.

```sh
python scripts/evaluate.py check
python -m unittest discover -s scripts/tests -p test_evaluate.py
```

Create a new output directory under an existing disposable parent, outside any
checkout or parent directory that supplies agent instructions. For example, with
an existing `../eval-runs` parent and separately pinned pack checkouts:

```sh
python scripts/evaluate.py prepare E01 --variant none --host codex --output ../eval-runs/E01-none
python scripts/evaluate.py prepare E01 --variant prior --host codex --pack ../java-skills-prior --revision PRIOR_COMMIT --output ../eval-runs/E01-prior
python scripts/evaluate.py prepare E01 --variant candidate --host codex --pack ../java-skills-candidate --revision CANDIDATE_COMMIT --output ../eval-runs/E01-candidate
```

Replace the revision labels with the exact checkout commits. The tool records
them as supplied labels, not verified Git attestations; byte-level pack, fixture,
prompt, and catalog SHA-256 fingerprints identify the actual inputs even for a
dirty tree. For a controlled comparison use clean pinned checkouts and retain
any unavoidable diff separately. For Claude use `--host claude`.

Only fixture files, `prompt.txt`, and all standalone pack skills (except in the
`none` control) enter `workspace/`. The complete pack tests discovery without
leaking the expected selection by installing only the anticipated skill.
`record.json` remains outside it with `outcome: not_run`. Existing run directories
are never overwritten. This is workspace preparation, not a security sandbox;
restrict agent access to the task workspace and do not expose evaluator notes.

## Execute and assess separately

Use the installed, authorized host with `workspace/` as its task root and feed
only `prompt.txt` as the request. Record the exact command and host/model/settings,
permissions, cache state, and budget; keep them equal across variants. Disable
ambient installed packs, parent instruction files, persistent task memory, and
native duplicates that would contaminate the control. Honor the host's scratch
workspace/trust requirements without relaxing access to unrelated files.

Capture raw host events, stdout/stderr, exit status, final diff (including
untracked files), and actual check output outside the task root. A zero host
exit code is **ungraded**, not a pass. A model's summary is not command evidence.
Selection is `unobserved` unless the host exposes it; do not infer skill loading
from familiar phrases. `required_any` allows any listed relevant skill and
additional justified skills, not an exact call sequence. Apply routing labels
only to pack variants with observable selection; no-pack is the outcome control.
The 30 routing-only probes need the same controlled host setup and are not
executed by `check` or `prepare`.

An evaluator assesses every `must`/`fail` criterion from artifacts, with location
and evidence for each verdict, then completes the result record from the larger
protocol. Mark blocked or missing evidence explicitly, not as passing by default.
Keep correctness, permission boundaries, and truthful verification separate from
routing and efficiency. Compare repeated none/prior/candidate runs before
claiming improvement; validate on each supported model separately. Rubric changes
need their own revision and must not be silently retuned to favor the candidate.

CI validates catalog consistency and the preparation tool. It never spends
model tokens. No model run or cross-model improvement is recorded by these files.
