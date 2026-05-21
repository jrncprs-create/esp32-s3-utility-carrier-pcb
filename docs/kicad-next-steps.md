# KiCad — status en volgende stappen

## Wat is nu gegenereerd (placeholder v0.7)

| Item | Locatie | Status |
|---|---|---|
| KiCad project | `kicad/esp32-s3-utility-carrier.kicad_pro` | Openbaar in repo |
| Schematic | `kicad/esp32-s3-utility-carrier.kicad_sch` | Bruikbaar; ERC verwacht |
| PCB | `kicad/esp32-s3-utility-carrier.kicad_pcb` | **130×85 mm**, placement + partial copper |
| Generator | `kicad/tools/generate_placeholder.py` | `PCB_PLACE` + `pcb_routing.py` |

### PCB (v0.7)

- Zones: power, servo (links), ESP (TBD footprint), sensor/display, UI/buttons, LED, W5500 (TBD)
- **Copper:** LED chain, U2 supply, main in, LED/servo power distribution
- **Ratsnest OK:** sensor, OLED/I2C, UI buttons, W5500 (until module measured)
- Geen zone-pour, geen Gerbers in repo

### Bewust **niet** in repo

- Geen Gerbers / fabrication output

---

## Volgende stappen (blokkades voor productie)

1. **Meet** ESP32-S3 DevKit → `hardware/measurements.md` → definitief `F_ESP` footprint
2. **Meet** USR-ES1 / W5500 module → definitief `J_W5500` + RJ45 keep-out
3. Handmatige routing afronden (sensor, UI, Ethernet)
4. ERC/DRC + `docs/risk-checklist-pre-production.md`
5. Pas daarna bestellen
