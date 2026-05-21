# PCB-layoutplan (tekst) v0.5

**Board:** **130 × 85 mm** (tijdelijk). **Marge:** 5 mm (edge connectors 4 mm).  
**Generator:** `kicad/tools/generate_placeholder.py` · **DOC_REV** `0.5-placeholder`.

KiCad-origin = **linksonder**; hoge Y = bovenkant board.

---

## Visueel beleid v0.5

- Geen zone-kaders over het hele board (diagram = gids alleen).
- Geen GND-pour, geen placeholder-tracks — **airwires** in KiCad.
- Dunne Dwgs.User-lijnen alleen bij ESP (outline + USB/ANT keep-outs).
- Kleine horizontale F.SilkS labels per zone; geen `(justify center)` op PCB.

---

## Zones (plaatsing)

| Zone | Locatie | Refs (at x,y mm) |
|---|---|---|
| Power | linksboven | J_MAIN @(10,68), C_MAIN @(20,68) |
| ESP | midden-links | F_ESP @(16,20) — USB laag Y, ANT hoog Y |
| LED | rechtsboven | U2 @(62,58), R_LED* kolom @(84,*), J_LED* @(115,*) |
| Sensor/UI | linksonder | J_LD2450, J_OLED_EXT, J_I2C, J_BTN, F_OLED, SW1–3, J_ENC |
| Servo | midden-links / onder-mid | SJ_SERVO, C_SERVO, J_SERVO1/2 @(42–55, 30–38) |
| Ethernet | rechtsonder (ruim) | J_W5500 @(95,12) — NOT POPULATED |
| M3 | hoeken | H1–H4 @ ±8.2 mm van hoek |

---

## Silk (kort)

`POWER IN 5V` · `LED OUTPUTS` / `LED1-3: 5 TUBES` / `LED4: AUX` ·  
`SENSOR / OLED / UI` · `SERVO POWER` · `W5500 OPTIONAL` / `ETHERNET / ART-NET` ·  
`ESP FOOTPRINT TBD` / `MEASURE BEFORE FAB` · `FOOTPRINT TBD` (W5500)
