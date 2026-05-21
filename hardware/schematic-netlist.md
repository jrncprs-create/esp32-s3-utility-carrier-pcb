# Schema / netlist (mensentaal) v0.9

Geen KiCad-bestanden in deze fase — dit document is de **logische netlist** voor het schema.

---

## Nets (hoofdlijst)

| Net | Beschrijving |
|---|---|
| `GND` | Common ground |
| `5V_MAIN` | Ingang J_MAIN (+ PAD_PWR) |
| `5V_LOGIC` | ESP32 VIN, AHCT VCC, LD2450 5V, 5V tap J_GPIO |
| `5V_LED` | 5V op J_LED1..3 (in v1 direct verbonden met 5V_MAIN) |
| `5V_SERVO` | Servo 5V via SJ_SERVO |
| `3V3` | Van DevKit header naar OLED/I2C/ENC |
| `LED1_IN` … `LED3_IN` | GPIO → AHCT A inputs |
| `LED1_DATA` … `LED3_DATA` | AHCT Y → R → J_LED DATA |
| `SERVO1_PWM`, `SERVO2_PWM` | GPIO15/16 → J_SERVO |
| `LD_ESP_RX`, `LD_ESP_TX` | GPIO10/11 ↔ J_LD2450 |
| `I2C_SDA`, `I2C_SCL` | GPIO8/9 bus |
| `BTN1` … `BTN3` | GPIO knoppen |
| `ENC_CLK`, `ENC_DT`, `ENC_SW` | Encoder |

---

## Voeding

```text
J_MAIN.1 (5V) ──┬── F_MAIN (optioneel) ──┬── 5V_MAIN
                │                        │
J_MAIN.2 (GND) ─┴── GND ─────────────────┴── (star bij connector)

5V_MAIN ── C_MAIN+ ; C_MAIN- ── GND

5V_MAIN ── 5V_LOGIC ──┬── F_ESP.5V (beide 5V pins op DevKit)
                      ├── U2.14 (VCC)
                      ├── J_LD2450.1
                      ├── J_LEDx.1 (×3)
                      └── J_GPIO.3 (5V tap)

5V_MAIN ── SJ_SERVO.1
SJ_SERVO.2 ── 5V_SERVO ──┬── C_SERVO+
                         ├── J_SERVO1.2
                         └── J_SERVO2.2
C_SERVO- ── GND

F_ESP.GND (alle) ── GND pour
F_ESP.3V3 (alle) ── 3V3 net ── J_OLED.2, J_I2C.2, J_ENC.2, F_OLED.2
```

**Opmerking:** `5V_LED` is in v1 **elektrisch gelijk** aan `5V_MAIN`; in KiCad kan het apart net heten voor DRC/clarity, met **single point** tie bij input.

---

## SN74AHCT125N (U2)

```text
U2.14 (VCC) ── 5V_LOGIC
U2.7  (GND) ── GND
U2.1  (1~OE) ── GND
U2.4  (2~OE) ── GND
U2.10 (4~OE) ── GND
U2.13 (3~OE) ── GND

F_ESP.GPIO18 ── U2.2 (1A)
U2.3 (1Y) ── R_LED1.1 ── R_LED1.2 ── J_LED1.3 (DATA)

F_ESP.GPIO17 ── U2.5 (2A)
U2.6 (2Y) ── R_LED2 ── J_LED2.3

F_ESP.GPIO21 ── U2.9 (3A)
U2.8 (3Y) ── R_LED3 ── J_LED3.3

U2.11 (4A) ── NC
U2.12 (4Y) ── NC (optioneel TP)

C_AHCT tussen U2.14 en U2.7, < 5 mm trace
```

---

## LED connectors

```text
J_LEDn.1 ── 5V_LED (≡ 5V_MAIN)
J_LEDn.2 ── GND
J_LEDn.3 ── LEDn_DATA
```

---

## Servo

```text
J_SERVO1.1 ── GND
J_SERVO1.2 ── 5V_SERVO
J_SERVO1.3 ── SERVO1_PWM ← F_ESP.GPIO15

J_SERVO2.1 ── GND
J_SERVO2.2 ── 5V_SERVO
J_SERVO2.3 ── SERVO2_PWM ← F_ESP.GPIO16
```

---

## LD2450

```text
J_LD2450.1 ── 5V_LOGIC
J_LD2450.2 ── GND
J_LD2450.3 ── LD_ESP_RX ← F_ESP.GPIO10
J_LD2450.4 ── LD_ESP_TX ← F_ESP.GPIO11
```

---

## I2C / OLED

```text
F_ESP.GPIO8 ── I2C_SDA ──┬── F_OLED.3
                         ├── J_OLED_EXT.3
                         └── J_I2C.3

F_ESP.GPIO9 ── I2C_SCL ──┬── F_OLED.4
                         ├── J_OLED_EXT.4
                         └── J_I2C.4

F_OLED.1, J_OLED_EXT.1, J_I2C.1 ── GND
F_OLED.2, J_OLED_EXT.2, J_I2C.2 ── 3V3
```

---

## Knoppen

```text
F_ESP.GPIO1 ── SW1.1 ── SW1.2 ── GND   (of J_BTN.2)
F_ESP.GPIO2 ── SW2 ── GND              (of J_BTN.3)
F_ESP.GPIO42 ── SW3 ── GND             (of J_BTN.4)
J_BTN.1 ── GND
```

Geen externe pull-down; firmware `INPUT_PULLUP`.

---

## Rotary encoder (EC11)

```text
ENC1.A ── ENC_CLK ← GPIO6
ENC1.B ── ENC_DT  ← GPIO7
ENC1.C ── GND
ENC1.D ── 3V3 (common)
ENC1.SW ── ENC_SW ← GPIO40 ── (switch naar GND bij druk)

J_ENC spiegelt ENC1 signalen
```

Optioneel: R_ENC1..3 10k naar 3V3 (DNP).

---

## Extra GPIO header

```text
J_GPIO.4 ── GPIO12
J_GPIO.5 ── GPIO13
J_GPIO.6 ── GPIO14
J_GPIO.7 ── GPIO47
J_GPIO.8 ── NC
```

---

## Netlist-tabel (compact)

| Net | Van | Naar |
|---|---|---|
| GND | J_MAIN.2 | alle GND pins |
| 5V_MAIN | J_MAIN.1 | SJ_SERVO.1, C_MAIN+, 5V_LOGIC |
| 5V_SERVO | SJ_SERVO.2 | J_SERVO*.2, C_SERVO+ |
| 3V3 | F_ESP.3V3 | J_OLED, J_I2C, J_ENC |
| LED1_IN | F_ESP.18 | U2.2 |
| LED1_DATA | U2.3 | R_LED1 → J_LED1.3 |
| SERVO1_PWM | F_ESP.15 | J_SERVO1.3 |
| LD_ESP_RX | J_LD2450.3 | F_ESP.10 |
| I2C_SDA | F_ESP.8 | J_OLED.3, J_I2C.3 |

---

## ERC-aandachtspunten (voor KiCad)

- Geen verbinding naar GPIO19/20/35–38/43/44/0/3/45/46/48.
- `5V_MAIN` en `3V3` nooit kort.
- AHCT inputs alleen van 3,3 V GPIO — OK.
- Polariteit C_MAIN, C_SERVO in schema + footprint.
