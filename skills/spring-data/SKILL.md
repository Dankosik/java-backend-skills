---
name: spring-data
description: "Atomicity. Use when changing or reviewing a Spring query, persistence mapping, transaction boundary, concurrency control, or schema migration."
---

# Spring Data

**Atomicity.** Identify the persistence decision this task changes: result shape and fetching, a consistency invariant, or a schema transition. Preserve the project's persistence approach, resolved dependencies, requirements, and settled choices unless the task explicitly changes them. Investigate the relevant branch, not every data-access concern.

For consistency changes, ask what must remain true when requests overlap or an operation fails halfway through. Put the unit of work around that operation. Verify the boundary is invoked through Spring; self-invocation can bypass transactional interception. Understand rollback before catching exceptions. `readOnly` does not guarantee writes are impossible, and an external HTTP effect is not rolled back with the database.

Use database constraints, conditional writes, or locking where an invariant requires arbitration. A preflight existence check cannot settle a race. Choose conflict behavior deliberately instead of adding blind retries.

For query or mapping changes, work backward from the required result to the query and fetch plan. Fetch what the operation needs, with bounded cardinality; inspect relevant SQL rather than making every association eager. Keep entity identity and lifecycle separate from DTO value semantics. A projection change alone does not require a concurrency audit.

For schema changes, use the existing migration mechanism as authority; do not rewrite applied versioned migrations. When old and new application instances overlap, preserve their shared schema contract: expand compatibly, migrate existing data, then remove obsolete structures only after their consumers retire. Account for relevant backfill, locking, restart, and recovery behavior. An application rollback need not reverse a data migration; do not introduce another migration system.

For review, explain the relevant risk without editing. For changes, verify the affected property at its real boundary: rollback through the actual bean, fetching through emitted SQL, or constraints and concurrency against the relevant database. Choose applicable checks, not the whole list. Repository mocks cannot establish those properties. Reuse valid evidence, respect required checks, and report unavailable database verification as a limitation rather than a pass or an invitation to build an unrequested environment.
