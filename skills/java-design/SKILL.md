---
name: java-design
description: "Cohesion. Use when Java responsibilities, package boundaries, domain models, or abstractions make a backend change harder to reason about."
---

# Java Design

Design for **cohesion**: a business decision should have one natural home, and callers should need little knowledge of its implementation. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Trace the requested behavior through the existing code before choosing a pattern. Put invariants where every relevant caller encounters them. Keep transport, business policy, and persistence distinguishable at the boundaries that matter; let the problem determine how many classes that requires.

Evaluate an abstraction by the complexity it removes from its callers. Keep it when it hides a real policy, variation, or dependency direction. Collapse it when it merely forwards the same knowledge through another layer. A single implementation can justify an interface; a naming convention alone cannot.

Prefer cohesive feature packages, narrow visibility, composition, and explicit domain transitions. Use the project's established architecture and Java baseline. Let new structure answer a current pressure rather than an imagined future.

For refactoring, compare caller-visible behavior before and after, including failures and effect ordering. Similar-looking branches may express different contracts.

Finish when the changed responsibility has a clear owner, each retained boundary earns its cost, and focused checks preserve the behavior that matters.
