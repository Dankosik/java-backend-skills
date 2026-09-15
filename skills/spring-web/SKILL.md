---
name: spring-web
description: "Translation. Use when Spring MVC or WebFlux endpoints, validation, serialization, pagination, or errors affect the HTTP contract."
---

# Spring Web

**Translation.** Treat the web layer as a translation between an HTTP contract and an application operation. Start from what the caller can observe: accepted input, identity, status, headers, response shape, and failure behavior. Preserve requirements, established contracts, and technical choices unless the task explicitly changes them.

Make the translation explicit. Bind purpose-built input and return intentional output; do not let persistence graphs or bulk property copying define the API. Separate caller-controlled fields from trusted identity and ownership. Distinguish absent, null, and empty values when they imply different operations.

Keep transport validation at entry and business decisions with the operation that owns them. Map failures through the mechanism that actually handles them; controller advice does not automatically catch security-filter errors. Prefer built-in error machinery when it fits, while retaining an established public error format and concealing internal details.

Choose execution from the real dependency chain. Preserve the current MVC or WebFlux model unless changing it is the task; a reactive signature does not make blocking persistence nonblocking. Bound collection responses and make their ordering intentional.

For review, explain HTTP contract risks without editing. For changes to HTTP handling, exercise the affected contract through the smallest request boundary that includes the changed mechanism and meaningful failure case. A direct controller call cannot prove binding, serialization, validation, or filter behavior. A pure helper change need not trigger a full HTTP audit. Report observed results and any unavailable verification without claiming a stronger boundary than was exercised.
