# EH3D-HYDRA-BRIDGE: scope

Status: **planned**. EH3D-HYDRA-BRIDGE has no code. This page says what it is meant to do, what it will not do and where it sits; nothing here has been built or run. This page says what it is for, what it will not do and where it sits among the other programs of the suite.

## Purpose

The adapter between the EH3D and HYDRA-UMC ecosystems: it talks to the EH3D server through its public API and is the counterpart of the bridge adapters of HYDRA-UMC. First the contract of the bridge is written, with conformance vectors; then the four links (assembly and pick and place, vision, state and telemetry, digital twin) are built together.

## What it does

* Nothing yet: the repository holds the base that every repository of the suite carries, the written scope, requirements, dependencies, threat model and decisions, and checks that keep those documents honest.
* Planned first: the contract of the bridge with conformance vectors, separate service identities, tokens and mutual TLS, and the manifest of the adapter for the connector hub of HYDRA-UMC.
* Planned then, built together: the assembly link (a pick-and-place request with the bill of materials, centroids and fiducials from EH3D, with status, results and traceability coming back), the vision link (templates shared and inspection results returning), the state link (the machine telemetry types published to HYDRA-UMC, and the cell state, emergency stop included, shown read-only in EH3D) and the twin link (the models of the board and the enclosure sent to the twin and its catalogue).
* Planned: the exchange of artifacts by hash.

## What it will not do

* No shared code and no shared database between the two ecosystems: each keeps its own authority.
* The emergency stop and the motion limits belong to HYDRA-UMC and to the machine; EH3D cannot bypass them and the bridge sends no motion command.
* A.R.M.O.R. is outside the bridge.
* Nothing is implemented before the contract of the bridge is written and accepted.
* Nothing here has been built or run: the evidence of every capability is `none`.

## Where it sits

* **It reads:** nothing yet; the adapter will read the API of the EH3D server and the contracts of HYDRA-UMC.
* **It writes:** nothing yet; the adapter will write only through the contracts, and never a motion command.
* **It is read by:** nothing yet: the connector hub of HYDRA-UMC will read the manifest of the adapter once it exists.
* **It depends on:** EH3D-COMMON (telemetry types and the project container), EH3D-SERVER (its API) and the contracts of HYDRA-UMC, none of them accepted for this use yet (see `DEPENDENCIES.md`).

## What it never decides

The emergency stop, the motion limits and the cell state belong to HYDRA-UMC and to the machine. The bridge shows the state read-only and sends no motion command, so no request that crosses it can start motion, bypass a limit or release an emergency stop.

The requirements of the program, with the state of each and the test that shows it, are in `REQUIREMENTS.md`; the state in a paragraph is in `STATUS.md`.
