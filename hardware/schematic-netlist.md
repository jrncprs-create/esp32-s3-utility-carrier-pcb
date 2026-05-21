# Schema / netlist (mensentaal) v0.9 phase 2

Logische netlist voor het placeholder-schema. KiCad-bestanden in `kicad/` worden gegenereerd via `generate_placeholder.py`.

---

## Nets (hoofdlijst)

| Net | Beschrijving |
|---|---|
| `GND` | Common ground (lokaal gerouteerd; geen board-wide pour) |
| `5V_MAIN` | Ingang J_MAIN (schroefklem) |
| `5V_LOGIC` | ESP32 VIN, AHCT VCC, LD2450 5V |
| `5V_LED` | 5V op J_LED1..3 |
| `5V_SERVO` | Servo 5V via SJ_SERVO |
| `3V3` | Van DevKit → OLED/I2C/J_ENC/J_W5500 |
| `LED1_IN` … `LED3_IN` | GPIO → AHCT A |
| `LED1_DATA` … `LED3_DATA` | AHCT Y → R → J_LED DATA |
| `SERVO1_PWM`, `SERVO2_PWM` | GPIO15/16 |
| `LD_ESP_RX`, `LD_ESP_TX` | UART1 |
| `I2C_SDA`, `I2C_SCL` | GPIO8/9 |
| `BTN1` … `BTN3` | Via J_BTN alleen |
| `ENC_CLK`, `ENC_DT`, `ENC_SW` | Via J_ENC alleen |
| `SPI_*`, `ETH_*` | W5500 optioneel |

**Verwijderd:** `LED4_*`, `F_MAIN`, on-board SW/ENC/F_OLED nets.

---

## Voeding

```text
J_MAIN.1 (5V) ── 5V_MAIN ── C_MAIN+
J_MAIN.2 (GND) ── GND ───── C_MAIN-

5V_MAIN ── 5V_LOGIC ──┬── F_ESP.5V
                      ├── U2.14 (VCC)
                      └── J_LD2450.1

5V_MAIN ── 5V_LED ── J_LED1..3.1

5V_MAIN ── SJ_SERVO.1
SJ_SERVO.2 ── 5V_SERVO ── J_SERVO*.2, C_SERVO+

F_ESP.3V3 ── 3V3 ── J_OLED_EXT, J_I2C, J_ENC, J_W5500.1
```

Geen polyfuse / F_MAIN in actief schema.

---

## SN74AHCT125N (U2) — 3 actieve kanalen

```text
U2.14 (VCC) ── 5V_LOGIC ; U2.7 (GND) ── GND
~OE 1,4,10,13 ── GND

GPIO18 ── U2.2/3 ── R_LED1 ── J_LED1.3
GPIO17 ── U2.5/6 ── R_LED2 ── J_LED2.3
GPIO21 ── U2.9/8 ── R_LED3 ── J_LED3.3

U2.11 (4A), U2.12 (4Y) ── DNP/NC (niet gerouteerd)
```

---

## LED connectors (×3, schroefklem 5,08 mm)

| Pin | Signaal |
|---|---|
| 1 | 5V_LED |
| 2 | GND |
| 3 | LEDn_DATA |

---

## UI (extern alleen)

```text
J_BTN: GND | BTN1 | BTN2 | BTN3  (GPIO 1, 2, 42)
J_ENC: GND | 3V3 | CLK | DT | SW  (GPIO 6, 7, 40)
```

Geen SW1–3 of ENC1 footprint op PCB.

---

## W5500 optional (SBC-USR-ES1, NOT POPULATED)

Zie v0.2 SPI-netten (GPIO5/13/14/47/4/39). Header **TBD** — meet module vóór fab.

---

## Servo, LD2450, I2C

Ongewijzigde logica; GPIO 15/16, 10/11, 8/9 — zie pinout-table.
