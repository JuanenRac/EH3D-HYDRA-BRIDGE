# EH3D-HYDRA-BRIDGE: requirements

This register is the single source of the state of each capability. Status values: planned, prototype, implemented, validated. Every requirement is `planned` today: nothing is implemented or verified. High test coverage is not proof of geometric or electrical correctness, so each requirement says how it will be checked and what result is expected.

| Requirement | Description | Status | How it will be checked | Expected result | Known limits |
|---|---|---|---|---|---|
| HBRI-001 | Write the contract of the bridge with conformance vectors. | planned | review plus automatic vectors | Both sides pass the same vectors. | Not started: no limits known yet. |
| HBRI-002 | Separate service identities, tokens and mutual TLS. | planned | automatic: negative tests | Revoked, expired and scope-less credentials are refused. | Not started: no limits known yet. |
| HBRI-003 | Manifest of the adapter for the connector hub of HYDRA-UMC. | planned | automatic: manifest validation | The hub accepts the manifest. | Not started: no limits known yet. |
| HBRI-004 | Assembly link: pick-and-place request and traceability back. | planned | automatic plus real machine | A request round-trips with status and results. | Not started: no limits known yet. |
| HBRI-005 | Vision link: shared templates and results back. | planned | automatic plus real machine | A template round-trips unchanged. | Not started: no limits known yet. |
| HBRI-006 | State link: telemetry out, cell state and emergency stop in, read-only. | planned | automatic | No write path exists for the cell state. | Not started: no limits known yet. |
| HBRI-007 | Twin link: board and enclosure models to the twin catalogue. | planned | automatic | Published models keep their hashes. | Not started: no limits known yet. |

Rules: a claim of correctness names the corpus, the tolerance and the tool version it holds for. A phase is complete when the measured rate does not drop, every failure is classified and fixed or documented, and the measured figure is reported.
