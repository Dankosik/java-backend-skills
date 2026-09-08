---
name: java-performance
description: "Evidence. Use for a reported Java latency, throughput, CPU, memory, or startup problem, or a requested benchmark."
---

# Java Performance

**Evidence.** Turn “slow” into a measurable question. Identify the affected workload, metric, runtime, and resource budget, then establish a comparable baseline. If evidence is missing, collect it or describe the uncertainty; do not nominate a bottleneck from code appearance. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Follow where time and resources actually go: computation, allocation, retained memory, locks, queues, database work, or remote calls. Choose the smallest diagnostic that distinguishes plausible causes. JFR and `jcmd` are useful when runtime evidence is available; account for the impact of collecting it.

Form a falsifiable hypothesis before changing code. Prefer removing the operation shown to be wasteful over introducing caching, parallelism, object pools, or tuning flags speculatively. Preserve error, ordering, and consistency behavior.

Match proof to the claim. Use JMH for isolated JVM operations, with warmup, forks, realistic state, and observed results. Use representative application load for service latency and throughput. A microbenchmark gain does not establish endpoint improvement; heap growth alone does not identify a leak.

Compare before and after under equivalent conditions, including errors and saturation. Report the measured cause, change, result, and limits of the evidence. If the result is inconclusive, retain the simpler correct implementation rather than inventing a speedup.
