# EH3D-HYDRA-BRIDGE: scope

Status: **planned**. EH3D-HYDRA-BRIDGE has no code. This page says what it is meant to do, what it will not do, and where it sits. Nothing here has been built or run.

## Purpose

EH3D-HYDRA-BRIDGE is planned as an adapter between EH3D and HYDRA-UMC that exchanges data through versioned contracts.

Adapter between the EH3D and HYDRA-UMC ecosystems. It talks to the EH3D server and is the counterpart of the bridge adapters of HYDRA-UMC.

## What it is planned to do

* First the contract of the bridge: the four links, conformance vectors, separate service identities, tokens and mutual TLS, and the manifest of the adapter for the connector hub of HYDRA-UMC.
* Then the four links, built together: (a) assembly and pick and place: a request with bill of materials, centroids and fiducials from EH3D, with status, results and traceability coming back; (b) vision: fiducial and inspection templates shared between the vision tool and the vision nodes, with inspection results returning to the project; (c) state and telemetry: machine telemetry types of the common repository published to the telemetry of HYDRA-UMC, and the cell state of HYDRA-UMC, emergency stop included, shown read-only in EH3D clients; (d) digital twin: 3D models of board and enclosure sent to the twin and its model catalogue.
* Exchange of artifacts by hash.

## What it will not do

* No shared code and no shared database between the two ecosystems: each keeps its own authority.
* The emergency stop and the motion limits belong to HYDRA-UMC and to the machine; EH3D cannot bypass them and the bridge sends no motion command.
* A.R.M.O.R. is outside the bridge.
* Nothing is implemented before the contract of the bridge is written and accepted.

## Planned shape

An adapter in its own repository that talks to the EH3D server through the public API, the twin of the bridge adapters on the HYDRA-UMC side. It is written in Rust (planned) and ships a manifest the connector hub of HYDRA-UMC can read.

Crates, names and file layout will be decided together with the first code; no crate exists yet.

## Where it sits

It belongs to the EH3D Fabrication Suite, as the counterpart of the bridge adapters of HYDRA-UMC.
See DEPENDENCIES.md for the relations, REQUIREMENTS.md for the requirements and STATUS.md for the honest state.
