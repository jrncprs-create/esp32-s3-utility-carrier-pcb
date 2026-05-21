# Changelog

## [Unreleased]

## [0.9.1] — 2026-05-21

### Changed

- Clean visible routing: **LED data only** plus short **J_MAIN→C_MAIN** and **U2↔C_AHCT**;
  remove top-edge 5V bus and **5V_LED** distribution traces (LED power stays ratsnest).

## [0.9.0] — 2026-05-21 (phase 2)

### Changed

- Simplify carrier: **3 LED outputs** (schroefklem 5,08 mm), remove LED4/GPIO12 route.
- **J_MAIN** schroefklem 5,08 mm; remove **F_MAIN** / polyfuse from BOM, schematic, layout.
- Remove **SW1–3**, **F_OLED**, on-board encoder; keep **J_BTN** / **J_ENC** external only.
- **F_ESP** uses Espressif DevKitC-1 **25,4×52,5 mm** (22,86 mm row); verify-clone silk.
- **J_W5500** → SBC-USR-ES1 **23×29 mm** placeholder; header TBD.
- Phase 2 **PCB_PLACE** table; `pcb_routing.py`: 3× LED + limited power (no GND pour).
- U2 channel 4 documented DNP/NC in schematic.

### Removed

- J_LED4, R_LED4, F_MAIN, SW1–3, F_OLED, ENC1 footprint from generator outputs.

## [0.8.0] — 2026-05-21

### Changed

- Revert board-wide power/GND routing (v0.7); **placement unchanged** (v0.7 zones).
- Add **LED-data-only** routing pass: ESP GPIO → U2 → R_LED → J_LED DATA, plus short
  C_AHCT at U2; thin 0.25 mm tracks, 45° bends, routes avoid ESP USB/ANT keep-outs.
- Servo/main/LED power, sensor/UI, W5500 remain ratsnest.

## [0.7.0] — 2026-05-21

### Changed

- PCB layout v0.7: zones split (sensor/display linksonder, UI/buttons rechts van ESP,
  servo links, LED-kolom strak, W5500 compact met 5 mm marge); `PCB_PLACE` / `PCB_SILK` in
  `generate_placeholder.py`.
- First **visible routing pass** (LED data, U2 power, main in, LED 5V/GND, servo power) via
  `kicad/tools/pcb_routing.py` — sensor/UI/W5500 remain ratsnest.
- ESP / W5500 footprints and outlines remain **TBD** (measure before fab).

## [0.6.0] — 2026-05-21

### Changed

- PCB component placement from explicit **mm coordinate table** (`PCB_PLACE` / `PCB_SILK` in
  `kicad/tools/generate_placeholder.py`); `DOC_REV` `0.6-placeholder`.
- Board **130 × 85 mm**, M3 at (7,7), (123,7), (7,78), (123,78); no zone flood boxes; small
  horizontal silk only; `verify_no_overlap()` on generate.
- **F_ESP** anchor **x = 45** (table 42 + 3 mm) for 1 mm clearance vs **J_I2C** @ (36,58) with
  2×20 placeholder width; silk labels nudged where table coords hit parts (see generator comments).
- Thin ESP USB/ANT keep-outs + dashed **30 × 16 mm** W5500 reserve (Dwgs.User); airwires only.

## [0.5.0] — 2026-05-21

### Changed

- PCB layout aligned to **6-zone placement diagram** (130 × 85 mm); `DOC_REV` `0.5-placeholder`.
- Components per zone: power top-left, ESP center-left (USB/ANT keep-outs), LED top-right
  (U2 left, R column, J_LED on right edge ~x120), sensor/UI bottom-left, servo mid-left,
  W5500 bottom-right (spacious).
- No large zone flood boxes; generator verifies no segments, pours, or `(justify center)`.
- Airwires only — no copper tracks or GND pour.

## [0.4.0] — 2026-05-21

### Changed

- PCB layout **visual reset** (v0.4): board **110 × 75 mm**, cleaner placement, no zone flood
  boxes, no GND pour, no placeholder tracks — airwires only.
- Subtle ESP keep-outs (thin USB/ANT rectangles); small horizontal silk labels per zone.
- M3 holes ~5 mm from corners; connectors grouped by function with more spacing.

## [0.3.0] — 2026-05-21

### Changed

- PCB placeholder **visual layout cleanup** (reproducible via `generate_placeholder.py`):
  - Board **100 × 70 mm**, **5 mm** keep-in margin, **4× M3** mounting holes.
  - Zones: power (top-left), ESP (center-left), LED+AHCT (right), sensor/OLED/UI (lower-left),
    servo (left), W5500 (bottom, optional).
  - No overlapping silk; connectors inset from edges; **no signal copper** (airwires + GND pour only).
  - Dwgs.User zone boxes + USB/antenna keep-outs aligned to ESP.
- Fix W5500 schematic text string (unterminated quote).

## [0.2.0] — 2026-05-21

### Added

- Optional **J_W5500** 8-pin header (W5500 Ethernet module route): 3V3, GND, SPI_SCK/MOSI/MISO, ETH_CS/RST/INT.
- Footprint `carrier:JST_W5500_1x08_Placeholder` with silk **W5500 OPTIONAL / NOT POPULATED**.
- Canonical `PINOUT` dict in `generate_placeholder.py` + `verify_pinout()` (no forbidden GPIO overlap).

### Changed

- **4 LED outputs:** GPIO18/17/21 + **GPIO12 (AUX)** via AHCT channel 4 → J_LED4.
- W5500 SPI/control GPIOs: **5, 13, 14, 47, 4, 39** (replaces v0.1 `J_GPIO` header).
- Updated pinout-table, schematic-netlist, technical-spec §3, connector-list, KiCad schematic/PCB placeholders.

### Notes

- **Not production-ready** — no Gerbers, incomplete routing, ESP32 footprint **NIET DEFINITIEF**.
- W5500 module not mounted in BOM v0.2; header only for future wired module.

## [0.1.0] — 2026-05-21

### Added

- KiCad placeholder project in `kicad/` (schematic + PCB 90×65 mm, carrier symbol/footprint libraries).
- Generator script `kicad/tools/generate_placeholder.py` to regenerate placeholder files.
- KiCad syntax fixes (sheet_instances order, schematic text, PCB justify center).

## [0.9.1] — 2026-05-21

- Full technical specification, pinout, BOM, connector list, schematic netlist (markdown).
- Assumed Espressif DevKitC-1 dimensions for diymore B0F3XMYYQY (measure later).

## [0.9.0] — 2026-05-21

- Initial PCB project briefing and documentation structure.
