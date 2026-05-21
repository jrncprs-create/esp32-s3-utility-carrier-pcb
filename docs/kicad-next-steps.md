# KiCad — status en volgende stappen

## Wat is nu gegenereerd (placeholder v0.1)

| Item | Locatie | Status |
|---|---|---|
| KiCad project | `kicad/esp32-s3-utility-carrier.kicad_pro` | Openbaar in repo |
| Schematic | `kicad/esp32-s3-utility-carrier.kicad_sch` | Eerste bruikbare versie |
| PCB | `kicad/esp32-s3-utility-carrier.kicad_pcb` | 90×65 mm, componenten geplaatst |
| Symbolen | `kicad/libraries/carrier.kicad_sym` | F_ESP, SN74AHCT125N, SJ_SERVO |
| Footprints | `kicad/libraries/carrier.pretty/` | JST placeholders, F_ESP 2×20 |
| Generator | `kicad/tools/generate_placeholder.py` | Opnieuw bouwen na doc-wijziging |

### Schema (logisch aanwezig)

- Voeding: `5V_MAIN`, `5V_LOGIC`, `5V_LED`, `5V_SERVO`, `SJ_SERVO`, `C_MAIN`, `C_SERVO`, GND, `3V3`
- `F_ESP` placeholder (gebruikte GPIO’s uit pinout-tabel)
- `U2` SN74AHCT125N — alle **~OE → GND**
- **4×** LED-keten: GPIO → AHCT → 330Ω → `J_LED1`…`J_LED4` (`LED4` = GPIO12)
- `J_LD2450` (GPIO10/11), `J_OLED_EXT`, `J_I2C`, servo's, knoppen, encoder, `J_GPIO`

### PCB (layout placeholder)

- Board **90 × 65 mm**
- `F_ESP`: 2×20 @ **22,86 mm** rijafstand — silkscreen **NIET DEFINITIEF / NIET BESTELLEN ZONDER METINGEN**
- Connectors aan randen; AHCT bij LED-zijde; power links
- **Dwgs.User:** USB keep-out + antenne keep-out (tekst/vlak)
- GND zone + enkele **5V**-sporen (routing **niet** compleet)

### Bewust **niet** in repo

- Geen Gerbers (`.gbr`, `.gbrjob`)
- Geen fabrication ZIP / job output
- Geen productie-claim

---

## Openen in KiCad

1. Open **`kicad/esp32-s3-utility-carrier.kicad_pro`** (KiCad 7 of 8).
2. Schematic Editor → controleer blokken en netlabels.
3. PCB Editor → **Tools → Update PCB from Schematic** (eerste keer).
4. Run **ERC** (schema) en **DRC** (PCB) — verwacht waarschuwingen (onvolledige routing, ontbrekende standaard footprints op jouw machine).

Sommige footprints verwijzen naar **KiCad standaard bibliotheken** (`Package_DIP`, `Capacitor_THT`, `Resistor_THT`, …). Die moeten lokaal geïnstalleerd zijn (standaard bij KiCad).

---

## Geblokkeerd door fysieke metingen

| Item | Document | Blokkeert |
|---|---|---|
| ESP32 2×20 footprint definitief | `hardware/measurements.md` B3, B5–B10 | Productie-PCB, 1:1 overlay |
| USB keep-out exact | measurements B8, B9 | Behuizing + boardrand |
| Antenne keep-out | measurements B11 | Copper vrije zone |
| Boardgrootte definitief | measurements + behuizing | Randconnectors / M3 |

**Geen PCB bestellen** vóór:

1. `hardware/measurements.md` ingevuld op echt DevKit (diymore).
2. PDF/print **1:1 overlay** DevKit op PCB-tekening in KiCad.
3. `docs/risk-checklist-pre-production.md` sectie A groen.
4. ERC/DRC acceptabel na footprint-update.

---

## Volgende stappen (na metingen)

| # | Actie |
|---|---|
| 1 | Pas `F_ESP_2x20_Placeholder` aan gemeten maten |
| 2 | Update USB/antenne keep-out op `Dwgs.User` |
| 3 | Voltooi routing (5V ≥1 mm, GND pour, korte LED-data) |
| 4 | ERC/DRC groen |
| 5 | Overlay-test met fysiek board |
| 6 | Pas dan pas footprint-status → **DEFINITIEF** in `measurements.md` |
| 7 | **Dan pas** Gerber-export voor prototype-bestelling |

---

## Regenereren

```bash
cd kicad && python3 tools/generate_placeholder.py
```

Daarna opnieuw **Update PCB from Schematic** in KiCad.
