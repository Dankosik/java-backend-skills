---
name: java-build
description: "Resolution. Use for Maven or Gradle build failures, toolchain changes, annotation processors, or dependency conflicts."
---

# Java Build

**Resolution.** Explain what the build actually selects before changing what it declares. Identify the failing task or requested build change and inspect the effective configuration that can explain it. Examine toolchains, processors, dependency resolution, or packaging when the evidence points to that layer, not as a universal preflight. Preserve requirements and settled technical choices unless the task explicitly changes them.

Use the project's wrapper and relevant task; an IDE's cached success can hide a broken build. Prefer the affected module and incremental tasks. Use clean builds, cache deletion, dependency refresh, or a full reactor only for a specific diagnostic need or required project gate; do not rerun unchanged successful checks without a reason. Separate the JVM running the build, the compilation toolchain, and the application runtime. `--release` constrains target APIs; source/target alone may not. Missing generated classes after a JDK change may reflect processor configuration. Use configuration supported by the project's Maven or Gradle generation.

For dependency conflicts, trace resolution to its origin. Declare directly used libraries in the consuming module rather than relying on transitive presence; preserve BOM or platform version management. Check why security overrides and exclusions exist before changing them. A parent update can change the entire effective graph.

Preserve repeatable inputs and their trust checks. Version locks and artifact verification solve different problems; neither justifies disabling the other to pass a download. Generate and review metadata rather than inventing it.

For diagnosis or review, explain the affected layer without editing. For changes, keep the build system, DSL, and runtime commitments unless changing them is the task. Validate the affected layer and required project checks, not every build phase. For dependency changes, inspect the resulting graph and relevant vulnerability evidence. Report actual versions, checks, and blockers, not an unsupported “build fixed.”
