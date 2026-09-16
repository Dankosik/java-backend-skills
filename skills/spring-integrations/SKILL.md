---
name: spring-integrations
description: "Delivery semantics. Use when Spring outbound calls, retries, messages, scheduled work, or caches must remain correct across delay, duplication, failure, or restart."
---

# Spring Integrations

Reason in **delivery semantics**: what can repeat, disappear, or remain unknown at the affected boundary. Preserve requirements and settled technical choices unless the task explicitly changes them. Apply the relevant call, message/job, or cache reasoning rather than auditing all three.

For outbound calls, trace intent through effect to acknowledgement. Distinguish definitive rejection from a lost response after success. Tie safe replay to a stable operation identity and equivalent request meaning; a timeout alone cannot establish that nothing happened.

Where retries or background work are involved, budget attempts, elapsed time, concurrency, and queued work together. Place retry policy where effect semantics are known, using the project's actual framework and client versions. Recovery should reduce failure impact without multiplying downstream load.

For messages and jobs, follow commit, publication, acknowledgement, redelivery, and process death. Choose durability and coordination to match the promised outcome. Where deduplication is needed, examine concurrent claims and the gap between recording completion and performing the effect; a check-then-mark sequence cannot close either gap. Reusing an operation identity with different request meaning must not silently replay success. Local events and scheduling have local lifetimes; broker guarantees do not by themselves establish exactly-once business effects.

For caches, identify the authority, key identity, freshness contract, and invalidation owner. Consider concurrent stale refill and origin load during failure when relevant. Let a measured need justify introducing a cache.

For review, explain the consequential failure path without editing. For changes, check the affected promise: bounded replay after a lost response, recovery between effect and acknowledgement, or cache freshness/invalidation and relevant origin load. Observe the actual effect at the smallest adequate boundary. Finish with the result and evidence limits, not checks for every integration type or newly invented infrastructure.
