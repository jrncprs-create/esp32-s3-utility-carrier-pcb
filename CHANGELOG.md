# Changelog

## [Unreleased]

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
