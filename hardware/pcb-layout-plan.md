# PCB-layoutplan (tekst) v0.3

**Board:** **100 × 70 mm** (placeholder).  
**Marges:** 5 mm keep-in; M3-centers op 9 mm van hoek.  
**Generator:** `kicad/tools/generate_placeholder.py` — `BOARD_W`, `BOARD_H`, placement list.

---

## Zones

```text
+------------------------------------------------------------------------+
| [M3]  POWER (J_MAIN, C_MAIN)                              [M3]         |
|       W5500 zone (optional)                                            |
|       +---------------- ESP ----------------+   U2    J_LED1           |
|       | USB keep-out (bottom)              |   AHCT   J_LED2           |
|       | ANTENNA keep-out (top)             |         J_LED3           |
|       +------------------------------------+         J_LED4           |
|  SERVO   SENSOR/OLED/I2C                         (5-tube / AUX labels)  |
|  J_SERVO*  J_LD J_OLED J_I2C                                          |
|            SW* J_BTN J_ENC                              [M3]    [M3]   |
+------------------------------------------------------------------------+
```

---

## Plaatsing (samenvatting)

| Zone | Componenten | Positie (mm, pad-1) |
|---|---|---|
| Power | J_MAIN, C_MAIN | linksboven ~(10,10) |
| Servo pwr | SJ_SERVO, C_SERVO | ~(10,34) |
| ESP | F_ESP | (22, 14) |
| LED | U2, R_LED*, J_LED1–4 | rechts; J @ x=86, y=16/28/40/52 |
| Servo | J_SERVO1/2 | (10,38), (18,38) |
| Sensor/UI | J_LD, J_OLED, J_I2C, F_OLED, SW*, J_BTN, J_ENC | linksonder / onder midden |
| Ethernet | J_W5500 | (22, 8) — NOT POPULATED |
| Mount | H1–H4 M3 | hoeken @(9,9), (91,9), (9,61), (91,61) |

---

## Routing-beleid v0.3

- **Geen** placeholder signaal-tracks.
- **GND zone** met inset (~8 mm van rand).
- Overige nets: **airwires** in KiCad.

---

## Silk (kort, horizontaal)

- `POWER IN 5V` / `LED PWR EXTERNAL / PER TUBE`
- `ESP FOOTPRINT NIET DEFINITIEF` / `MEASURE BEFORE FAB`
- `LED1-3: 5 TUBE OUTPUTS` / `LED4: AUX / RESERVE`
- `SENSOR / OLED / UI` / `SERVO 5V VIA SJ_SERVO`
- `W5500 OPTIONAL / NOT POPULATED` / `ETHERNET FOR RESOLUME / ART-NET`
