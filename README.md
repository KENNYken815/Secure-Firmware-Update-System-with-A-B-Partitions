# Secure Firmware Update System with A/B Partitions

A host-runnable embedded firmware-update reference framework demonstrating dual application slots, image-version policy, pending-slot boot, application confirmation, and automatic rollback.

> **Project status:** Completed reference implementation. The repository demonstrates the A/B boot-policy architecture in portable C. It is not a production secure-boot implementation and does not claim hardware validation, signed-image key management, or secure-element integration.

## What is implemented
- Two firmware slots: A and B
- Active and pending slot state
- Inactive-slot installation policy
- Minimum-version / anti-downgrade policy model
- Bounded boot-attempt counter
- Application confirmation step
- Automatic fallback to the previously active slot
- Portable C boot-manager core
- Python policy tests
- Architecture, update-flow, rollback, and test documentation

## Repository structure
```text
.
├── firmware/
│   └── secure_update.c      # Core A/B boot and update policy
├── tests/
│   └── test_update.py       # Host-side policy verification
├── docs/
│   ├── ARCHITECTURE.md      # System design
│   ├── UPDATE_FLOW.md       # Update sequence
│   ├── ROLLBACK_POLICY.md   # Failure/recovery behavior
│   └── TEST_PLAN.md         # Verification scenarios
├── Makefile
├── README.md
└── .gitignore
```

## Update sequence
```text
 New image
    |
    v
Validate version/metadata
    |
    v
Write INACTIVE slot
    |
    v
Mark slot PENDING
    |
    v
Boot pending image
    |
    +---- confirmation ----> ACTIVE
    |
    +---- repeated failure -> ROLLBACK
```

The previous confirmed slot remains available while the new image is being evaluated.

## Reference policy
| Parameter | Value |
|---|---:|
| Slots | 2 |
| Minimum supported version | 1 |
| Maximum boot attempts | 3 |
| Update target | Inactive slot |
| Rollback | Enabled |

These are demonstration values, not vendor or OEM requirements.

## Build
```bash
make
./secure_update_demo
```

## Test
```bash
python3 -m unittest discover -s tests -v
```

## Important design decisions
**Why A/B?** A failed update does not destroy the last confirmed application image.

**Why pending state?** A newly installed image should not become permanently active until it proves that it can boot successfully.

**Why confirmation?** Startup health can be checked before promoting the candidate image.

**Why a boot-attempt limit?** Repeated failures should return control to a known-good image instead of looping forever.

**Why minimum version?** The boot policy can reject software versions older than the last accepted security baseline.

## Security scope
The project models the control flow needed around secure firmware updates. A production implementation should additionally use cryptographic signatures, protected public keys, authenticated metadata, secure rollback counters, hardware-backed roots of trust where appropriate, atomic NVM records, watchdog supervision, power-loss recovery, secure provisioning, and security testing.

The included reference uses a lightweight policy model rather than claiming a complete cryptographic secure-boot chain.

## Hardware integration path
The portable core can be connected to a real MCU by replacing the reference state operations with flash/NVM drivers and a verified-image implementation, then integrating the boot manager with the MCU reset/startup path and watchdog.

## Portfolio value
This project demonstrates embedded boot architecture, A/B partitioning, firmware-update state machines, rollback handling, version policy, fail-safe recovery, and test-driven reasoning around update failures.

## Safety / limitation
This repository is an educational/reference implementation, not certified bootloader firmware. Do not deploy it on a production ECU or safety-critical device without a complete security architecture, target-specific implementation, code review, and hardware validation.
