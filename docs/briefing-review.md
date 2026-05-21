# Kritische review briefing (v1 voorbereiding)

Datum: 2026-05-21  
Status: **voorbereidingsfase** — geen productie-PCB, geen Gerbers, geen definitieve ESP32-footprint.

## Wat klopt en sterk is

| Onderdeel | Beoordeling |
|---|---|
| Carrier i.p.v. losse module | Correct: USB, programmer en RF blijven op het DevKit. |
| Eén 5V MAIN IN + interne rail-splitsing | Correct voor modulaire installaties en stroombeheer. |
| 74AHCT125 voor LED-data | Correct: 3,3 V ESP32 → 5 V tolerant WS2812/SPI-achtige data. |
| LD2450 via kabel, niet gesoldeerd | Correct voor richting/positionering. |
| Through-hole / soldeervriendelijk | Past bij v1 zelf solderen. |
| Vermijden GPIO19/20, 43/44, 35–37 | In lijn met ESP32-S3-DevKitC-1 v1.1 + N16R8 (octal PSRAM). |
| Geen Gerbers vóór ERC/DRC/metingen | Juiste volgorde. |

## Gaten en correcties t.o.v. oorspronkelijke briefing

### 1. ESP32-footprint en clone-risico (kritiek)

- De briefing noemt DevKitC-1 v1.1 en een Amazon/diymore N16R8-clone, maar **geen enkele fysieke maat is ingevuld**.
- Clone-boards wijken vaak af in: header-afstand, USB-C-uitstek, totale lengte/breedte, antenne-zone, extra silkscreen.
- **Besluit:** footprint en keep-out rond USB blijven **`NIET DEFINITIEF`** tot `hardware/measurements.md` is ingevuld op de werkplaats.

### 2. Hoofdvoeding vs JST-XH (kritiek)

- JST-XH (2,54 mm) is prima voor signalen en lichte lasten; per contact vaak ~3 A bij AWG22 en goede contacten — **niet** comfortabel voor 2× servo-piek + zware LED-last op één dunne XH-lijn.
- **Besluit v1:** primaire **5V MAIN IN** = **JST-VH 2-pin** (of parallel **schroefklem 2-pin** / **XT30** footprint + **grote soldeerpads**). JST-XH 2-pin alleen als **secundaire/optionele** tap met silkscreen *max ~2 A totaal*.

### 3. GPIO3 strapping

- ESP-IDF noemt **GPIO0, GPIO3, GPIO45, GPIO46** als strapping. De oude pinout-notes noemden GPIO3 niet.
- **Besluit:** GPIO3 niet gebruiken voor encoder/knoppen; in pinout-tabel als verboden/strapping.

### 4. 74AHCT125 OE-pinnen

- Alle vier **~OE** (actief laag) moeten naar **GND** — niet alleen “OE-pinnen” in het algemeen.
- SN74AHCT125N: **pin 1, 4, 10, 13** → GND (zie `hardware/schematic-netlist.md`).

### 5. LED-connector pinvolgorde

- Briefing liet twee volgordes toe. **Eén vaste volgorde** is gekozen (GND in het midden) — zie `hardware/connector-list.md`.

### 6. Servo vs UART

- GPIO15/16 zijn logisch voor servo-PWM, maar **niet** combineren met hardware-UART2 op default pins zonder firmware-conflict.
- LD2450 krijgt **UART1 op GPIO10/11** (flexibel in ESP-IDF), niet UART0 (43/44).

### 7. I2C GPIO8/9

- Op DevKitC-1 v1.1 staan GPIO8/9 op de header; veilig voor SH1106 **mits** geen conflict met onboard gebruik (geen conflict op standaard DevKit).
- **Risico clone:** header-labels kunnen afwijken — altijd meten/loggen welk fysiek pin-nummer welk GPIO is.

### 8. 3V3 op carrier

- Carrier levert **geen aparte 3,3 V-regulator** in v1: 3V3 komt van het DevKit (interne LDO vanaf 5V VIN).
- Externe OLED/I2C: **max stroom** beperkt door DevKit-LDO (~typ. 500 mA totaal board — conservatief rekenen met 100–150 mA budget voor OLED+pull-ups).

### 9. Productieclaim

- Briefing vroeg “volledige specificatie”; dat is nu uitgewerkt in losse docs. **Geen** productieclaim tot risico-checklist en metingen groen zijn.

## Amazon-board vs Espressif DevKitC-1 v1.1

| Aspect | Waarschijnlijk gelijk | Onzeker / meten |
|---|---|---|
| Chip | ESP32-S3-WROOM-1 **N16R8** | Module-variant op print lezen |
| Header pitch | 2,54 mm, 2×20 pins | Exacte rij-afstand |
| USB | Dubbele USB-C (USB + UART) | Positie t.o.v. rand carrier |
| Pinout silkscreen | DevKitC-1-achtig | Clone kan andere GPIO-labels tonen |
| Octal PSRAM | GPIO35–37 intern | Bevestigen module marking |
| Onboard LED | GPIO38 RGB (v1.1) | Clone kan afwijken |

**Conclusie:** functioneel zeer waarschijnlijk DevKitC-1 v1.1-compatible, maar **mechanisch alleen na meting**.

## Aanbevolen documentstructuur (uitgevoerd)

| Bestand | Inhoud |
|---|---|
| `docs/technical-specification.md` | Volledige technische specificatie |
| `hardware/pinout-table.md` | Pinout-tabel met risico’s |
| `hardware/connector-list.md` | Connectors + JST footprints |
| `hardware/bom.md` | BOM verplicht/optioneel |
| `hardware/schematic-netlist.md` | Schema/netlist mensentaal |
| `hardware/pcb-layout-plan.md` | Layoutplan tekst |
| `docs/risk-checklist-pre-production.md` | Risico’s vóór productie |
| `docs/kicad-next-steps.md` | Veilige volgende stap KiCad |

## Open punten uit review (doorverwijzing)

Zie einde README en `hardware/measurements.md` voor de meetlijst voor Jeroen.
