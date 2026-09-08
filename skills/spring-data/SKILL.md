---
name: spring-data
description: "Atomicity. Use when Spring queries, persistence mappings, transactions, or migrations affect consistency, concurrency, or data access."
---

# Spring Data

**Atomicity.** Start with the invariant: what must remain true when two requests overlap or one operation fails halfway through? Locate the database state and transaction boundary that can enforce it. Preserve the project's persistence approach and resolved dependencies. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Put the unit of work around the operation that needs consistency. Verify the boundary is actually invoked through Spring; self-invocation can bypass transactional interception. Understand rollback behavior before catching exceptions. `readOnly` is not a guarantee that writes are impossible, and an external HTTP effect is not rolled back with the database.

Use database constraints, conditional writes, or locking where the invariant requires arbitration. A preflight existence check cannot settle a race. Choose conflict behavior deliberately instead of adding blind retries.

Work backward from the required result to the query and fetch plan. Fetch what the operation needs, with bounded cardinality; inspect SQL rather than fixing every association to eager loading. Keep entity identity and lifecycle separate from DTO value semantics. Use the existing migration mechanism as schema authority.

Verify the claim at its real boundary: rollback through the actual bean, fetching through emitted SQL, and concurrency against the relevant database. Repository mocks cannot establish those properties. Report evidence and what remains unverified.
