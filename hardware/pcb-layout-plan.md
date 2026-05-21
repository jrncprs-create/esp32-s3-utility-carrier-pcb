# PCB-layoutplan (tekst) v0.6

**Board:** **130 × 85 mm**. **Marge:** 5 mm (edge connectors 4 mm).  
**Generator:** `kicad/tools/generate_placeholder.py` · **DOC_REV** `0.6-placeholder`.

KiCad-origin = **linksonder**; hoge Y = bovenkant board. Plaatsing = `PCB_PLACE` / `PCB_SILK` (geen zone-interpretatie).

---

## Visueel beleid v0.6

- Geen zone-kaders / flood op F.Cu.
- Geen GND-pour, geen placeholder-tracks — **airwires** in KiCad.
- Dunne Dwgs.User: ESP-outline, USB/ANT keep-outs, W5500-reserve **30 × 16 mm** (gestippeld).
- Kleine horizontale F.SilkS labels; `verify_no_overlap()` bij genereren.

---

## Componenten (mm, at x,y)

| Ref | x | y | Opmerking |
|---|---:|---:|---|
| H1–H4 | 7 / 123 | 7 / 78 | M3 hoeken |
| J_MAIN | 8 | 14 | |
| C_MAIN | 22 | 14 | |
| F_ESP | **45** | 13 | Tabel **42** + 3 mm i.v.m. J_I2C |
| U2 | 78 | 28 | |
| C_AHCT | 78 | 50 | |
| R_LED1–4 | 94 | 18 / 30 / 42 / 54 | |
| J_LED1–4 | 112 | 18 / 30 / 42 / 54 | |
| J_LD2450 | 8 | 58 | |
| J_OLED_EXT | 22 | 58 | |
| J_I2C | 36 | 58 | |
| J_BTN | 8 | 68 | |
| SW1–3 | 24 / 34 / 44 | 68 | |
| J_ENC | 56 | 68 | |
| SJ_SERVO | 70 | 66 | |
| C_SERVO | 82 | 64 | |
| J_SERVO1/2 | 70 / 84 | 74 | |
| J_W5500 | 94 | 70 | NOT POPULATED |

---

## Silk (mm) — tabel vs gegenereerd

| Label | Tabel | PCB |
|---|---|---|
| POWER IN 5V | 15, 10 | 15, 10 |
| ESP FOOTPRINT TBD | 54, 70 | 42, 64.5 |
| MEASURE BEFORE FAB | 54, 73 | 42, 66.2 |
| LED OUTPUTS / LED1-3 | 100, 12 / 14 | 100, 12 / 14 |
| LED4: AUX | 100, 58 | 107, 60 |
| SENSOR / OLED / UI | 26, 54 | 26, 54 |
| SERVO POWER | 78, 62 | 78, 62 |
| USR-ES1 / W5500 TBD | 103, 66 | 103, 66 |
| RJ45 TO EDGE | 116, 74 | 116, 67 |

---

## Footprints TBD

- `F_ESP` — 2×20 placeholder; meet vóór productie.
- `J_W5500` — USR-ES1 / RJ45 naar rand; header placeholder.
