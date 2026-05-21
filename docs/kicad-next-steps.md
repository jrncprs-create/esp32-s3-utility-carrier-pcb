# KiCad — status en volgende stappen

## Wat is nu gegenereerd (placeholder v0.5)

| Item | Locatie | Status |
|---|---|---|
| KiCad project | `kicad/esp32-s3-utility-carrier.kicad_pro` | Openbaar in repo |
| Schematic | `kicad/esp32-s3-utility-carrier.kicad_sch` | Bruikbaar; ERC verwacht |
| PCB | `kicad/esp32-s3-utility-carrier.kicad_pcb` | **130×85 mm**, zone-diagram layout |
| Generator | `kicad/tools/generate_placeholder.py` | `python3 tools/generate_placeholder.py` |

### PCB (v0.5 — zone diagram)

- Board **130 × 85 mm**, **6 zones** als dunne dashed Dwgs.User boxes
- Componenten per zone (power linksboven, ESP midden, LED rechts, sensor linksonder, servo midden-links, W5500 rechtsonder)
- **Geen** signaal-copper — airwires (ratsnest) only
- **4× M3** in hoeken; `F_ESP` footprint **TBD**

### Bewust **niet** in repo

- Geen Gerbers / fabrication output

---

## Openen in KiCad

1. Open **`kicad/esp32-s3-utility-carrier.kicad_pro`**
2. PCB Editor → controleer zone-layout en 3D Viewer
3. **Update PCB from Schematic** indien refs gewijzigd
4. DRC: unrouted nets verwacht

---

## Volgende stappen (echte v1)

1. Metingen DevKit → `hardware/measurements.md`
2. Definitief ESP-footprint
3. Handmatige routing
4. ERC/DRC + risico-checklist
5. Pas daarna bestellen
