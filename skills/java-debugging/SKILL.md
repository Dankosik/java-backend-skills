---
name: java-debugging
description: "Causality. Use for a Java or Spring failure, startup problem, hang, or flaky test whose root cause is uncertain."
---

# Java Debugging

Debug through **falsifiable hypotheses**. Find the first observable divergence between expected behavior and the real execution path. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Build the smallest repeatable signal for the reported symptom. Read the complete exception chain, affected callers, effective configuration, and resolved runtime versions. Separate what the evidence shows from what would explain it.

Choose the next observation for its ability to distinguish plausible causes. Follow Spring calls through the actual bean, proxy, transaction, and thread boundaries. For runtime failures, inspect runtime evidence: a source annotation or compile-time dependency is not proof of what executed.

Change one causal variable at a time. Tighten the reproduction as you learn; for intermittent failures, control scheduling and state sufficiently to make the suspected mechanism observable. Select diagnostics that fit the hypothesis and handle captured data according to its sensitivity.

Fix the cause at the shared owner, then replay the original failure and relevant neighboring paths. Keep a regression check that detects the mechanism and remove temporary instrumentation.

Finish with a supported causal explanation and observed verification. When evidence is incomplete, name the remaining hypothesis and the next discriminating check precisely.
