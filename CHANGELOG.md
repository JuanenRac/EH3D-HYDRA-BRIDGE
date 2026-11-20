# Changelog

All notable changes to this project are documented here.

## [Unreleased]

- **The title of the 0.0.2 section says what it contains:** the brand, the shared checks and the hardened workflows (the repository has no library, command line or tests of its own yet).

- **The shared validation tools are updated:** the validator also runs the workflow and lessons checks of the suite with their latest rules, including a check to run before every push.
- **The CI validation checks the workflows and the lessons of past CI failures against a baseline:** `tools/workflow_hygiene.py` and `tools/lessons_lint.py` (copies of the shared tools) run in the validation, and only findings that are not in `tools/workflow_hygiene_baseline.json` and `tools/lessons_lint_baseline.json` fail it, so what exists today stays as it is and a new one is caught. `python tools/workflow_hygiene.py --root . --detail` and `python tools/lessons_lint.py --repo .` list the findings.
- **The validation of the CI is the reusable one of the documentation hub:** the job `validate` calls `validate.yml` of EH3D-DOCS (pinned by commit) and the check of the CHANGELOG is a job of its own.
- **A test keeps the register of requirements and the status page in agreement:** the identifiers must run `HBRI-001`, `HBRI-002`, ... with no gap or repetition, each state must be one of planned, prototype, implemented or validated, the count that the status page gives must be the number of rows, and a page that says all are planned fails the day a row is not.
- **A test ties the maturity of the manifest to the presence of code:** while the repository has no `Cargo.toml` and no `src/`, the manifest must say `scaffolding` with no evidence; the day code appears, the test fails until the manifest and the README say how far it is.
- **A test keeps the shape of the tables of the threat model and of the ideas left for later:** every row has the columns of its table and none of them is empty.

## [0.0.2] - The brand, the shared checks and the hardened workflows

- **Brand:** Add the application icon and the logos of the program.
- **Shared checks updated:** the validator also compares the badge and the Version row of the README with the manifest, fails when one of its checks cannot run, and the CHANGELOG step of the workflow reads the base branch from the environment.
- **The workflows are hardened:** every action is pinned by its commit with its version in a comment, and the checkouts keep no credentials.

## [0.0.1] - The base of the repository

- **The base that every repository of the suite has:** the manifest, the README files in eight languages, this changelog, the CI workflow, the issue and pull-request templates, and the shared checks of EH3D-DOCS (the repository check and the drawers of the two README pictures).
- **A planned project, described honestly:** the scope, the requirements (all planned), the relations with other repositories, the threat model, the decisions that apply and the rules for writing code are in `docs/`; there is no code yet.
