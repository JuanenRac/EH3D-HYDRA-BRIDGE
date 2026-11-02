# EH3D-HYDRA-BRIDGE: dependencies

One row per relation with another repository. The kind is conceptual, compile-time or run-time. The state of a contract is: not written, drafted, accepted, frozen or published. A repository existing does not mean that its contract is ready: this project does not implement or consume a contract that is not accepted.

| From | To | Kind | Contract | Contract state | Minimum version | Tested version | Compatibility test | Change owner | What it blocks | Migration |
|---|---|---|---|---|---|---|---|---|---|---|
| EH3D-HYDRA-BRIDGE | EH3D-COMMON | compile | machine telemetry types, project container | drafted | not set | not set | to be written with the first code | the owner of the contract | state link, artifact exchange | to be defined |
| EH3D-HYDRA-BRIDGE | EH3D-SERVER | runtime | server API (the adapter talks to it) | drafted | not set | not set | to be written with the first code | the owner of the contract | all links | to be defined |
| EH3D-HYDRA-BRIDGE | HYDRA-UMC-SDK | conceptual | contracts and thin clients of HYDRA-UMC | published by its owner | not set | not set | to be written with the first code | the owner of the contract | the contract | to be defined |
| EH3D-HYDRA-BRIDGE | HYDRA-UMC-CONNECTOR-HUB | conceptual | adapter registry by manifest | published by its owner | not set | not set | to be written with the first code | the owner of the contract | the adapter manifest | to be defined |
| EH3D-HYDRA-BRIDGE | HYDRA-UMC-BRIDGE-OPENPNP | conceptual | pick-and-place side of the assembly link | published by its owner | not set | not set | to be written with the first code | the owner of the contract | the assembly link | to be defined |
| EH3D-HYDRA-BRIDGE | HYDRA-UMC-TWIN | conceptual | digital twin and model catalogue | published by its owner | not set | not set | to be written with the first code | the owner of the contract | the twin link | to be defined |
| EH3D-HYDRA-BRIDGE | EH3D-PNP-MANAGER | conceptual | pick-and-place side on the EH3D side | not written | not set | not set | to be written with the first code | the owner of the contract | the assembly link | to be defined |
| EH3D-HYDRA-BRIDGE | EH3D-VISION-STUDIO | conceptual | vision templates on the EH3D side | not written | not set | not set | to be written with the first code | the owner of the contract | the vision link | to be defined |

Rules: repositories are built next to each other as sibling folders and each declares in its manifest the versions of the others that it needs, once those exist. A lower layer never depends on a higher one. The manifest field for build dependencies stays empty until code exists.
