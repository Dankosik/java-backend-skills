---
name: spring-testing
description: "Mechanism. Use when a Spring test must establish HTTP handling, configuration, security, persistence, or infrastructure behavior, including Testcontainers integration."
---

# Spring Testing

**Prove the mechanism.** Identify what makes the promised behavior true, then choose the smallest test boundary that actually includes it. A direct method call cannot prove request validation; a mock cannot prove transaction or security interception. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Read the project's Spring generation, dependency management and existing test setup before selecting annotations or starters. Use a slice for a focused framework contract, a full context for composition, and a running server when real HTTP behavior matters. A missing slice collaborator is a configuration question before it is a reason to load the whole application.

Keep the mechanism under test real. Mock only outside that boundary. Security tests must exercise the relevant filter chain; a fabricated authenticated principal establishes authorization behavior, not token validation. Database constraints, locking and isolation need the target engine and real transactions.

Ask where the effect becomes observable. Flush is not commit; cached entity state is not a storage read. Test-side rollback does not undo server or worker transactions. Align container lifetime with context lifetime and clean up committed fixtures.

Control concurrency at a meaningful boundary, bound waits and surface worker failures. Repeated sleeps or swallowed exceptions cannot establish an eventual outcome.

Run the relevant existing test task, confirm discovery, and describe exactly which boundary the result covers.
