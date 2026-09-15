---
name: java-concurrency
description: "Lifetime. Use when Java tasks, executors, virtual threads, or shared state require cancellation, capacity bounds, or concurrent correctness."
---

# Java Concurrency

**Lifetime.** Account for affected tasks from admission to termination: who owns them, observes failure, waits for completion, and cancels them when the initiating operation ends. Start from the actual execution model and supported JDK; do not introduce preview APIs incidentally. Preserve requirements and settled technical choices unless the task explicitly changes them.

Separate concurrency from capacity. Count active work, waiting work, and scarce dependencies on the affected path. Virtual threads make waiting cheaper; they do not enlarge database pools or accelerate CPU work. A semaphore limiting active calls can still leave unbounded pending tasks.

Trace relevant failure and shutdown paths before choosing an executor or future composition. A timeout ends waiting; it does not prove an external effect stopped. Cancellation is cooperative. Preserve interruption, observe background failures, and close only resources owned by the current scope. Remember that executor close can wait beyond an earlier future timeout.

Follow shared state and context across changed thread boundaries. Concurrent containers do not make compound operations atomic, and JVM locks do not coordinate separate service instances. Verify transaction, security, and logging context when those contexts cross the boundary. Diagnose pinning using the actual JDK rather than a remembered blanket rule.

For review, explain the affected lifetime or shared-state risk without editing. For changes, verify the relevant conflict, cancellation, saturation, or shutdown behavior using controlled coordination and bounded tests that leave no running work. Select checks for the changed property, not every concurrency topic; report actual results and unavailable evidence.
