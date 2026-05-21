# KiCad — status en volgende stappen

## Wat is nu gegenereerd (placeholder v0.6)

| Item | Locatie | Status |
|---|---|---|
| KiCad project | `kicad/esp32-s3-utility-carrier.kicad_pro` | Openbaar in repo |
| Schematic | `kicad/esp32-s3-utility-carrier.kicad_sch` | Bruikbaar; ERC verwacht |
| PCB | `kicad/esp32-s3-utility-carrier.kicad_pcb` | **130×85 mm**, explicit coords |
| Generator | `kicad/tools/generate_placeholder.py` | `PCB_PLACE` / `PCB_SILK` + overlap check |

### PCB (v0.6 — coordinate table)

- Board **130 × 85 mm**; componenten op vaste mm-coördinaten (zie `hardware/pcb-layout-plan.md`)
- Geen zone-flood; kleine F.SilkS labels; dunne ESP/W5500 Dwgs.User guides
- **Geen** signaal-copper — airwires (ratsnest) only
- **4× M3** in hoeken; `F_ESP` / W5500 footprint **TBD**

### Bewust **niet** in repo

- Geen Gerbers / fabrication output

---

## Openen in KiCad

1. Open **`kicad/esp32-s3-utility-carrier.kicad_pro`**
2. PCB Editor → controleer plaatsing en 3D Viewer
3. **Update PCB from Schematic** indien refs gewijzigd
4. DRC: unrouted nets verwacht

---

## Volgende stappen (echte v1)

1. Metingen DevKit → `hardware/measurements.md`
2. Definitief ESP-footprint
3. Handmatige routing
4. ERC/DRC + risico-checklist
5. Pas daarna bestellen
