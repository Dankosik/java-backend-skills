---
name: java-implement
description: "Execution. Use to turn clear requirements, a specification, a technical design, or a straightforward business request into working Java or Spring code."
---

# Java Implement

**Execution.** When the intended behavior is clear, implement it directly. Treat supplied requirements and settled technical decisions as constraints, not invitations to redesign.

Read the affected code and callers, then extend the existing path. Resolve local details using the project's Java version and conventions.

**Reuse.** Before writing technical helpers, check existing project code, JDK and Spring APIs, and declared libraries such as Apache Commons. Use a matching API directly. Write custom mechanics only for a concrete semantic or operational gap; keep business policy explicit. A wrapper should add domain meaning or adaptation, not merely rename a library call.

Choose the smallest complete change that delivers the requested behavior. New abstractions, dependencies, configuration, and adjacent cleanup need a present requirement. Preserve established contracts and technical choices even when another design is personally preferable.

If a concrete contradiction prevents correct implementation, identify the exact conflict and continue any independent work. Ask only for information that materially changes the required outcome; routine implementation choices remain yours.

Verify the requested behavior with focused checks, including its meaningful failure case. Match testing effort to the change and respect existing required checks.

Finish with working code, the actual verification result, and any specific unresolved requirement. Clear tasks should end in implementation, without an unsolicited redesign or additional features.
