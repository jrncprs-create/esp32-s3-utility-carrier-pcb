# ESP32-S3 Utility Carrier PCB v1

Doel: een soldeerbare carrier-PCB voor een ESP32-S3 DevKit, bedoeld voor kleine interactieve installaties met LED-data, servo's, HLK-LD2450 mmWave sensor, SH1106 OLED-display, knoppen en rotary encoder.

**Documentatieversie:** 0.9 (voorbereiding)  
**Status:** specificatie compleet · **geen KiCad/Gerber-productie** · ESP32-footprint **NIET DEFINITIEF**

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
| [docs/kicad-next-steps.md](docs/kicad-next-steps.md) | Veilige volgende stap KiCad |
| [hardware/measurements.md](hardware/measurements.md) | **Werkplaats meetformulier** |
| [docs/pcb-briefing.md](docs/pcb-briefing.md) | Oorspronkelijke briefing (archief) |

## Belangrijkste ontwerpkeuzes (v0.9)

- ESP32-S3 DevKit blijft los module met eigen USB-C.
- Eén **5V MAIN IN** — primair **JST-VH** of schroefklem; JST-XH alleen secundair met stroomlimiet.
- Interne rails: `5V_LOGIC`, `5V_LED`, `5V_SERVO` (via **SJ_SERVO** vanaf MAIN).
- LED-data: ESP32 GPIO → **SN74AHCT125N** → 330 Ω → JST-XH 3p (`5V | GND | DATA`).
- Alle AHCT **~OE** (pins 1, 4, 10, 13) → GND.
- LD2450: UART op **GPIO10/11**, niet op UART0 (43/44).
- I2C OLED: **GPIO8/9**.
- Connectorfamilie signaal: **JST-XH 2,54 mm** through-hole waar mogelijk.

## Werkwijze

1. ~~Specificatie, pinout, BOM, risico-check~~ (gedaan in v0.9 docs)
2. **Werkplaatsmetingen** invullen in `hardware/measurements.md`
3. KiCad schema + placeholder PCB (`docs/kicad-next-steps.md`)
4. Geen Gerbers vóór ERC/DRC + risico-checklist + metingen
5. v1 kale PCB, zelf solderen
6. PCBA pas v2/v3

## Rode vlaggen

- ESP32-footprint **NIET DEFINITIEF** zonder fysieke metingen.
- Amazon/diymore clone ≈ DevKitC-1 v1.1, maar **niet blind vertrouwen**.
- GPIO35/36/37 verboden bij N16R8 (octal PSRAM).
- GPIO19/20 (USB), GPIO43/44 (UART0), GPIO0/3/45/46 (strapping), GPIO38/48 (onboard LED).
- Hoofdvoeding: controleer stroom vóór alleen JST-XH op MAIN.

## Target board

- [Amazon B0F3XMYYQY](https://www.amazon.nl/dp/B0F3XMYYQY) — vermoedelijk diymore ESP32-S3-DevKitC-1 N16R8
- Referentie: [Espressif ESP32-S3-DevKitC-1 v1.1](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32s3/esp32-s3-devkitc-1/user_guide_v1.1.html)
