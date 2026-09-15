---
name: java-idiomatic
description: "Contracts. Use for Java representation and transformation choices where caller-visible semantics or readability need attention."
---

# Java Idiomatic

**Contracts.** Make the code's contract easier to see. Before changing its shape, identify what callers observe: values, identity, mutation, absence, ordering, effects, and failures. Use the project's supported Java release and conventions. Preserve requirements and settled technical choices unless the task explicitly changes them.

Choose the representation that tells that story directly. Records fit component-based values; ordinary classes fit identity or controlled mutation. Remember that records and collection copies are shallow. Sealed types fit genuinely closed alternatives. Streams fit understandable transformations; loops often make effects and branching clearer. Optional should clarify absence, not spread wrappers through every layer.

**Reuse.** Prefer existing JDK, Spring, or library operations over handwritten utility logic when their semantics match. Keep wrappers only when they add domain meaning or adaptation. Judge modernization by clearer caller contracts, not a different spelling.

Preserve the details a tidy rewrite can accidentally change: lazy evaluation, null acceptance, collection order and mutability, equality, rounding, time boundaries, and exception causes. Never put required effects in a stream stage that may be skipped.

For review, explain the contract risk and smallest compatible improvement without editing files. When changes are requested, apply the smallest improvement and check the behavior it could disturb. State actual validation; avoid unrelated style churn.
