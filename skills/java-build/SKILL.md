---
name: java-build
description: "Resolution. Use for Maven or Gradle build failures, toolchain changes, annotation processors, or dependency conflicts."
---

# Java Build

**Resolution.** Explain what the build actually selects before changing what it declares. Inspect the wrapper, selected JDKs, compiler target, plugins, annotation processors, and resolved dependency graph. Reproduce the relevant task; an IDE's cached success can hide a broken build. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Separate the JVM running the build, the compilation toolchain, and the application runtime. `--release` constrains target APIs; source/target alone may not. Missing generated classes after a JDK change may reflect processor configuration rather than application code. Use configuration supported by the project's Maven or Gradle generation.

Trace dependency conflicts to their origin. Declare directly used libraries explicitly in the consuming module rather than relying on transitive presence; preserve BOM or platform version management. Check why security overrides and exclusions exist before changing them. A parent update can change the entire effective graph.

Preserve repeatable inputs and their trust checks. Version locks and artifact verification solve different problems; neither justifies disabling the other to pass a download. Generate and review metadata rather than inventing it.

Keep the build system, DSL, and runtime commitments unless changing them is the task. Validate the layer affected: processing, compilation, tests, target-runtime linkage, or packaging. For dependency changes, inspect the resulting graph and relevant vulnerability evidence. Report actual versions and checks, not an unsupported “build fixed.”
