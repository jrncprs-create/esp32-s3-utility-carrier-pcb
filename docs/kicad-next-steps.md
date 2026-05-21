# KiCad — status en volgende stappen

## Wat is nu gegenereerd (placeholder v0.9 phase 2)

| Item | Locatie | Status |
|---|---|---|
| KiCad project | `kicad/esp32-s3-utility-carrier.kicad_pro` | Openbaar in repo |
| Schematic | `kicad/esp32-s3-utility-carrier.kicad_sch` | Phase 2 — ERC verwacht |
| PCB | `kicad/esp32-s3-utility-carrier.kicad_pcb` | **130×85 mm**, phase 2 placement |
| Generator | `kicad/tools/generate_placeholder.py` | `DOC_REV` `0.9-phase2` |
| Routing | `kicad/tools/pcb_routing.py` | 3× LED + limited power |

### PCB copper (placeholder)

- **Gerouteerd:** LED1–3 data; J_MAIN→C_MAIN; 5V_LOGIC→U2; 5V_LED→J_LED1–3; C_AHCT @ U2
- **Ratsnest:** servo, sensor, UI, W5500 signalen
- Geen zone-pour, geen Gerbers

### Verwijderd uit outputs (verify bij generate)

`F_MAIN`, `SW1`–`SW3`, `F_OLED`, `J_LED4`, `R_LED4`, `LED4_*` nets

---

## Volgende stappen

1. **Meet** DevKit clone → `hardware/measurements.md` → definitief `F_ESP`
2. **Meet** SBC-USR-ES1 header → definitief `J_W5500` + RJ45 keep-out
3. Handmatige routing (servo, LD2450, I2C, J_BTN, J_ENC, W5500)
4. ERC/DRC + risico-checklist
5. Pas daarna bestellen — **geen Gerbers** tot goedgekeurd

Regenerate: `python3 kicad/tools/generate_placeholder.py`
