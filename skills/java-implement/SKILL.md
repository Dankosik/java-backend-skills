---
name: java-implement
description: "Execution. Implement requested Java or Spring behavior within the project's existing contracts and technical choices."
---

# Java Implement

**Execution.** When the intended behavior is clear, implement it directly. Preserve supplied requirements and settled technical decisions unless the task explicitly changes them; routine implementation choices remain yours.

Read the affected code and callers, then extend the existing path. Resolve local details using the project's Java version and conventions.

**Reuse.** Before writing a technical helper, check likely existing project, JDK, Spring, or declared-library APIs for matching semantics. Keep the search proportional to the helper. Write custom mechanics for a concrete semantic or operational gap; keep business policy explicit. A wrapper should add domain meaning or adaptation, not merely rename a library call.

**Clarity.** Write for the next reader: intention-revealing names, cohesive responsibilities, explicit control flow, and visible effects and failure paths. Keep changes local and idiomatic. Apply SOLID, DRY, and YAGNI as heuristics: abstract shared knowledge, preserve distinct business rules, and add structure only for current requirements.

New dependencies, configuration, and adjacent cleanup need a present requirement. If a contradiction prevents correct implementation, identify the exact conflict and continue independent work. Ask only for information that materially changes the required outcome.

Carry the change through appropriate verification. Use focused checks that detect a plausible contract violation, including its meaningful failure case, and respect required project checks. Within the environment's permissions, fix failures caused by the change and rerun affected checks without stopping for review after the first patch.

Finish when the requested behavior and required checks are satisfied, or report the concrete blocker, actual verification, and unresolved requirement. Do not add unrelated cleanup or a new test environment as an unrequested completion gate. Unavailable verification is a limitation, not a passed check; never assume tests have no production access.
