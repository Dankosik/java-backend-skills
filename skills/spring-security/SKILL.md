---
name: spring-security
description: "Authorization. Use when Spring identity, filter chains, resource permissions, tenancy, or browser credentials cross a trust boundary."
---

# Spring Security

**Authorization.** Model the decision as subject, action, resource, and context. Establish where identity becomes trusted and where permission is enforced. Authentication answers who the caller is; it does not grant access to every object they can name. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Use the project's established Spring Security mechanisms. Follow the actual filter-chain selection and request rules, including unmatched routes, before adding another filter or annotation. Check resource ownership and tenant scope at the operation that can enforce them; do not trust an incoming identifier as proof of permission.

For bearer tokens, preserve signature, issuer, audience, and validity checks through the framework's support. Derive authorities deliberately. Avoid custom token parsing or password handling when an existing identity integration already owns them.

Reason about browser credentials separately. Cookies or other credentials attached automatically can require CSRF protection even in a stateless API. CORS governs browser cross-origin access; it does not replace authorization. Keep exposed management and diagnostic surfaces within the same access reasoning.

Test the denial that would expose the flaw: wrong identity, wrong resource, wrong tenant, missing permission, or invalid token. Exercise the real security path and assert the protected effect did not occur, alongside the response. A happy-path login test is insufficient evidence.
