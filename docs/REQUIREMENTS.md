# EH3D-HYDRA-BRIDGE: requirements

This register is the single source of the state of each capability: `STATUS.md` and the README files cite it and never state a state that it does not. A state is one of `planned`, `prototype`, `implemented` and `validated`. `validated` means that a person has run the capability on a real machine and the evidence of the manifest says `bench` or `field`; nothing here is validated, because the repository has no code: it holds the written scope, requirements, dependencies and threat model of a bridge that is not built.

The register has 11 requirements: 3 implemented, 0 prototype, 8 planned and 0 validated. By progress: 3 done, 0 partial, 3 pending and 5 blocked. High coverage is not proof of correctness, so each row says how it is checked: the test that names it, and what it shows.

## How to read the register

* **ID:** `HBRI-NNN`, never reused and never renumbered; a new capability takes the next number.
* **State:** `implemented` is code that is complete and tested on a computer, `prototype` is part of the capability, `planned` is not written.
* **Progress:** `done`, `partial`, `pending` (can be written without hardware) or `blocked` (waits for hardware or for another program of the suite).
* **Evidence:** `simulator` when the test runs against a simulated adapter (none exists yet), `host-test` when it checks a calculation, a reader or a screen-less piece, `none` when nothing is written yet.
* **Test:** the acceptance criterion: `file::name` is the test `name` of `tools/file.py`. The test must exist. For a capability that is not written the cell says `planned:` and the name of the test that will show it; the day that test exists, the row must change.
* **Limits:** what is not done or not proven; a row that is `partial` or `blocked` always says it.

The check is `tools/test_requirements.py`: it reads this table, finds each test and fails when a state, a test or a count does not agree.

## The contract and the links

| ID | Requirement | State | Progress | Evidence | Test | Limits |
|---|---|---|---|---|---|---|
| HBRI-001 | Write the contract of the bridge with conformance vectors that both sides pass. | planned | pending | none | `planned:test_contract::test_both_sides_pass_the_same_vectors` | Not written: the contract comes before any code and has to be accepted by both ecosystems. |
| HBRI-002 | Separate service identities, tokens and mutual TLS: revoked, expired and scope-less credentials are refused. | planned | blocked | none | `planned:test_identity::test_revoked_expired_and_scopeless_credentials_are_refused` | Waits for the contract of the bridge and for the decision on the credentials of a service. |
| HBRI-003 | Manifest of the adapter that the connector hub of HYDRA-UMC accepts. | planned | pending | none | `planned:test_manifest::test_the_hub_accepts_the_manifest` | Not written: it needs the contract and the format of the manifest of the hub. |
| HBRI-004 | Assembly link: a pick-and-place request round-trips with status, results and traceability. | planned | blocked | none | `planned:test_assembly::test_a_request_round_trips_with_status_and_results` | Waits for the contract, the pick-and-place side of both ecosystems and a real machine for the last proof. |
| HBRI-005 | Vision link: a template round-trips unchanged and inspection results return to the project. | planned | blocked | none | `planned:test_vision::test_a_template_round_trips_unchanged` | Waits for the contract and for the vision tool and nodes; the last proof needs a real machine. |
| HBRI-006 | State link: telemetry out, cell state and emergency stop in, read-only. | planned | blocked | none | `planned:test_state::test_no_write_path_exists_for_the_cell_state` | Waits for the contract and for the telemetry types of EH3D-COMMON. |
| HBRI-007 | Twin link: the models of the board and the enclosure reach the twin catalogue with their hashes. | planned | blocked | none | `planned:test_twin::test_published_models_keep_their_hashes` | Waits for the contract and for the models of the design tools. |
| HBRI-008 | Exchange of artifacts by hash. | planned | pending | none | `planned:test_artifacts::test_an_artifact_is_cited_and_checked_by_its_hash` | Not written: it needs the contract and the container rule of EH3D-COMMON. |

## The repository while it has no code

| ID | Requirement | State | Progress | Evidence | Test | Limits |
|---|---|---|---|---|---|---|
| HBRI-009 | The register of requirements agrees with the status page and its identifiers run without a gap. | implemented | done | host-test | `test_docs::test_the_register_of_requirements_agrees_with_the_status_page` | - |
| HBRI-010 | The maturity of the manifest agrees with the presence of code: no code, no evidence. | implemented | done | host-test | `test_docs::test_the_maturity_of_the_manifest_agrees_with_the_presence_of_code` | - |
| HBRI-011 | The tables of the threat model and of the ideas left for later keep their shape. | implemented | done | host-test | `test_docs::test_the_tables_of_the_other_pages_keep_their_shape` | - |
