---
name: java-performance
description: "Evidence. Use to assess or improve Java latency, throughput, CPU, memory, or startup behavior, or to benchmark a specific claim."
---

# Java Performance

**Evidence.** Turn “slow” into a measurable question: the affected workload, metric, runtime, and resource budget. Preserve requirements and settled technical choices unless the task explicitly changes them. Match the work to the request: code assessment, measurement, or a verified optimization.

For a code assessment, separate properties established from code from hypotheses about runtime impact. Explain the next discriminating measurement; do not edit code, create a benchmark project, or claim a bottleneck or speedup without supporting evidence.

For measurement or optimization, establish a comparable baseline and follow where resources actually go: computation, allocation, retained memory, locks, queues, database work, or remote calls. Choose the smallest diagnostic that distinguishes plausible causes. JFR and `jcmd` can help when runtime access is available; respect permissions, captured-data sensitivity, and collection impact.

Form a falsifiable hypothesis before changing code. Prefer removing demonstrated waste over speculative caching, parallelism, object pools, or tuning flags. Preserve error, ordering, and consistency behavior.

Match proof to the claim. JMH fits isolated JVM operations, with warmup, forks, realistic state, and observed results. Representative application load fits service latency and throughput. A microbenchmark gain does not establish endpoint improvement; heap growth alone does not identify a leak.

For a requested optimization, compare before and after under equivalent conditions, including relevant errors and saturation. Report the cause, change, result, and evidence limits. If measurement is unavailable or inconclusive, state that limit and prefer the simpler correct implementation; do not invent infrastructure or a speedup as a completion requirement.
