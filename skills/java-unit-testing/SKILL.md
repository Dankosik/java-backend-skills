---
name: java-unit-testing
description: "Behavior. Use when writing or improving JUnit Jupiter tests, Mockito interactions, assertions, or deterministic fixtures for ordinary Java components."
---

# Java Unit Testing

**Behavior first.** Find the observable promise this change could break. Choose inputs that distinguish a correct implementation from a plausible wrong one; calculate expected results independently of the production algorithm. Honor supplied requirements and settled technical choices; resolve only what the task leaves open.

Read the existing tests and build before choosing APIs. Preserve the project's Java and test-library baseline. Construct an ordinary component directly; an annotation on its class does not make every test a Spring test.

Ask what each mock isolates. Use real values and collections; mock a collaborator when its responses or effects define the scenario. Verify a call when the call is the requirement. Otherwise assert the result. Keep stubs local and strict; an unused stub is a reason to reconsider setup before adding leniency.

Make the failure explain the rule. Parameterize inputs sharing one rule; separate different behaviors. Control time and randomness when relevant, bound asynchronous completion, and propagate worker failures. A test that returns before its assertion runs proves nothing.

Challenge the test: could the original defect survive it, or could a harmless refactor break it? Strengthen the former; remove implementation choreography from the latter. Keep integration claims outside the reach of mocked dependencies.

Run the relevant existing test task, confirm discovery, and state the result and any untested boundary.
