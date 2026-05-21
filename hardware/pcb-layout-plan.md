# PCB-layoutplan (tekst) v0.5

**Board:** **130 × 85 mm** (tijdelijk). **Marge:** 5 mm; edge-connectors 4 mm.  
**Zone-diagram:** zie gebruikersdiagram / `Dwgs.User` dashed boxes in KiCad.  
**Generator:** `kicad/tools/generate_placeholder.py`.

---

## Zes zones (mm, origin onder-links)

| Zone | Box (x1,y1)-(x2,y2) | Componenten |
|---|---|---|
| 1 POWER | (10,58)-(48,82) | J_MAIN, C_MAIN |
| 2 ESP32-S3 | (50,12)-(78,68) | F_ESP; USB onder, ANT boven |
| 3 LED | (82,48)-(126,82) | U2, R_LED1-4, J_LED1-4 @ x≈120 |
| 4 SENSOR/UI | (10,8)-(52,38) | LD2450, OLED, I2C, SW*, ENC |
| 5 SERVO | (10,40)-(48,56) | SJ_SERVO, C_SERVO, J_SERVO1/2 |
| 6 W5500 | (78,8)-(126,32) | J_W5500 optional |

**M3:** hoeken @ (8.2, 8.2), (121.8, 8.2), (8.2, 76.8), (121.8, 76.8).

---

## Visueel beleid

- Dunne **dashed** zone-kaders op Dwgs.User (geen gevulde vlakken).
- Geen copper tracks, geen GND-pour — **airwires** in KiCad.
- Kleine F.SilkS labels per functie; zone-namen in Dwgs.User.

---

## Nog niet productieklaar

- ESP-footprint TBD (`hardware/measurements.md`).
- Geen Gerbers / geen routing.
