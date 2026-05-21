# Schema / netlist (mensentaal) v0.2

Logische netlist voor het placeholder-schema. KiCad-bestanden in `kicad/` worden gegenereerd via `generate_placeholder.py`.

---

## Nets (hoofdlijst)

| Net | Beschrijving |
|---|---|
| `GND` | Common ground |
| `5V_MAIN` | Ingang J_MAIN (+ PAD_PWR) |
| `5V_LOGIC` | ESP32 VIN, AHCT VCC, LD2450 5V |
| `5V_LED` | 5V op J_LED1..4 |
| `5V_SERVO` | Servo 5V via SJ_SERVO |
| `3V3` | Van DevKit naar OLED/I2C/ENC/**J_W5500** |
| `LED1_IN` … `LED4_IN` | GPIO → AHCT A inputs |
| `LED1_DATA` … `LED4_DATA` | AHCT Y → R → J_LED DATA |
| `SERVO1_PWM`, `SERVO2_PWM` | GPIO15/16 → J_SERVO |
| `LD_ESP_RX`, `LD_ESP_TX` | GPIO10/11 ↔ J_LD2450 |
| `I2C_SDA`, `I2C_SCL` | GPIO8/9 bus |
| `BTN1` … `BTN3` | GPIO knoppen |
| `ENC_CLK`, `ENC_DT`, `ENC_SW` | Encoder |
| `SPI_SCK`, `SPI_MOSI`, `SPI_MISO` | W5500 SPI (GPIO5/13/14) |
| `ETH_CS`, `ETH_RST`, `ETH_INT` | W5500 control (GPIO47/4/39) |

---

## Voeding

```text
J_MAIN.1 (5V) ──┬── F_MAIN (optioneel) ──┬── 5V_MAIN
J_MAIN.2 (GND) ─┴── GND ─────────────────┴── (star bij connector)

5V_MAIN ── C_MAIN+ ; C_MAIN- ── GND

5V_MAIN ── 5V_LOGIC ──┬── F_ESP.5V
                      ├── U2.14 (VCC)
                      ├── J_LD2450.1
                      └── J_LEDx.1 (×4)

5V_MAIN ── SJ_SERVO.1
SJ_SERVO.2 ── 5V_SERVO ── J_SERVO*.2, C_SERVO+

F_ESP.3V3 ── 3V3 ── J_OLED, J_I2C, J_ENC, J_W5500.1
F_ESP.GND ── GND pour
```

---

## SN74AHCT125N (U2) — 4 LED-kanalen

```text
U2.14 (VCC) ── 5V_LOGIC ; U2.7 (GND) ── GND
~OE pins 1,4,10,13 ── GND

F_ESP.GPIO18 ── U2.2 (1A) ── U2.3 (1Y) ── R_LED1 ── J_LED1.3
F_ESP.GPIO17 ── U2.5 (2A) ── U2.6 (2Y) ── R_LED2 ── J_LED2.3
F_ESP.GPIO21 ── U2.9 (3A) ── U2.8 (3Y) ── R_LED3 ── J_LED3.3
F_ESP.GPIO12 ── U2.11 (4A) ── U2.12 (4Y) ── R_LED4 ── J_LED4.3
```

---

## LED connectors (×4)

```text
J_LEDn.1 ── 5V_LED ; J_LEDn.2 ── GND ; J_LEDn.3 ── LEDn_DATA
```

---

## W5500 optional (NOT POPULATED)

```text
J_W5500.1 ── 3V3
J_W5500.2 ── GND
J_W5500.3 ── SPI_SCK  ← F_ESP.GPIO5
J_W5500.4 ── SPI_MOSI ← F_ESP.GPIO13
J_W5500.5 ── SPI_MISO ← F_ESP.GPIO14
J_W5500.6 ── ETH_CS   ← F_ESP.GPIO47
J_W5500.7 ── ETH_RST  ← F_ESP.GPIO4
J_W5500.8 ── ETH_INT  ← F_ESP.GPIO39
```

Module footprint op carrier: **niet gemonteerd in v0.2 placeholder**. Bedrade W5500-breakout of Ethernet-shield voor toekomstige Resolume / Art-Net / sACN route.

---

## Servo, LD2450, I2C, knoppen, encoder

Ongewijzigd t.o.v. v0.1 logica — zie v0.1 secties; GPIO’s:

- Servo: **15**, **16**
- LD2450 UART1: **10**, **11**
- I2C: **8**, **9**
- Knoppen: **1**, **2**, **42**
- Encoder: **6**, **7**, **40**

---

## Netlist-tabel (compact)

| Net | Van | Naar |
|---|---|---|
| LED4_IN | F_ESP.12 | U2.11 |
| LED4_DATA | U2.12 | R_LED4 → J_LED4.3 |
| SPI_SCK | F_ESP.5 | J_W5500.3 |
| ETH_INT | F_ESP.39 | J_W5500.8 |

---

## ERC-aandachtspunten

- Geen verbinding naar GPIO19/20/35–38/43/44/0/3/45/46/48.
- W5500-header mag “unconnected” ERC geven tot module + firmware — verwacht in placeholder.
- `5V_MAIN` en `3V3` nooit kort.
