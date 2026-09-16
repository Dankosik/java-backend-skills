# Instruction design and review

Maintainer material, not a prerequisite for using any installed skill.
Baseline audited: `75219fb069695cc15d34f3beded4cef5f0cdcc03`.
Sources accessed on 2026-09-16. These are independently written adaptations,
not imported source code or a claim that every upstream rule suits Java.

## Source decisions

| Primary source | Retain here | Deliberately do not import |
| --- | --- | --- |
| [Matt Pocock: code review](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md) | Separate requirements from engineering judgments; pin the comparison; supply evidence and scope to independent reviewers when available. | Mandatory setup, external issue tracker, automatic every-task subagents, or treating stylistic smells as defects. |
| [Matt Pocock: TDD](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md) | Observable behavior, independent expectations, and a regression that distinguishes the defect. | Mandatory user approval of every testing boundary, a universal TDD sequence, or banning storage observations needed to prove Spring effects. |
| [Matt Pocock: codebase design](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/SKILL.md) | Judge an abstraction by the complexity it removes from callers, including invariants and effects. Already present in `java-design`; retain it. | A new compulsory glossary or an absolute ban on interfaces with one implementation. |
| [Alibaba: Open Code Review](https://github.com/alibaba/open-code-review/blob/main/skills/open-code-review/SKILL.md) | Relevant business context, explicit review scope, located findings, preserved output, and visible partial failures. | Installing OCR, an external provider, global npm packages, or upgrade prompts as requirements of the Java pack. |
| [OpenAI: Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills) | Frozen prompts and fixtures, traces and artifacts, routing negatives, and checkable outcomes. Implemented in the eval catalog and preparation tool. | Treating JSON validity, tool exit status, or an agent's success sentence as proof of task correctness. |
| [OpenAI: Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) | Narrow activation, selective reading, bounded scope, and completion through relevant checks. Existing concise skills already implement much of this. | Longer capability catalogs, forced itineraries, blanket file reading, or one model's results generalized to all models. |
| [Anthropic: The new rules of context engineering](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) | Repository-specific context and judgment; references outside the always-loaded path; test/rubric interfaces. | Removing meaningful safety or domain constraints merely to reduce instruction length. |

The requested [X article](https://x.com/trq212/article/2080710971228918066)
could not be read directly. The official Anthropic article by Thariq Shihipar
was used as an accessible primary source on context engineering. Its equivalence
to the inaccessible X article was not verified; no claim here relies on having
read the X text. The supplied Alibaba URL had a trailing Cyrillic character;
the table links the verified repository without it.

Inspected Git blob identities for the source skills, so future upstream edits
are distinguishable from this audit:

```text
mattpocock/skills code-review: e28d7acbf7b3bb4d7817b7eb5d9c105af03f6ec4
mattpocock/skills tdd: 8fc086710806190ee7c4baa32089cb877a75736a
mattpocock/skills codebase-design: 3f63c8146dd2604b419c929e9876b90c30d410e9
alibaba/open-code-review skill: e0d8dacfedf608624fcb861089b8fe02beb7601c
```

Technical cross-checks: [Gradle incremental builds](https://docs.gradle.org/current/userguide/incremental_build.html)
explain why clean/refresh is not a default validation strategy;
[Flyway versioned migrations](https://documentation.red-gate.com/fd/versioned-migrations-273973333.html)
explain why already-applied versioned migrations are not rewritten.
Rolling-deployment and effect/acknowledgement cases test the stated project
contracts rather than prescribing a particular framework version.

## Coverage and editing decisions

All 15 skill bodies and descriptions were inspected. A retained skill is not a
missed rewrite: preserve working distinctions unless a concrete case exposes a gap.

| Skills | Decision and evidence target |
| --- | --- |
| `java-implement` | Clarify unrelated-work preservation and untrusted task data; E01/E19/E20. |
| `java-build` | Prefer incremental, affected-module checks without waiving required gates; E12 in the behavioral protocol and R07. |
| `java-unit-testing` | Distinguish a real behavioral regression failure from setup/compilation failure; E02 and the executable boundary oracle. |
| `spring-data` | Clarify applied migrations and old/new schema compatibility; E06/E17. |
| `spring-integrations` | Make concurrent deduplication and effect/record gaps explicit; E14/E18. |
| `java-idiomatic`, `java-design` | Retain caller-visible contracts and earned abstractions; E03/E10 and routing probes. |
| `java-debugging`, `java-performance`, `java-concurrency` | Retain falsifiable diagnosis, measured-claim limits, and task lifetime; E08/E11/E15. |
| `spring-boot`, `spring-web`, `spring-security`, `spring-observability`, `spring-testing` | Retain smallest real mechanism, denied effects, and local operational scope; E04/E07/E13/E16. |

E01-E16 are defined in [the behavioral protocol](evaluation.md); the
[frozen catalog](../evals/README.md) supplies eight concrete or reduced fixtures
and E17-E20 extensions. Routing probes are hypotheses to test, not observed
selection results. No release or model-quality claim follows from this table.

## Review a candidate, not an aspiration

Pin base and candidate commits and enumerate changed, staged, unstaged, and
untracked files that are actually in scope. For a branch, state whether the diff
is against its merge-base or a literal commit; do not silently change the target.
Read surrounding callers or packaging rules only when they resolve a finding.

For a substantial instruction change, separate these questions:

- **Requirements:** does the change preserve task scope, standalone installation,
  settled decisions, and the intended outcome? What requested behavior is absent?
- **Technical and instruction judgment:** is each new rule accurate, conditional,
  discriminating, and free of counterexamples that defeat its purpose?
- **Evidence and distribution:** do fixtures distinguish failures, are claims
  supported by captured artifacts, and can the unchanged packaging still ship?

When subagent tools exist and independent review is useful, give each reviewer
one question, exact refs/files, the applicable contract, and a read-only remit.
Do not prefill the desired verdict or another reviewer's findings. The coordinator
owns edits and integration; reviewers do not race to modify the same files.
When tools are absent, use labeled sequential passes and disclose that they are
not independent agent reviews. Do not invent reviewer identities or votes.

A finding needs a file and location, a concrete triggering condition, the
violated contract, and the consequence. Separate supported defects, uncertain
hypotheses, and optional preferences. Test the strongest plausible counterexample
before accepting a finding. Deduplicate the same causal issue while retaining
which review dimension it affects. Reject generic cleanup that does not solve
the reported problem. Preserve complete results; list skipped files or failed
reviewers instead of calling a partial review complete.

After a fix, recheck its affected contract and regression case. Additional rounds
need a remaining supported issue, a newly changed boundary, or a concrete
uncertainty. Stop when those are resolved within the declared scope, or report
the remaining blocker/budget limit. Never manufacture new rules to keep a review
loop alive, and never label reviewer agreement as proof of universal perfection.
