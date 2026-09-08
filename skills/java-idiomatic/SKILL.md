---
name: java-idiomatic
description: "Contracts. Use when writing or simplifying Java values, methods, or collection transformations while preserving caller-visible behavior."
---

# Java Idiomatic

**Contracts.** Make the code's contract easier to see. Before changing its shape, identify what callers observe: values, identity, mutation, absence, ordering, effects, and failures. Use the project's supported Java release and existing conventions. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Choose the representation that tells that story directly. Records fit component-based values; ordinary classes fit identity or controlled mutation. Remember that records and collection copies are shallow. Sealed types fit genuinely closed alternatives. Streams fit understandable transformations; loops often make effects and branching clearer. Optional should clarify absence, not spread wrappers through every layer.

Challenge each proposed “modernization”: which decision becomes easier for the next reader? If it only trades one familiar spelling for another, leave it. Prefer existing code and the JDK before adding helpers, dependencies, or abstraction layers.

Preserve the details a tidy rewrite can accidentally change: lazy evaluation, null acceptance, collection mutability, equality, rounding, time boundaries, and exception causes. Never put required effects in a stream stage that may be skipped.

Finish with the smallest change that makes intent explicit and a focused check of the contract it could have disturbed. State actual validation; avoid unrelated style churn.
