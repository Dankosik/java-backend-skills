---
name: java-design
description: "Cohesion. Use when deciding or reviewing Java responsibilities, domain boundaries, or abstractions for a concrete change."
---

# Java Design

Design for **cohesion**: a business decision should have one natural home, and callers should need little knowledge of its implementation. Preserve requirements and settled technical choices unless the task explicitly changes them. Design is not a mandatory phase before implementation.

Trace the requested behavior through the existing code before choosing a pattern. Put invariants where every relevant caller encounters them. Keep transport, business policy, and persistence distinguishable at the boundaries that matter; let the problem determine how many classes that requires.

Evaluate an abstraction by the complexity it removes from its callers. Keep it when it hides a real policy, variation, or dependency direction. Collapse it when it merely forwards the same knowledge through another layer. A single implementation can justify an interface; a naming convention alone cannot.

Favor cohesive responsibilities, narrow visibility, composition, and explicit domain transitions within the established architecture and Java baseline. Feature packages can help when package boundaries are the problem; that preference alone does not justify reorganizing the project. Let new structure answer a current pressure rather than an imagined future.

For refactoring, compare caller-visible behavior before and after, including failures and effect ordering. Similar-looking branches may express different contracts.

For analysis or review, explain the responsibility problem and smallest justified change without editing files. For implementation, finish when the changed responsibility has a clear owner, retained boundaries earn their cost, and focused checks preserve affected behavior. Report actual verification and any blocker.
