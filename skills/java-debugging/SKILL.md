---
name: java-debugging
description: "Causality. Use for a Java or Spring failure, startup problem, hang, or flaky test whose root cause is uncertain."
---

# Java Debugging

Debug through **falsifiable hypotheses**. Find the first observable divergence between expected behavior and the real execution path. Preserve requirements and settled technical choices unless the task explicitly changes them.

Build the smallest repeatable signal for the reported symptom. Read the complete exception chain when present; inspect affected callers, effective configuration, or resolved runtime versions when they can distinguish plausible causes. Reuse relevant observations rather than repeating a fixed inspection checklist. Separate what the evidence shows from what would explain it.

Choose the next observation for its ability to distinguish plausible causes. Follow Spring calls through relevant bean, proxy, transaction, and thread boundaries. For runtime failures, inspect runtime evidence: a source annotation or compile-time dependency is not proof of what executed.

Change one causal variable at a time. Tighten the reproduction as you learn; for intermittent failures, control scheduling and state sufficiently to make the suspected mechanism observable. Select diagnostics that fit the hypothesis, available permissions, and sensitivity of captured data.

When diagnosis is requested, finish with a supported cause or the remaining hypothesis and next discriminating check; do not edit files. When fixing is requested, fix the cause at its owner, replay the original failure and affected neighboring paths, retain a regression check, and remove temporary instrumentation. Report observed verification or the concrete blocker rather than claiming an untested fix.
