# EH3D-HYDRA-BRIDGE: decisions that apply here

Decisions of the suite that shape this project, written as project documentation. A decision marked proposed is not final: this project must not rely on it silently, and where a number or a limit depends on it, the code will keep it as one named constant.

## Independent repositories related by contracts

State: **accepted**.

Every repository of the suite is independent. Repositories relate through versioned contracts and build next to each other as sibling folders. Programs never depend on each other: they exchange work through project files or through the server. The design tool does not depend at build time on the satellites that depend on it; it reaches them through their command line or through server tasks. A lower layer never depends on a higher one.

## Stable diagnostic codes

State: **proposed**.

Failures that a reader or a check cannot hide become diagnostics with a stable code of the form `PHOENIX-<AREA>-<NNN>` (the registry is kept in the board tool). A code is never reused or renumbered, its message may be translated but the code and field names are not, and a repository never keeps a private list: it asks for numbers in the registry in the same change that uses them, together with a test.

## Nothing here moves a machine

State: **accepted**.

Importing, converting, simulating or validating a design never starts motion, even as a side effect. Programs may at most prepare a job in the ready state through the server when a task says so; authorising, starting, confirming and cancelling are actions of a person. Computing tasks run without access to machine connectors.

## Separate ecosystems, joined by versioned contracts

State: **accepted**.

EH3D and HYDRA-UMC stay separate ecosystems: they talk through versioned contracts with conformance vectors, share no code and no database, and each keeps its authority. The emergency stop and the motion limits belong to HYDRA-UMC and to the machine. The EH3D side of the bridge lives in its own repository, the twin of the bridge adapters on the HYDRA-UMC side.
