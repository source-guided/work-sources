# Verify the outcome

Use the brief and decisions as the expected behavior. Existing code and tests are observations, not authority to shrink the requirement. Scale the checks to the change and time budget.

## Plan and execute relevant checks

Derive coverage from the supplied outcomes and material decisions before relying on the implementation's existing tests. For each applicable requirement, identify a concrete starting state, user action, observable result, and evidence type. Mark omitted or unexecutable checks as unverified with a reason. Source reading, component presence, test totals, and an agent's completion message are not substitutes for that coverage.

For each mandatory outcome, choose the smallest meaningful check. Consider:
- Normal task completion with representative input.
- Invalid/empty input, important boundaries, and recovery.
- Changed inputs versus old results; unsaved versus confirmed state.
- Duplicate requests, conflicting edits, partial failure where relevant.
- Restart persistence, export schema, run/deployment artifacts if required.

For computed output, check invariants independently of the generator. Reusing the same calculation as the test oracle can repeat the same mistake. Use small hand-checkable fixtures or a separate validation path. Do not add tests that only mirror text or implementation details.

For material format, range, precision, or normalization decisions, include contract-valid inputs near an implementation boundary as well as contract-invalid inputs a library may accept. Derive expected behavior from the adopted profile, not from another call to the same parser. Compare available supported environments when a dependency default can change the outcome; do not claim all-version coverage from one runtime. Separate a confirmed contract mismatch from an unspecified dialect or resource envelope that needs clarification, and state practical impact without inventing operational scale.

Run the project's required static and targeted dynamic checks. Use available browser/app tools for affected user flows. Inspect meaningful visual states as well as accessible controls. A screenshot proves appearance at a moment, not persistence or concurrency.

## Evidence and completion

Record input/action, expected outcome, observed result, evidence location, and revision. Distinguish **passed**, **failed**, **not run**, and **blocked**. Mark evidence invalidated when relevant code changes after the run. Do not broaden or repeat passing checks without new changes or unresolved concerns.

Before completion, reconcile material contrary observations with the claims being made. Keep a short disposition in the existing owner record: what was observed, which requirement or chosen benefit it calls into question, and what happened next. When it demonstrates a gap within the authorized scope, revise the work and re-observe the affected result. When retaining the behavior, support that decision with its applicable contract, task tradeoff and evidence; the original implementation rationale alone does not resolve the observation. When a question remains unresolved, keep it open and narrow the completion claim. Do not quietly omit a noticed problem because other checks passed or a different problem was fixed. This is follow-through on material findings, not a mandatory report for every harmless observation or a new approval gate.

Do not turn a documentation checklist into a passing test report. Tool failures are not product passes. If runtime checks cannot run, identify the minimum missing capability and finish independent static work. No screenshots or measurements may be invented.

For a reusable-workflow evaluation, resolve `independent-review` through the [current project reference](../../../references/verification/index.json). That source owns the independent review method and its relationship to the execution harness.

Use [evidence and handoff — reference](../../../references/verification/index.json) for a substantial final handoff. Keep final reporting compact for small edits. Report residual limitations without claiming external submission, deployment, or acceptance that was not observed and authorized.

## Review the decision as well as its implementation

Separate checks grounded in the user's outcome or adopted contract from checks grounded in the model's implementation choice. The latter may be valuable regression checks but are not independent acceptance evidence. Before accepting a test, consider whether another reasonable solution would fail it and whether a visibly poor outcome could still pass it. Resolve that mismatch through the task's actual requirements, not by elevating the current implementation to authority.

For discretionary choices, observe the relevant before/during/after experience and a counterexample that could expose a poor judgment. The reviewer chooses those situations from the task. Do not impose a universal component, notification, focus destination, document layout or transition geometry.

For a material claim, connect the adopted criterion and its scope, the chosen approach, the expected user benefit or risk, and the observation that can challenge it. A design intention explains why something was chosen; it does not establish that the benefit occurred. When a criterion concerns a relationship across time, objects or environments, evidence must cover that relationship, not just one endpoint. Leave unsupported claims unverified even when functional checks pass. Use the selected domain owner to decide what observations and tradeoffs are meaningful; do not copy its detailed criteria here.

Audit source selection and reads using the connected reference client's `usage` / `entry` procedure. Compare those accesses with actual decisions and observations to assess application. Classify a failure at the appropriate stage: absent guidance, inaccessible or missed reference, misunderstood applicability, conflicting choice, or evidence insufficient for the claim. A later read may inform a new decision but cannot establish how an earlier decision was made.
