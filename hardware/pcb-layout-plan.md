# PCB-layoutplan (tekst) v0.3

**Boardgrootte:** **90 × 65 mm** (placeholder).  
**ESP32-footprint:** **VOORLOPIG** — zie `hardware/measurements.md`.  
**KiCad:** posities worden gegenereerd door `kicad/tools/generate_placeholder.py` (`BOARD_W/H`, placement list).

---

## 1. Zones (v0.3)

```text
+------------------------------------------------------------------+
| POWER          |     USB/antenna keep-out (Dwgs.User)            |
| J_MAIN C_*     |     +-------- ESP (F_ESP) --------+  LED1-3    |
| SJ_SERVO       |     |  NIET DEFINITIEF            |  5-TUBE    |
|                |     +-----------------------------+  J_LED*    |
| SERVO          |              U2 AHCT125 ---------->  (right)  |
| J_SERVO*       |                                                 |
|                |  SENSOR/OLED/I2C cluster                         |
| J_LD J_OLED    |  J_BTN J_ENC (UI)                                |
| J_I2C F_OLED   |                                                 |
| W5500 (8p)     |  OPTIONAL / NOT POPULATED                        |
+------------------------------------------------------------------+
```

---

## 2. Plaatsingregels (v0.3)

| Element | Positie | Reden |
|---|---|---|
| **J_MAIN … C_SERVO** | Linksboven (y≈4 mm) | Korte 5V/GND stubs |
| **F_ESP** | Centrum (28, 10) | Binnen outline; USB keep-out boven |
| **U2 + C_AHCT** | Tussen ESP en LED-kolom | Korte AHCT → LED data |
| **J_LED1–3** | Rechterrand, verticaal | 5-buizen outputs |
| **J_LED4** | Rechts onder LED1–3 | AUX / reserve |
| **J_LD2450, J_OLED, J_I2C, F_OLED** | Linkeronder cluster | Sensor + display bedrading |
| **SW*, J_BTN, J_ENC** | Onder midden | Frontpaneel UI |
| **J_W5500** | Onder links (8, 57) | 17,5 mm breedte; niet buiten board |
| **Routing** | Geen lange diagonalen | Placeholder: airwires OK |

---

## 3. Silk (placeholder)

| Tekst | Zone |
|---|---|
| `LED1-3: 5-TUBE OUTPUT` | Rechtsboven |
| `LED4: AUX / RESERVE` | Rechts midden |
| `W5500 OPTIONAL / NOT POPULATED` | Boven J_W5500 |
| `ESP FOOTPRINT NIET DEFINITIEF` | Onder ESP-zone |

---

## 4. Nog niet in v0.3

- Definitieve ESP-meting en footprint
- Volledige copper routing
- M3 montagegaten (footprints in layoutplan v0.9, nog niet in KiCad placeholder)
- Proto-gaten vak
