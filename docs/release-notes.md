# Java Backend Skills 1.0.1

Release candidate; this document does not assert that the version is published.

This patch refines skill selection, task scope, and completion within the existing
15-skill contract. Review and diagnosis no longer imply editing. Implementation
continues through appropriate verification and fixes for introduced failures,
while specialist checks stay tied to the property changed by the task.

Technical evidence requirements remain intact: weaker mocked boundaries do not
prove database or security mechanisms, and unavailable execution is not a pass.
Skill names, paths, independent installation, and environment requirements are
unchanged. Native manifests derive from the canonical package metadata.

Authoring-only behavioral scenarios cover natural selection, task modes, scoped
verification, and completion. Structural CI and installation checks do not run
these scenarios; no cross-model quality or speedup claim follows from packaging.
Record focused behavioral results before publishing semantic instruction changes.

The README installation commands remain pinned to published v1.0.0. Update those
pins and the reviewed author marketplace entry when 1.0.1 is actually published;
do not move existing tags or silently update consumers from main.

OpenAI and Anthropic public-directory listings have their own submission and
review process; this candidate does not claim either listing has been approved.
