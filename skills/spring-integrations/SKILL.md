---
name: spring-integrations
description: "Delivery semantics. Use when Spring outbound calls, retries, messages, scheduled work, or caches must remain correct across delay, duplication, failure, or restart."
---

# Spring Integrations

Reason in **delivery semantics**: what can repeat, what can disappear, and what can remain unknown at each boundary. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Trace an operation from intent through effect to acknowledgement. Distinguish definitive rejection from a lost response after success. Tie safe replay to a stable operation identity and equivalent request meaning; a timeout alone cannot establish that nothing happened.

Budget attempts, elapsed time, concurrency, and queued work together. Place retry policy where effect semantics are known, using the project's actual framework and client versions. Recovery should reduce failure impact without multiplying downstream load.

For messages and jobs, follow commit, publication, acknowledgement, redelivery, and process death. Choose durability and coordination to match the promised outcome. Local events and scheduling have local lifetimes; broker guarantees end at their documented boundary.

For caches, identify the authority, key identity, freshness contract, and invalidation owner. Consider concurrent stale refill and origin load during failure. Let a measured need justify the cache.

Challenge the design at its most consequential interruption point: success before response loss, commit before publication, or effect before acknowledgement. Finish when that path has a bounded recovery outcome and a check that observes the actual effect.
