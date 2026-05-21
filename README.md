# ESP32-S3 Utility Carrier PCB v1

Doel: een soldeerbare carrier-PCB voor een ESP32-S3 DevKit, bedoeld voor kleine interactieve installaties met LED-data, servo's, HLK-LD2450 mmWave sensor, SH1106 OLED-display, knoppen en rotary encoder.

**Documentatieversie:** 0.8 (placeholder)  
**Status:** KiCad placeholder v0.8 · **LED-data routing only** · **nog niet productieklaar** · **geen Gerbers** · ESP32-footprint blijft **NIET DEFINITIEF** (meting later · [diymore B0F3XMYYQY](https://www.amazon.nl/-/en/diymore-DevKitC-1-S3-1-N16R8-development-connectable/dp/B0F3XMYYQY))

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

## Belangrijkste ontwerpkeuzes (v0.8)

- ESP32-S3 DevKit blijft los module met eigen USB-C.
- Eén **5V MAIN IN** — primair **JST-VH** of schroefklem; JST-XH alleen secundair met stroomlimiet.
- Interne rails: `5V_LOGIC`, `5V_LED`, `5V_SERVO` (via **SJ_SERVO** vanaf MAIN).
- LED-data: **4×** ESP32 GPIO → **SN74AHCT125N** (4 kanalen) → 330 Ω → JST-XH 3p — **3 actief** (GPIO18/17/21) + **1 AUX** (GPIO12).
- Alle AHCT **~OE** (pins 1, 4, 10, 13) → GND.
- LD2450: UART op **GPIO10/11**, niet op UART0 (43/44).
- I2C OLED: **GPIO8/9**.
- **Optionele W5500** header **J_W5500** (8p): 3V3, GND, SPI + CS/RST/INT op **GPIO5/13/14/47/4/39** — **NOT POPULATED**, voor toekomstige bedrade Ethernet/Art-Net route.
- Pinout conflict-check: zie [hardware/pinout-table.md](hardware/pinout-table.md).
- Connectorfamilie signaal: **JST-XH 2,54 mm** through-hole waar mogelijk.
- PCB placeholder **130 × 85 mm**, **6-zone layout** (geen zone-vlakken; ESP keep-outs alleen), **4× M3**, airwires only — **geen** definitieve routing.

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
