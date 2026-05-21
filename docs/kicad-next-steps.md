# KiCad — status en volgende stappen

## Wat is nu gegenereerd (placeholder v0.8)

| Item | Locatie | Status |
|---|---|---|
| KiCad project | `kicad/esp32-s3-utility-carrier.kicad_pro` | Openbaar in repo |
| Schematic | `kicad/esp32-s3-utility-carrier.kicad_sch` | Bruikbaar; ERC verwacht |
| PCB | `kicad/esp32-s3-utility-carrier.kicad_pcb` | **130×85 mm**, placement + partial copper |
| Generator | `kicad/tools/generate_placeholder.py` | `PCB_PLACE` + `pcb_routing.py` |

### PCB (v0.8)

- Zones: power, servo (links), ESP (TBD footprint), sensor/display, UI/buttons, LED, W5500 (TBD)
- **Copper:** LED **data** chain + short C_AHCT at U2 only (0.25 mm, local paths)
- **Ratsnest OK:** power, servo, LED 5V/GND, sensor, UI, W5500
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
