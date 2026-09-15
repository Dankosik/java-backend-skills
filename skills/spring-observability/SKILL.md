---
name: spring-observability
description: "Operability. Use when Spring metrics, traces, logs, health probes, or shutdown behavior must explain and support a backend operation."
---

# Spring Observability

Design for **operability**: begin with the requested operational question, then choose the smallest signal that answers it. Preserve requirements and settled technical choices unless the task explicitly changes them.

Follow the affected operation through its existing instrumentation. Keep logical outcomes distinct from retry attempts. Use the project's configured registries and instrumented clients so added signals compose with existing metrics and traces.

Give each signal a purpose: metrics describe aggregate behavior, traces explain a path, and logs preserve actionable events. Bound metric cardinality by the combinations of dimension values. Put correlation where it helps diagnosis, carrying context across affected asynchronous boundaries without carrying secrets or treating telemetry as identity authority.

When changing probes, treat them as control inputs. Liveness should reflect local progress; readiness should reflect this instance's ability to serve its contract. Consider what the platform will do when a shared dependency fails.

When changing shutdown behavior, follow admission, in-flight work, acknowledgement, and resource release. Align the application's drain budget with its environment and observe unfinished work. An isolated metric or log change does not require this lifecycle audit.

For review, explain whether the signal answers the question without editing. For changes, finish when the requested question is answered by the affected signal or lifecycle behavior, with bounded cardinality and no unintended duplication. Verify emitted signals; check saturation or shutdown when the task affects them. Report actual results and distinguish local evidence, unavailable checks, and deployment evidence.
