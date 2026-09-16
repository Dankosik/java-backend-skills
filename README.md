# Java Backend Skills

Small, independent skills for clean, idiomatic Java and Spring backend development.

Each skill starts with a familiar engineering concept and directs a decision: what to inspect, how to reason, and what would make the result convincing. The model brings its language and framework knowledge. Your project supplies the versions, conventions, and constraints.

One `SKILL.md` per skill. No reference libraries, setup ceremony, mandatory process, or dependencies between skills.

## Install

Versioned release: [v1.0.0](https://github.com/Dankosik/java-backend-skills/releases/tag/v1.0.0).
The source prepares 1.0.1; the commands below remain pinned to the published release until a new release is available.
Install selected skills, or the entire pack, into your current project:

```sh
npx skills@1.5.25 add "Dankosik/java-backend-skills#v1.0.0" --agent codex --skill '*' --copy
```

Use `--skill java-implement` for one skill, or `--agent claude-code` for Claude
standalone placement. Node.js >=22.20.0 is required by this installer, not by
the skill instructions.

For native Claude Code and Codex installation, add the
[Dankosik marketplace](https://github.com/Dankosik/agent-skills-marketplace), then
install `java-backend-skills@dankosik-skills`. The author catalog is available independently
of review for either provider's public directory.

[All installation methods, updates and rollback](docs/distribution.md) ·
[Versioning](docs/versioning.md) · [Changelog](CHANGELOG.md)

## Choose the decision

| Skill | Leading concept | Use it for |
| --- | --- | --- |
| [java-implement](skills/java-implement/SKILL.md) | Execution | Implement requested behavior within existing contracts and technical choices |
| [java-idiomatic](skills/java-idiomatic/SKILL.md) | Contracts | Representation and transformation choices where semantics or readability need attention |
| [java-design](skills/java-design/SKILL.md) | Cohesion | Responsibilities, domain boundaries, and abstractions for a concrete change |
| [java-concurrency](skills/java-concurrency/SKILL.md) | Lifetime | Shared state, executors, virtual threads, cancellation, and bounds |
| [java-debugging](skills/java-debugging/SKILL.md) | Causality | Bugs, startup failures, hangs, and flaky behavior |
| [java-performance](skills/java-performance/SKILL.md) | Evidence | Code assessment, measurement, or verified resource improvements, as requested |
| [java-build](skills/java-build/SKILL.md) | Resolution | Maven, Gradle, toolchains, processors, and dependencies |
| [spring-boot](skills/spring-boot/SKILL.md) | Composition | Bean wiring, configuration, auto-configuration, and startup |
| [spring-web](skills/spring-web/SKILL.md) | Translation | MVC/WebFlux endpoints, validation, serialization, and HTTP contracts |
| [spring-data](skills/spring-data/SKILL.md) | Atomicity | Changes to queries, mappings, transactions, concurrency control, or migrations |
| [spring-security](skills/spring-security/SKILL.md) | Authorization | Trusted identity, resource access, tenancy, and browser security |
| [spring-integrations](skills/spring-integrations/SKILL.md) | Delivery semantics | External calls, retries, messages, jobs, and caches |
| [spring-observability](skills/spring-observability/SKILL.md) | Operability | Metrics, traces, logs, probes, and shutdown |
| [java-unit-testing](skills/java-unit-testing/SKILL.md) | Behavior | JUnit Jupiter, Mockito, AssertJ, and deterministic unit tests |
| [spring-testing](skills/spring-testing/SKILL.md) | Mechanism | Spring slices, application tests, Testcontainers, and real infrastructure |

Use `java-implement` when the task is clear and the work is to implement it. Use a specialist when its particular decision needs attention. Each preserves supplied requirements and settled technical choices unless the task explicitly changes them; none requires a design phase. Debugging identifies an uncertain cause; performance work distinguishes code assessment from measured claims. Unit tests isolate ordinary behavior; Spring tests retain the framework or infrastructure mechanism being tested.

Select skills for decisions that need their guidance, not merely because the repository uses Java or Spring. A specialist is not a mandatory implementation stage. Combine skills when distinct parts of the task need them; there is no fixed one-skill limit or required sequence.

A skill supplements the requested task; it does not expand permission to edit or require every topic in its body to be investigated. Review and diagnosis produce findings unless changes are requested. Implementation continues through appropriate checks and fixes for failures it caused, not just a first patch. Verification covers the affected property and required project gates. Unavailable evidence remains explicitly unverified, not a reason to claim success or invent unrelated work.

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

Keep essential standalone guidance in the skill, not in a mandatory shared file or README lookup. The current packaging contract is `SKILL.md` plus `LICENSE`; additional resources need a demonstrated need and corresponding packaging and installation checks, not a speculative directory layout.

For semantic changes, use the affected [behavioral evaluation scenarios](docs/evaluation.md), including natural requests that do not name a skill. Record the model, fixture, instruction revision, and observed result. Compare correctness and scope before tool counts or elapsed time; do not encode a mandatory tool-call sequence. These authoring materials are not installed with individual skills.

[Maintainer instructions](AGENTS.md), [source decisions and review protocol](docs/instruction-design.md),
and [frozen eval fixtures](evals/README.md) support that workflow. The offline
`python scripts/evaluate.py check` validates 30 routing probes and eight fixture
specifications. `prepare` creates comparable workspaces and a `not_run` record;
it does not execute a model or establish better behavior. Model comparisons
remain separate from lightweight distribution CI.

The pack uses the [Agent Skills format](https://agentskills.io/specification). Structural validity and a few useful examples do not establish a universal improvement across models.

## Acknowledgements

Inspired by the focused technical judgments in [Dankosik/go-service-template-rest](https://github.com/Dankosik/go-service-template-rest) and the leading concepts and composability of [mattpocock/skills](https://github.com/mattpocock/skills). The Java/Spring instructions are independently written.

[MIT license](LICENSE).
