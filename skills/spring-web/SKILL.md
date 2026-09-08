---
name: spring-web
description: "Translation. Use when Spring MVC or WebFlux endpoints, validation, serialization, pagination, or errors affect the HTTP contract."
---

# Spring Web

**Translation.** Treat the web layer as a translation between an HTTP contract and an application operation. Start from what the caller can observe: accepted input, identity, status, headers, response shape, and failure behavior. Preserve that contract unless changing it is the task. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Make the translation explicit. Bind purpose-built input and return intentional output; do not let persistence graphs or bulk property copying define the API. Separate caller-controlled fields from trusted identity and ownership. Distinguish absent, null, and empty values when they imply different operations.

Keep transport validation at entry and business decisions with the operation that owns them. Map failures through the mechanism that actually handles them; controller advice does not automatically catch security-filter errors. Prefer built-in error machinery when it fits, while retaining an established public error format and concealing internal details.

Choose execution from the real dependency chain. Preserve the current MVC or WebFlux model; a reactive signature does not make blocking persistence nonblocking. Bound collection responses and make their ordering intentional.

Exercise the changed contract through a request, including the meaningful failure or boundary case. A direct controller call cannot prove binding, serialization, validation, or filter behavior. Report the observable result.
