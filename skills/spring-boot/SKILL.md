---
name: spring-boot
description: "Composition. Use when Spring Boot bean wiring, configuration, auto-configuration, or startup behavior needs implementation or diagnosis."
---

# Spring Boot

**Composition.** Make construction and configuration explainable. Start with the project's actual Boot generation and trace how the affected object is created, which settings reach it, and who owns its lifetime. Preserve requirements and settled technical choices unless the task explicitly changes them.

Use the container where it supplies a useful boundary. Prefer constructor dependencies and ordinary objects for ordinary calculations. A dependency cycle is a question about responsibilities before it is a question about injection tricks. Mutable request state does not belong to a shared singleton.

Treat auto-configuration as existing implementation. Before adding a bean or enable annotation, determine which default it replaces and what behavior disappears with that default. Prefer a narrow customization over reconstructing Boot's setup.

Give related configuration a typed home. Decide which values are required, defaulted, or absent; validate that decision where settings enter the application. Constructor-bound properties need properties registration, not ordinary component construction. A dummy secret is not a meaningful default.

For diagnosis or review, explain the composition issue without editing. When changing wiring or settings, check the changed composition and its relevant invalid configuration using the smallest existing context boundary. Compilation alone cannot prove either. Report what was exercised and any unavailable verification; do not audit unrelated beans or create a full test environment merely to finish.
