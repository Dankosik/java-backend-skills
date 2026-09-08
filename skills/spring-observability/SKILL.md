---
name: spring-observability
description: "Operability. Use when Spring metrics, traces, logs, health probes, or shutdown behavior must explain and support a backend operation."
---

# Spring Observability

Design for **operability**: begin with the operational question, then choose the smallest signal that answers it. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Follow the business operation through its existing instrumentation. Keep logical outcomes distinct from retry attempts. Use the project's configured registries and instrumented clients so added signals compose with existing metrics and traces.

Give each signal a purpose: metrics describe aggregate behavior, traces explain a path, and logs preserve actionable events. Bound metric cardinality by the combinations of dimension values. Put correlation where it helps diagnosis, carrying context across asynchronous boundaries without carrying secrets or treating telemetry as identity authority.

Treat probes as control inputs. Liveness should reflect local progress; readiness should reflect this instance's ability to serve its contract. Consider what the platform will do when a shared dependency fails.

Follow shutdown through admission, in-flight work, acknowledgement, and resource release. Align the application's drain budget with its environment and observe what happens to unfinished work.

Finish when success, failure, and saturation are distinguishable without duplicate or unbounded instrumentation. Verify emitted signals and the affected lifecycle behavior, and distinguish local evidence from deployment evidence.
