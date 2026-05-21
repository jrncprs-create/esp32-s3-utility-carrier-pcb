# Current status — ESP32-S3 Utility Carrier PCB

**Date:** 2026-05-21  
**Status:** v0.9 hardware decisions captured · FASE 1 reviewplan afgerond · wacht op akkoord/uitvoering FASE 2  
**Production status:** geen productie · geen Gerbers · geen fabrication-output

## Repository

- Repo: `jrncprs-create/esp32-s3-utility-carrier-pcb`
- Project: ESP32-S3 Utility Carrier PCB
- Current KiCad state before v0.9 refactor: v0.8 placeholder, board 130 × 85 mm, placement v0.7, LED-data-only routing.
- Existing schema/BOM/docs may still reflect older assumptions: 4 LED outputs, JST LED connectors, optional F_MAIN/polyfuse, SW1–3, F_OLED, Amazon/diymore clone as reference.

## New v0.9 hardware decisions

### ESP32

- Use **official Espressif ESP32-S3-DevKitC-1 dimensions** as reference:
  - Board envelope reference: approx. 25.4 × 52.5 mm
  - Header row spacing reference: 22.86 mm
- ESP footprint remains **TBD** until the real clone board is physically verified.
- Label/warning: `official dimensions assumed, verify clone before fab`.

### 5V power

- One external 5V supply enters the PCB.
- `J_MAIN` = sturdy 2-pole screw terminal, 5.08 mm pitch:
  - 5V
  - GND
- **No F_MAIN/polyfuse on PCB.** Protection/fusing is external at the power supply.

### LED outputs

- Maximum **3 LED outputs**.
- Remove LED4/AUX as active LED output.
- `J_LED1`, `J_LED2`, `J_LED3` = 3-pole screw terminals / pluggable terminal blocks, 5.08 mm pitch:
  1. 5V
  2. GND
  3. DATA
- `R_LED1`, `R_LED2`, `R_LED3` remain 330 Ω.
- `U2` remains SN74AHCT125N / 74AHCT125.
- AHCT channel 4: unused / DNP / NC, documented cleanly.
- GPIO12 becomes free/reserve; no LED4/AUX label.

### UI / buttons / encoder

- Remove onboard `SW1`, `SW2`, `SW3`.
- Remove onboard encoder footprint if present.
- Keep only external connectors:
  - `J_BTN` for external buttons
  - `J_ENC` for external encoder

### OLED / sensor

- OLED only externally via `J_OLED_EXT`.
- Remove `F_OLED` direct-mount footprint.
- Keep `J_I2C` as extra I2C connector.
- LD2450 radar only externally via `J_LD2450`.

### W5500 / Ethernet

- Use **SBC-USR-ES1** datasheet as reference.
- Module dimensions: **23 × 29 × 24 mm**.
- Module uses **3V3**.
- RJ45 should face the board edge.
- Header/footprint remains **TBD** until pin header / underside / physical module is checked.
- Label/warning: `SBC-USR-ES1 W5500 TBD / measure header before fab`.

## FASE 1 reviewplan outcome

FASE 1 completed without changing files. It proposed:

- Updated parts in/out list.
- Updated pinout with no LED4; GPIO12 free/reserve.
- Updated placement table, including:
  - `J_MAIN` around (10,16)
  - 3 LED screw terminals on the right
  - no onboard SW buttons
  - W5500 zone around (100,64)
- ASCII topdown layout.
- Routing intent:
  - 3× LED-data routing
  - limited/local power visibility
  - no board-wide messy GND/power bus
- Open risks:
  - clone vs official Espressif dimensions
  - exact screw-terminal footprints
  - SBC-USR-ES1 header/pinout/underside still TBD

## Approved instruction for next Cursor phase

FASE 2 may proceed with these confirmations:

- Question 10 is **B**: no F_MAIN/polyfuse on PCB.
- Remove F_MAIN from active BOM/schema/layout/generator.
- Remove LED4/GPIO12 from LED outputs. GPIO12 may remain free/reserve only.
- LED connectors become 3× 3-pole screw terminals, 5.08 mm pitch.
- Remove SW1/SW2/SW3 and F_OLED from layout/schema/BOM.
- Keep `J_BTN`, `J_ENC`, `J_OLED_EXT`, `J_I2C`, `J_LD2450` as external connectors.
- Use SBC-USR-ES1 dimensions: 23 × 29 × 24 mm, 3V3, header TBD, RJ45 to board edge.
- Use official Espressif ESP32-S3-DevKitC-1 dimensions as reference, but still verify before fab.

## FASE 2 requested scope

After approval, Cursor should:

- Update schema/generator/BOM/pinout/layout/docs.
- Keep or remake neat routing for 3 LED-data outputs.
- Keep power routing limited and clear.
- Avoid autorouter chaos.
- Create no Gerbers and no fabrication-output.
- Update README, CHANGELOG, and `docs/kicad-next-steps.md`.

Target commit message:

```text
refactor(pcb): simplify carrier around external controls and 3 LED outputs
```

## Current hard blockers before fabrication

- Physical measurement of the ESP32-S3 DevKit clone against official DevKitC-1 reference.
- Physical/datasheet confirmation of SBC-USR-ES1 header positions and pinout.
- Exact screw-terminal footprint choice.
- 1:1 print/overlay check in KiCad.
- ERC/DRC pass after final footprint corrections.

## Absolute rules

- No Gerbers.
- No fabrication ZIP/output.
- No production claim.
- ESP footprint remains TBD until verified.
- W5500 footprint remains TBD until verified.
- PCB remains prototype/placeholder until physical measurements and overlay checks are complete.
