---
name: spring-security
description: "Authorization. Use when Spring identity, filter chains, resource permissions, tenancy, or browser credentials cross a trust boundary."
---

# Spring Security

**Authorization.** Model the affected decision as subject, action, resource, and context. Establish where identity becomes trusted and where permission is enforced. Authentication answers who the caller is; it does not grant access to every object they can name. Preserve requirements and settled technical choices unless the task explicitly changes them.

Use the project's established Spring Security mechanisms. Follow the affected filter-chain selection and request rules, including relevant unmatched routes, before adding another filter or annotation. Check resource ownership and tenant scope at the operation that can enforce them; do not trust an incoming identifier as proof of permission.

For bearer tokens, preserve signature, issuer, audience, and validity checks through the framework's support. Derive authorities deliberately. Avoid custom token parsing or password handling when an existing identity integration already owns them.

Reason about browser credentials separately. Cookies or other credentials attached automatically can require CSRF protection even in a stateless API. CORS governs browser cross-origin access; it does not replace authorization. Include management and diagnostic surfaces when the changed access rules affect them.

For review, explain the trust-boundary risk without editing. For changes, test the denial that would expose the affected flaw: wrong identity, resource, tenant, permission, or token. Exercise the relevant real security path and assert the protected effect did not occur, alongside the response. A happy-path login test is insufficient. Report which enforcement path was verified and any unavailable evidence; do not broaden a local change into an unrelated security audit.
