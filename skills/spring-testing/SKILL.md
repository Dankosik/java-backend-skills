---
name: spring-testing
description: "Mechanism. Use when a Spring test must establish HTTP handling, configuration, security, persistence, or infrastructure behavior, including Testcontainers integration."
---

# Spring Testing

**Prove the mechanism.** Identify what makes the promised behavior true, then choose the smallest test boundary that includes it. Select scenarios exposing a relevant failure, not every Spring subsystem. A direct method call cannot prove request validation; a mock cannot prove transaction or security interception. Preserve requirements and settled technical choices unless the task explicitly changes them.

Use the project's Spring generation, dependency management, and existing test setup when choosing APIs. Use a slice for a focused framework contract, a full context for composition, and a running server when real HTTP behavior matters. A missing slice collaborator is a configuration question before it is a reason to load the whole application.

Keep the mechanism under test real. Mock only outside that boundary. Security tests must exercise the relevant filter chain; a fabricated authenticated principal establishes authorization behavior, not token validation. Database constraints, locking, and isolation need the target engine and real transactions.

Ask where the effect becomes observable. Preserve contract-relevant distinctions in observed responses and effects; decoding, normalization, or helpers must not conceal a violation. Flush is not commit; cached entity state is not a storage read. Test-side rollback does not undo server or worker transactions. Align container lifetime with context lifetime and clean up committed fixtures.

Control concurrency at a meaningful boundary, bound waits, and surface worker failures. Repeated sleeps or swallowed exceptions cannot establish an eventual outcome.

For review, explain the missing proof without editing. When writing tests, run the relevant existing task within environment permissions, confirm discovery, and fix failures caused by the change. Report the exact boundary covered. If required infrastructure is unavailable, name the unverified property and blocker; do not claim weaker tests prove it or create a new environment unless the task calls for one. Required project gates remain required.
