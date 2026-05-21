# PCB-layoutplan (tekst) v0.9

**Boardgrootte:** nog vrij — richting **~90 × 65 mm** na ESP-meting (twee USB’s + connectoren aan randen).  
**ESP32-footprint:** **NIET DEFINITIEF** — centrale zone is placeholder.

---

## 1. Zones (functioneel)

```text
+------------------------------------------------------------------+
|  [M3]                                              [M3]          |
|   J_MAIN/VH          J_LED1  J_LED2  J_LED3                      |
|   C_MAIN             (LED rand)                                    |
|   PAD_PWR                                                          |
|                                                                    |
|        +---------------- ESP32 ZONE (TBD) ----------------+       |
|        |  [USB cutout beide kanten]                        |       |
|        |  F_ESP 2x20                                       |       |
|        +---------------------------------------------------+       |
|   U2 AHCT125 + C_AHCT                                              |
|                                                                    |
|   J_SERVO1  J_SERVO2   C_SERVO    SJ_SERVO                         |
|   (servo rand)                                                     |
|                                                                    |
|   J_LD2450                    F_OLED / controls                    |
|   (sensor rand)               SW1-3 ENC1 J_BTN J_ENC J_OLED        |
|                                                                    |
|   J_I2C  J_GPIO   [proto 6x7]                      [M3]    [M3]  |
+------------------------------------------------------------------+
```

---

## 2. Plaatsingregels

| Element | Positie | Reden |
|---|---|---|
| **F_ESP** | Centrum, iets naar **linker** helft | USB naar **boven/onder** rand (meet welke kant op clone) |
| **USB keep-out** | Boardrand + 3 mm vrij | DevKit USB-C stick-out |
| **Antenne keep-out** | Boven DevKit module | Geen copper/gnd onder antenne (Espressif guideline) |
| **J_MAIN** | **Linkerboven** of **linker** rand | Power komt binnen; kort pad naar C_MAIN |
| **C_MAIN** | &lt; 15 mm van J_MAIN | Inrush/filter |
| **U2 + C_AHCT** | &lt; 20 mm van F_ESP GPIO 17–21 kant | Korte data-lijnen |
| **J_LED1–3** | **Rechter** of **boven** rand, gegroepeerd | Kabels naar LED-installaties |
| **J_SERVO + C_SERVO + SJ** | **Onder** of **rechteronder** rand | Dikke 5V_SERVO sporen naar rand |
| **J_LD2450** | **Linker** of **onder** rand, apart van servo power | Sensor kabel weg van servo EMI |
| **Controls** | **Onder** rand (frontpaneel) | OLED, knoppen, encoder bij gebruiker |
| **Proto** | **Rechteronder** hoek | Niet onder ESP32 |
| **Montage M3** | 4 hoeken, min. 5 mm van boardrand | Standaard doos |

---

## 3. Routing

| Net | Breedte (1 oz) | Methode |
|---|---|---|
| 5V_MAIN, 5V_SERVO | **≥ 1,0 mm** (servo **≥ 1,2 mm** indien 2 A) | Prefer bottom + via naar JST |
| GND | Pour + **≥ 1,0 mm** terug naar J_MAIN | Star bij power in |
| LED DATA | 0,3–0,4 mm | Kort AHCT → R → JST |
| I2C | 0,25 mm, parallel kort | Optioneel geen via’s onder ESP |
| UART LD2450 | 0,3 mm | Kruis GND niet parallel lang met 5V_SERVO |
| PWM servo | 0,3 mm | Kort naar header |

**Via’s:** minimaal voor power; signalen liever één laag waar mogelijk.

---

## 4. Silkscreen (verplicht op PCB)

- Projectnaam + **v1** + datum
- **NIET DEFINITIEF FOOTPRINT** in kleine tekst bij ESP (verwijderen na meting)
- Per JST: **pin1 vierkant** + volgorde `5V|GND|DATA` etc. **≥ 1,5 mm tekst**
- LD2450: `LD_TX→PIN3` `LD_RX←PIN4`
- Servo: `GND|5V|PWM`
- Polariteit `+` bij elco’s
- SJ_SERVO: `CLOSED = joint MAIN+SERVO`

---

## 5. Laagstack

| Laag | Gebruik |
|---|---|
| F.Cu | Signaal + componenten TH |
| B.Cu | 5V pours, GND pour, extra power |
| Edge.Cuts | Rechthoek + eventueel afgeronde hoek 2 mm |

---

## 6. Design rule checklist (layout)

- [ ] Min. 0,3 mm clearance copper (fab standaard 6/6 mil)
- [ ] Drill ≥ 0,3 mm voor via, M3 = 3,2 mm
- [ ] Geen traces onder ESP32 antenne
- [ ] Testpunten optioneel op 5V_MAIN, 5V_SERVO, 3V3, GND (1 mm ring)

---

## 7. Volgorde plaatsen in KiCad

1. Board outline + M3 holes (na behuizing/ESP meting)
2. F_ESP placeholder + USB keep-out
3. J_MAIN + C_MAIN + pours
4. U2 + LED chain + J_LED
5. Servo rail + SJ + J_SERVO + C_SERVO
6. Sensor + I2C + controls
7. Proto + silkscreen review

Zie `docs/kicad-next-steps.md`.
