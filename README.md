# ESP32-S3 Utility Carrier PCB v1

Doel: een soldeerbare carrier-PCB voor een ESP32-S3 DevKit, bedoeld voor kleine interactieve installaties met LED-data, servo's, HLK-LD2450 mmWave sensor, SH1106 OLED-display, knoppen en rotary encoder.

**Documentatieversie:** 0.9 phase 2  
**Status:** KiCad placeholder v0.9.1 · **3× LED data + minimal local power** · **nog niet productieklaar** · **geen Gerbers** · DevKitC-1 **25,4×52,5 mm assumed** — [verify clone](hardware/measurements.md)

## Documentatie-index

| Document | Inhoud |
|---|---|
| [docs/technical-specification.md](docs/technical-specification.md) | Volledige technische specificatie |
| [docs/briefing-review.md](docs/briefing-review.md) | Kritische review oorspronkelijke briefing |
| [hardware/pinout-table.md](hardware/pinout-table.md) | Pinout + risico’s |
| [hardware/connector-list.md](hardware/connector-list.md) | Connectors, JST footprints, pinvolgorde |
| [hardware/bom.md](hardware/bom.md) | BOM verplicht/optioneel |
| [hardware/schematic-netlist.md](hardware/schematic-netlist.md) | Schema/netlist mensentaal |
| [hardware/pcb-layout-plan.md](hardware/pcb-layout-plan.md) | PCB-layoutplan |
| [docs/risk-checklist-pre-production.md](docs/risk-checklist-pre-production.md) | Risico’s vóór productie |
| [docs/kicad-next-steps.md](docs/kicad-next-steps.md) | KiCad status en volgende stappen |
| [kicad/](kicad/) | **KiCad placeholder** — open `esp32-s3-utility-carrier.kicad_pro` |
| [CHANGELOG.md](CHANGELOG.md) | Wijzigingslog |
| [hardware/measurements.md](hardware/measurements.md) | **Werkplaats meetformulier** |
| [docs/pcb-briefing.md](docs/pcb-briefing.md) | Oorspronkelijke briefing (archief) |

## Belangrijkste ontwerpkeuzes (v0.9 phase 2)

- ESP32-S3 DevKit blijft los module met eigen USB-C.
- **J_MAIN:** schroefklem 2p **5,08 mm** (5V/GND) — **geen** polyfuse/F_MAIN.
- LED: **3×** GPIO18/17/21 → **SN74AHCT125N** (ch4 DNP) → 330 Ω → schroefklem 3p; **GPIO12 vrij**.
- UI: alleen **J_BTN** + **J_ENC** (geen SW1–3, geen on-board encoder).
- OLED: **J_OLED_EXT** alleen (geen F_OLED).
- W5500: **SBC-USR-ES1** placeholder 23×29 mm, header TBD, RJ45 naar rand.
- Placeholder routing: LED-data + J_MAIN→C_MAIN + korte 5V (geen board-wide GND-bussen).
- LD2450: UART op **GPIO10/11**, niet op UART0 (43/44).
- I2C OLED: **GPIO8/9**.
- **Optionele W5500** header **J_W5500** (8p): 3V3, GND, SPI + CS/RST/INT op **GPIO5/13/14/47/4/39** — **NOT POPULATED**, voor toekomstige bedrade Ethernet/Art-Net route.
- Pinout conflict-check: zie [hardware/pinout-table.md](hardware/pinout-table.md).
- Signaalconnectors: **JST-XH**; hoofdvoeding + LED: **schroefklem 5,08 mm**.
- PCB **130 × 85 mm**, placement phase 2; sensor/servo/UI/W5500 nog ratsnest.

## Werkwijze

1. ~~Specificatie, pinout, BOM, risico-check~~ (gedaan in v0.9 docs)
2. **Werkplaatsmetingen** ter verificatie in `hardware/measurements.md` (werkwaarden staan al als Espressif-ref)
3. ~~KiCad placeholder~~ — open [`kicad/esp32-s3-utility-carrier.kicad_pro`](kicad/esp32-s3-utility-carrier.kicad_pro) (bekijken/ERC; **niet bestellen**)
4. Geen Gerbers vóór ERC/DRC + risico-checklist + metingen
5. v1 kale PCB, zelf solderen
6. PCBA pas v2/v3

## Rode vlaggen

- ESP32-footprint **voorlopig = Espressif DevKitC-1** (diymore B0F3XMYYQY); **definitief na meting**.
- Amazon/diymore: uitgaan van zelfde maat als Espressif tot meting bevestigt/tegenspreekt.
- GPIO35/36/37 verboden bij N16R8 (octal PSRAM).
- GPIO19/20 (USB), GPIO43/44 (UART0), GPIO0/3/45/46 (strapping), GPIO38/48 (onboard LED).
- Hoofdvoeding: controleer stroom vóór alleen JST-XH op MAIN.

## Target board

- [diymore ESP32-S3-DevKitC-1 N16R8 — Amazon B0F3XMYYQY](https://www.amazon.nl/-/en/diymore-DevKitC-1-S3-1-N16R8-development-connectable/dp/B0F3XMYYQY) (footprint-werkwaarden = Espressif)
- Referentie: [Espressif ESP32-S3-DevKitC-1 v1.1](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32s3/esp32-s3-devkitc-1/user_guide_v1.1.html)
