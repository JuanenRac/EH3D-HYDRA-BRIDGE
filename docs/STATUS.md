# EH3D-HYDRA-BRIDGE: status

## Current state

EH3D-HYDRA-BRIDGE is planned. It holds the base that every repository of the suite carries (manifest, README files in eight languages, changelog, CI, shared checks), the written scope, requirements, dependencies, threat model and decisions, and tests that keep the register of requirements and the status page in step. There is no library, no command line and no adapter, nothing has been run on a machine, and no capability of the bridge is implemented.

## Capabilities

The official state of each capability is in `REQUIREMENTS.md`. The register has 11 requirements: 3 implemented, 0 prototype, 8 planned and 0 validated. By progress: 3 done, 0 partial, 3 pending and 5 blocked. This page never states a state that `REQUIREMENTS.md` does not.

## Open questions

* Exact capabilities of the HYDRA-UMC SDK and bridges to reuse; to be reviewed when the contract is written.

## What it needs from other repositories

* EH3D-COMMON: the telemetry types.
* EH3D-SERVER: its API.
* HYDRA-UMC: the contracts and the connector hub that read the manifest.

## Known technical debt and omitted tests

* 80 tests, all of the base: the 3 of the repository, the 3 that keep the documents in step, the 9 that keep this register true and the 65 of the shared tools (the lessons linter, the workflow check, the CHANGELOG check and the banner check). The code of the bridge will get its own as it is written.
* Every capability of the bridge is `planned`, so no test of the bridge exists; each row names the test that will show it.
