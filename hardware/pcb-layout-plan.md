# PCB-layoutplan (tekst) v0.9 phase 2

**Board:** **130 × 85 mm**. **Marge:** 5 mm (edge connectors 4 mm).  
**Generator:** `kicad/tools/generate_placeholder.py` · **DOC_REV** `0.9-phase2`.

KiCad-origin = **linksonder**; hoge Y = bovenkant board. Plaatsing = `PCB_PLACE` / `PCB_SILK`.

---

## Visueel beleid

- Geen zone-kaders / GND-pour op F.Cu.
- **Copper (placeholder):** 3× LED-data (0,25 mm), J_MAIN→C_MAIN, C_MAIN→U2 + C_AHCT lokaal; **5V_LED** en GND naar LED-terminals ratsnest; **geen** board-wide GND/5V-bussen.
- Dwgs.User: ESP **25,4×52,5 mm** outline, USB/ANT keep-outs, W5500 **23×29 mm** module + header keep-out.
- Sensor/UI/servo/W5500-signalen: ratsnest.

---

## Componenten (mm, at x,y) — Phase 2 tabel

| Ref | x | y | Opmerking |
|---|---:|---:|---|
| H1–H4 | 7 / 123 | 7 / 78 | M3 hoeken |
| J_MAIN | 10 | 16 | Schroefklem 2p 5,08 mm |
| C_MAIN | 26 | 14 | |
| SJ_SERVO | 10 | 30 | |
| C_SERVO | 22 | 28 | |
| J_SERVO2 | 24 | 38 | |
| J_SERVO1 | 24 | 48 | |
| F_ESP | 45 | 13 | DevKitC-1 **25,4×52,5** — verify clone |
| J_LD2450 | 8 | 58 | |
| J_OLED_EXT | 20 | 58 | |
| J_I2C | 32 | 58 | |
| J_BTN | 70 | 55 | Extern alleen |
| J_ENC | 84 | 62 | Extern alleen |
| U2 | 72 | 24 | SN74AHCT125N |
| C_AHCT | 80 | 46 | |
| R_LED1 / J_LED1 | 86 / 106 | 14 | Schroefklem 3p |
| R_LED2 / J_LED2 | 86 / 106 | 24 | |
| R_LED3 / J_LED3 | 86 / 106 | 34 | |
| J_W5500 | 100 | 64 | SBC-USR-ES1 TBD |

**Niet geplaatst:** SW1–3, ENC1, F_OLED, F_MAIN, J_LED4, R_LED4.

---

## Silk (samenvatting)

| Label | Positie (ca.) |
|---|---|
| POWER IN 5V | 12, 10 |
| LED OUTPUTS | 98, 10 |
| SENSOR / DISPLAY | 20, 52 |
| UI EXTERNAL | 72, 48 |
| DevKitC-1 dims assumed / verify clone | 8, 68–70 |
| W5500 SBC-USR-ES1 TBD | 14, 6–8 |
| RJ45 TO EDGE | 115, 78 |

---

## Footprints TBD

- `F_ESP` — Espressif DevKitC-1 25,4×52,5 mm; meet clone vóór fab.
- `J_W5500` — SBC-USR-ES1 23×29 mm; **header pitch/positie meten**; RJ45 naar boardrand.
