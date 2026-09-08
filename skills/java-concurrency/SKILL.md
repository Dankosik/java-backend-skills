---
name: java-concurrency
description: "Lifetime. Use when Java tasks, executors, virtual threads, or shared state require cancellation, capacity bounds, or concurrent correctness."
---

# Java Concurrency

**Lifetime.** Account for every task from admission to termination. Identify who owns it, observes failure, waits for completion, and cancels it when the initiating operation ends. Start from the actual execution model and supported JDK; do not introduce preview APIs incidentally. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Separate concurrency from capacity. Count active work, waiting work, and scarce dependencies. Virtual threads make waiting cheaper; they do not enlarge database pools or accelerate CPU work. A semaphore limiting active calls can still leave unbounded pending tasks.

Trace failure and shutdown before choosing an executor or future composition. A timeout ends waiting; it does not prove an external effect stopped. Cancellation is cooperative. Preserve interruption, observe background failures, and close only resources owned by the current scope. Remember that executor close can wait beyond an earlier future timeout.

Follow shared state and context across each thread boundary. Concurrent containers do not make compound operations atomic, and JVM locks do not coordinate separate service instances. Verify propagation of transaction, security, and logging context. Diagnose pinning using the actual JDK rather than a remembered blanket rule.

Prove the relevant conflict, cancellation, saturation, or shutdown behavior with controlled coordination and bounded tests. Ensure the test itself leaves no running work.
