# PCB-layoutplan (tekst) v0.4

**Board:** **110 × 75 mm**. **Marge:** 5 mm (edge connectors 4 mm).  
**Generator:** `kicad/tools/generate_placeholder.py`.

---

## Visueel beleid v0.4

- Geen zone-kaders over het hele board.
- Geen GND-pour, geen placeholder-tracks — **airwires** in KiCad.
- Dunne Dwgs.User-lijnen alleen bij ESP (outline + kleine USB/ANT).
- Kleine horizontale F.SilkS labels per zone.

---

## Zones (plaatsing)

| Zone | Locatie | Refs |
|---|---|---|
| Power | linksboven | J_MAIN, C_MAIN |
| ESP | midden-links | F_ESP @(34,16) |
| LED | rechts | U2, R_LED*, J_LED* @ x=100 |
| Sensor/UI | linksonder | J_LD, J_OLED, J_I2C, SW*, J_ENC |
| Servo | midden-onder | J_SERVO*, SJ_SERVO, C_SERVO |
| Ethernet | onder midden | J_W5500 @(42,10) |
| M3 | hoeken | H1–H4 @ ±8.2 mm |

---

## Silk (kort)

`POWER IN 5V` · `LED OUTPUTS` / `LED1-3: 5 TUBES` / `LED4: AUX` ·  
`SENSOR / OLED / UI` · `SERVO POWER` · `W5500 OPTIONAL` / `ETHERNET / ART-NET` ·  
`ESP FOOTPRINT TBD` / `MEASURE BEFORE FAB`
