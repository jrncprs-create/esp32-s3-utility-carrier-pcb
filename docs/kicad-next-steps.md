# KiCad — status en volgende stappen

## Wat is nu gegenereerd (placeholder v0.3)

| Item | Locatie | Status |
|---|---|---|
| KiCad project | `kicad/esp32-s3-utility-carrier.kicad_pro` | Openbaar in repo |
| Schematic | `kicad/esp32-s3-utility-carrier.kicad_sch` | Bruikbaar; ERC verwacht |
| PCB | `kicad/esp32-s3-utility-carrier.kicad_pcb` | **100×70 mm**, zone-layout, visueel opgeschoond |
| Symbolen | `kicad/libraries/carrier.kicad_sym` | F_ESP, SN74AHCT125N, SJ_SERVO |
| Footprints | `kicad/libraries/carrier.pretty/` | JST, F_ESP, M3, W5500 |
| Generator | `kicad/tools/generate_placeholder.py` | `python3 tools/generate_placeholder.py` |

### Schema (logisch aanwezig)

- Voeding, `F_ESP`, `U2` AHCT (4 LED-kanalen), servo's, LD2450, I2C/OLED, knoppen, encoder
- `J_W5500` optional (NOT POPULATED)

### PCB (v0.3 placeholder layout)

- Board **100 × 70 mm**, **5 mm** randmarge, **4× M3** (9 mm van hoek)
- **Geen** signaal-routing — alleen GND zone + airwires
- Zones met Dwgs.User kaders + leesbare F.SilkS labels (geen overlap)
- `F_ESP`: 2×20 @ 22,86 mm — **NIET DEFINITIEF / MEASURE BEFORE FAB**
- Connectors binnen outline; W5500 onderaan met ruimte

### Bewust **niet** in repo

- Geen Gerbers (`.gbr`, `.gbrjob`)
- Geen fabrication ZIP
- Geen productie-claim

---

## Openen in KiCad

1. Open **`kicad/esp32-s3-utility-carrier.kicad_pro`** (KiCad 7 of 8).
2. Schematic Editor → ERC (warnings OK op placeholder).
3. PCB Editor → bekijk zones / 3D Viewer; DRC (unrouted nets verwacht).
4. **Niet** Plot Gerbers tot metingen + definitief footprint.

---

## Volgende stappen (echte v1)

1. `hardware/measurements.md` invullen op fysieke DevKit.
2. ESP-footprint definitief maken.
3. Handmatig of assisted routing in KiCad.
4. ERC/DRC clean + `docs/risk-checklist-pre-production.md`.
5. Pas daarna Gerbers / bestellen.
