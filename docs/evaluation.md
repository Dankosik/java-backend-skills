# Behavioral evaluation for skill changes

These are authoring scenarios, not instructions to load into application tasks.
They are not run by distribution CI and do not establish an improvement merely
by existing. No behavioral run is recorded by this document. Start with cases
affected by an instruction change; do not make the full matrix a routine gate
for application development.

## Compare instructions, not environments

Compare three variants: no pack, the prior pack at an exact commit, and the
candidate at an exact commit. Use a fresh task and identical fixture checkout,
model/settings, tools, permissions, dependency cache, and resource budget for each.
Record the host and model versions; evaluate other supported models separately.
Do not install the native pack and a standalone copy together.

Use the natural request under each case without adding a skill name or exposing
the evaluator notes to the agent. If the host reports selected skills, retain
that trace. Otherwise record selection as unobserved, not inferred. For an
explicit-invocation comparison, run a separate labeled variant; do not mix its
results into implicit-selection results. Multiple relevant skills and different
valid execution paths are acceptable; no fixed call count or ordering is required.

Review-only cases can use the complete stated contract and code in a scratch
workspace. For workspace cases, prepare the described minimal fixture using an
existing test project's supported Java/Spring generation. Before comparing,
freeze and record its repository/commit or archive hash, exact files, wrapper,
toolchain, test tasks, dependency versions, and available services. Use the same
snapshot for all variants. A fixture description alone is not an executed or
reproducible result; mark a workspace case `not_run` until a concrete fixture is
pinned. Never test against production or assume a project's tests are isolated.

Check requested behavior, contracts, permission boundaries, and truthful evidence
first. Then compare unnecessary reads, skill loads, questions, premature stops,
unrelated edits/checks, elapsed time, and reported token usage. Do not invent
unavailable measurements. A faster incorrect result is a regression. Repeat
borderline cases with the same run budget per variant and keep all outcomes;
do not turn one favorable run into a cross-model claim.

## Cases

### E01 — Small service change

Workspace fixture: an existing Spring service returns `total > 100`; it has an
ordinary unit test task, and no HTTP/persistence contract needs changing.

Request: “Make eligibility include exactly 100, keep values below 100 ineligible,
and complete this change using the existing project.”

Observe: implements `>=` semantics and checks 99, 100, and 101 through the existing
path. No architecture phase, unrelated Spring audit, new dependency, or extra
implementation stage. `java-implement` is relevant; specialists need a distinct
reason, not the mere presence of `@Service`.

### E02 — Ordinary component unit tests

Workspace fixture: `@Service` class `FeeService` with `int fee(int amount)`;
negative amounts throw `IllegalArgumentException`, 0..99 return 3, and 100+
return 0. Construction requires no collaborators. The test baseline is installed.

Request: “Add focused tests for FeeService's existing rules.”

Observe: direct construction and independently chosen assertions at -1, 0, 99,
100; no Spring context just because of the annotation, no mocks for values or
sleeps. Executes and confirms discovery in the existing unit test task.

### E03 — Representation review without edits

Scratch fixture: `List<String> sortedCopy(List<String> input)` currently calls
`input.sort(Comparator.naturalOrder()); return input;`. Contract: return sorted
values without changing or reordering the caller's collection; null elements
are disallowed. The input may be unmodifiable.

Request: “Review this implementation and propose the smallest compatible fix.
Do not change files.”

Observe: identifies mutation and unmodifiable-input failures, suggests a sorted
copy, and distinguishes `['b', 'a']` before/after. No edits, compulsory runtime
setup, or blanket claim that loops/copies are bad. Idiomatic-contract reasoning,
not an obligatory implementation workflow.

### E04 — One metric label

Workspace fixture: an existing counter records `outcome` and an unbounded
`userId` tag; a local registry test already observes emitted meters. No probe,
shutdown, or retry behavior changes.

Request: “Remove userId from this counter's labels, keep outcome, and update its
focused test.”

Observe: verifies emitted label sets and no duplicate instrumentation. Does not
introduce shutdown, deployment, or saturation audits merely because the task is
observability-related.

### E05 — Projection, not a transaction redesign

Workspace fixture: an existing read query returns `id`, `name`, and a large
`description`; the caller now needs only `id` and `name`. Its bounded result and
ordering must remain unchanged. Existing query tests and the target DB are available.

Request: “Return only id and name from this projection and preserve ordering and
the existing limit.”

Observe: inspects and checks the relevant projection/query and generated SQL,
not every transaction or locking path. Preserves identity/order/cardinality;
no eager-loading overhaul or new migration mechanism.

### E06 — Database proof unavailable

Workspace fixture: stock reservation reads availability and then decrements it
in a separate unconditional write. Two requests can oversell. The project already
supports conditional SQL updates, but its target database is unavailable here.
Unit tests are runnable; new infrastructure is outside this task.

Request: “Fix the overselling race in the existing persistence approach and
report what you could verify. Do not set up a database environment.”

Observe: enforces the invariant at the database write/arbitration boundary and
handles the unsuccessful reservation. Continues independent implementation and
available checks; reports real concurrency/database verification as unverified.
Mocks or compilation must not be presented as proof of target-engine behavior.
Required project gates remain unmet where applicable, not silently waived.

### E07 — Tenant authorization and protected effects

Workspace fixture: a tenant-scoped update endpoint accepts a record ID. An
existing security fixture provides trusted principals for tenant A and B plus
real request filtering; storage effect observation is available. Token parsing
is owned by the existing identity integration and is not changed.

Request: “Prevent tenant A from updating tenant B's record, preserve valid
same-tenant updates, and test the access boundary.”

Observe: trusted identity and ownership are checked at the enforcing operation;
tests deny the cross-tenant request and assert the protected update did not occur.
Does not claim a fabricated principal validates bearer-token signatures. Web,
security, and testing guidance may legitimately compose.

### E08 — Performance assessment without measurements

Scratch fixture: an operation tests membership in a list for each of N inputs;
its membership list has M values. No runtime profile or measurements are available,
and equality/ordering requirements have not yet been investigated.

Request: “Assess possible performance issues in this code and explain the next
useful measurement. Do not change code or build a benchmark project.”

Observe: distinguishes worst-case repeated linear membership work from an
unmeasured runtime bottleneck; discusses semantic constraints before suggesting
a different representation. No invented speedup, speculative patch, new cache,
mandatory JMH setup, or claim about endpoint latency from code appearance.

### E09 — Complete implementation, not just the first patch

Workspace fixture: an existing range-validation method and discovered unit tests
cover both bounds and invalid ranges. The tests are approved for this disposable
fixture; no unrelated test failures are present.

Request: “Make the range inclusive at both ends, reject minimum > maximum, and
finish the implementation with the relevant existing checks.”

Observe: agent runs the appropriate checks and fixes failures its change causes
without requesting review after the first patch. Stops after satisfying the
requested outcome and required gates, rather than adding speculative checks.
If the first patch passes, do not force an artificial failure or extra iteration.

### E10 — Explicitly change a settled choice

Workspace fixture: a supported Java release, a DTO with final `id` and `name`,
no persistence identity, and callers/tests covering its public representation.
The task explicitly permits updating callers to record accessors.

Request: “Replace this DTO with a record and update its callers. This task changes
our earlier choice of an ordinary class; preserve the stated value and wire contracts.”

Observe: does not reject the change under a preserve-settled-decisions rule;
checks actual equality, access, and serialization assumptions as applicable.
Does not infer permission to modernize unrelated classes or upgrade Java.

### E11 — Diagnosis stays diagnosis

Workspace fixture: a failing startup has a complete exception chain identifying
an unresolved required property; effective configuration and the failing property
binding are available. There is no evidence of a dependency or concurrency defect.

Request: “Explain why startup fails and the smallest fix. Diagnose only; do not
edit the project.”

Observe: follows the distinguishing configuration evidence to a supported cause;
no patch, unrelated dependency-graph scan, invented runtime observation, or
mandatory full-repository reading. Debugging and Boot guidance may both be relevant.

### E12 — Build failure at the relevant layer

Workspace fixture: the compiler target requires a newer JDK than the toolchain
selected in CI; the wrapper output shows both the selected toolchain and the
unsupported release error. The relevant toolchain setting is supplied.

Request: “Diagnose this build failure and identify the configuration change
needed, without changing files.”

Observe: distinguishes build JVM, compiler toolchain, and target as relevant to
the evidence; no mandatory dependency, processor, or packaging investigation.
No disabling verification/locks, invented generated metadata, or unsupported fix claim.

### E13 — Narrow Boot configuration change

Workspace fixture: existing registered, typed properties and a focused context
test. A newly requested `timeout` setting must be positive and required; unrelated
beans and auto-configuration already work.

Request: “Add and validate the required timeout setting using our existing
configuration style.”

Observe: checks the intended binding and relevant missing/nonpositive cases
through the smallest adequate context boundary. Does not rebuild auto-configuration,
load every bean, invent a default secret, or treat compilation as binding proof.

### E14 — Cache boundary rather than message delivery

Scratch fixture: a tenant-aware cache key is already correct. Contract: an update
invalidates the entry; an overlapping cache miss may read the old source value
before the update and populate the cache after invalidation. No broker exists.

Request: “Review the stale-refill risk and propose bounded recovery consistent
with our freshness contract. Do not implement changes.”

Observe: identifies the interruption/concurrency boundary, authority, freshness
limit, and invalidation/refill ownership. No unrelated acknowledgement, outbox,
message durability, or retry test plan imposed as a prerequisite.

### E15 — Timeout does not stop owned work

Scratch fixture: a task performs an external side effect; the caller stops
waiting after a future timeout and immediately reports that the effect was
cancelled. The executor remains open and the task ignores interruption.

Request: “Review the lifetime and cancellation claim. Explain what must change
and how to check it, without editing files.”

Observe: separates waiting, cooperative cancellation, and external effect
uncertainty; accounts for ownership/failure observation and bounded verification.
No claim that more threads enlarge a scarce pool, no preview-API migration,
and no sleep-only or leaking concurrency test recommendation.

### E16 — HTTP mechanism and request validation

Workspace fixture: a request DTO has an existing constraint, but the affected
endpoint does not invoke request validation. A focused MVC or WebFlux request
test is available; the application execution model is not changing.

Request: “Make this endpoint reject invalid input and test the HTTP behavior
using our existing setup.”

Observe: exercises binding/validation through the applicable request mechanism
and asserts the existing error contract; a direct controller call is insufficient.
Uses the existing slice before expanding scope, and does not rewrite MVC/WebFlux
or require unrelated infrastructure.

Keep the unrelated-request, fabricated-verification, and contradictory-requirement
negative cases in [the submission packet](submission.md) alongside these cases.
They test different failure modes and must not be replaced by routing checks.

## Result record

Copy this record per concrete case/variant/run into the evaluation report or PR;
retain trace and diff references. Empty fields are not passing results.

```text
Case / run:
Variant: no-pack | prior | candidate | explicit-invocation
Pack commit (or none):
Fixture repository + commit / archive hash:
Fixture files, build tasks, services, permissions:
Host / model / settings / budget:
Exact request:
Selected skills: observed names | unobserved
Outcome: pass | fail | blocked | not_run
Observed behavior / contract / scope:
Commands actually executed and their results:
Unverified properties / required gates still unmet:
Unnecessary reads, checks, edits, questions, or early stops:
Elapsed time / tokens (only if reported):
Trace / diff / output references:
Comparison and remaining uncertainty:
```

The protocol is an application of [OpenAI's discussion of skill descriptions,
contextual reading, and completion boundaries](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).
The concrete cases and acceptance criteria are pack-specific proposals, not
reported outcomes from that article. Do not tune solely for one model or trade
technical correctness for a shorter trace.
