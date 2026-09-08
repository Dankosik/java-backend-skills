# Java Backend Skills

Small, independent skills for clean, idiomatic Java and Spring backend development.

Each skill starts with a familiar engineering concept and directs a decision: what to inspect, how to reason, and what would make the result convincing. The model brings its language and framework knowledge. Your project supplies the versions, conventions, and constraints.

One `SKILL.md` per skill. No reference libraries, setup ceremony, mandatory process, or dependencies between skills.

## Install

Use the [Agent Skills CLI](https://github.com/vercel-labs/skills) and choose your coding agent and desired skills:

```sh
npx skills add Dankosik/java-backend-skills
```

Install only the testing skills:

```sh
npx skills add Dankosik/java-backend-skills --skill java-unit-testing spring-testing
```

Or install from a local checkout:

```sh
npx skills add ./java-backend-skills
```

You can also copy any individual skill folder into the skills directory supported by your agent. Each folder is self-contained. There are no runtime dependencies; Node.js is needed only if you choose the CLI installer.

## Choose the decision

| Skill | Leading concept | Use it for |
| --- | --- | --- |
| [java-implement](skills/java-implement/SKILL.md) | Execution | Turn clear requirements or a finished technical design into working code |
| [java-idiomatic](skills/java-idiomatic/SKILL.md) | Contracts | Clear Java implementations and behavior-preserving cleanup |
| [java-design](skills/java-design/SKILL.md) | Cohesion | Responsibilities, domain models, and useful abstractions |
| [java-concurrency](skills/java-concurrency/SKILL.md) | Lifetime | Shared state, executors, virtual threads, cancellation, and bounds |
| [java-debugging](skills/java-debugging/SKILL.md) | Causality | Bugs, startup failures, hangs, and flaky behavior |
| [java-performance](skills/java-performance/SKILL.md) | Evidence | Measured latency, throughput, CPU, memory, and startup improvements |
| [java-build](skills/java-build/SKILL.md) | Resolution | Maven, Gradle, toolchains, processors, and dependencies |
| [spring-boot](skills/spring-boot/SKILL.md) | Composition | Bean wiring, configuration, auto-configuration, and startup |
| [spring-web](skills/spring-web/SKILL.md) | Translation | MVC/WebFlux endpoints, validation, serialization, and HTTP contracts |
| [spring-data](skills/spring-data/SKILL.md) | Atomicity | Queries, persistence, transactions, migrations, and data races |
| [spring-security](skills/spring-security/SKILL.md) | Authorization | Trusted identity, resource access, tenancy, and browser security |
| [spring-integrations](skills/spring-integrations/SKILL.md) | Delivery semantics | External calls, retries, messages, jobs, and caches |
| [spring-observability](skills/spring-observability/SKILL.md) | Operability | Metrics, traces, logs, probes, and shutdown |
| [java-unit-testing](skills/java-unit-testing/SKILL.md) | Behavior | JUnit Jupiter, Mockito, AssertJ, and deterministic unit tests |
| [spring-testing](skills/spring-testing/SKILL.md) | Mechanism | Spring slices, application tests, Testcontainers, and real infrastructure |

Use `java-implement` when the task is clear and the work is to implement it. Use a specialist when its particular decision needs attention. Each preserves supplied requirements and settled technical choices; none requires a design phase. Debugging identifies an uncertain cause; performance work measures a resource claim. Unit tests isolate ordinary behavior; Spring tests retain the framework or infrastructure mechanism being tested.

## Use

Ask naturally, or select a skill through your agent's explicit skill invocation:

- “Use java-idiomatic to simplify this service while preserving its public behavior.”
- “Use java-implement to implement this specification without changing its technical design.”
- “Use spring-data to fix the duplicate reservation race.”
- “Use java-unit-testing to cover the discount rules with JUnit and Mockito.”
- “Use spring-testing to test this endpoint's validation and access control.”

These skills adapt to the repository's Java release and Spring generation. They do not prescribe an upgrade, architecture, or reactive rewrite. The pack focuses on application-level Java/Spring backend work; provider-specific deployment and specialist infrastructure remain project concerns.

## Contribute

Keep each skill independent and decision-focused. Prefer an established concept over a new glossary, a discriminating trigger over a capability catalog, and an observable outcome over a long checklist. Improve wording against a realistic task that exposed a weakness. Keep version lookups and API tutorials out of the skill.

The pack uses the [Agent Skills format](https://agentskills.io/specification). Structural validity and a few useful examples do not establish a universal improvement across models.

## Acknowledgements

Inspired by the focused technical judgments in [Dankosik/go-service-template-rest](https://github.com/Dankosik/go-service-template-rest) and the leading concepts and composability of [mattpocock/skills](https://github.com/mattpocock/skills). The Java/Spring instructions are independently written.

[MIT license](LICENSE).
