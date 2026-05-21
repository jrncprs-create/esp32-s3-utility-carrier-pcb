# Connectorlijst (v0.2)

**Familie signaal / lichte voeding:** JST-XH 2,54 mm through-hole (JST **B2B-XH-A**-reeks of compatibel).  
**Hoofdvoeding:** JST-VH 3,96 mm **of** schroefklem — zie stroomkolom.

**Pin-weergave:** connector op PCB, kijkend naar **front** (kabel komt van buiten); **pin 1 = vierkant pad**.

---

## Overzicht

| Ref | Naam | Polen | Footprint voorstel | Stroomrisico |
|---|---|---|---|---|
| J_MAIN | 5V MAIN IN | 2 | **JST-VH B2B-VH-A(LF)(SN)** 2p **of** Phoenix 1980618 2p 5,08 mm | **Hoog** — totale installatie |
| J_MAIN_XH | 5V MAIN (alt.) | 2 | JST-XH B2B-XH-A 2p | **Midden** — max ~2 A aanbevolen |
| PAD_PWR | Power pads | 2×(5V+GND) | 3 mm × 6 mm oval pads | **Hoog** — parallel aan J_MAIN |
| J_LED1–4 | LED strip OUT | 3 | JST-XH B2B-XH-A 3p | **Midden** op 5V pin (LED-stroom); LED4 = AUX |
| J_W5500 | W5500 module (opt.) | 8 | JST-XH 8p placeholder | **Laag** signaal (3V3); **NOT POPULATED** |
| J_SERVO1–2 | Servo | 3 | JST-XH B2B-XH-A 3p | **Hoog** op 5V pin per kanaal |
| J_LD2450 | LD2450 UART | 4 | JST-XH B2B-XH-A 4p | **Laag–Midden** (~150 mA) |
| J_OLED_EXT | OLED extern | 4 | JST-XH B2B-XH-A 4p | **Laag** (3V3) |
| J_I2C | I2C bus | 4 | JST-XH B2B-XH-A 4p | **Laag** |
| J_BTN | Knoppen extern | 4 | JST-XH B2B-XH-A 4p | **Laag** |
| J_ENC | Rotary extern | 5 | JST-XH B2B-XH-A 5p | **Laag** |
| F_ESP | ESP32 DevKit | 2×20 | Pin header 2,54 mm, rij 22,86 mm **VOORLOPIG** | n.v.t. |
| F_OLED | OLED direct | 4 | 1×4 pinheader 2,54 mm | **Laag** |
| SW1–3 | Tact switch | 2 | 6×6 mm tactile TH | **Laag** |
| ENC1 | EC11 | 5+2 | EC11 18 mm / 20 mm shaft footprint | **Laag** |

---

## Pinvolgorde per connector

### J_MAIN (primair) — JST-VH 2p

| Pin | Signaal | Opmerking |
|---|---|---|
| 1 | **5V_MAIN** | + polariteit duidelijk silkscreen |
| 2 | **GND** | |

### J_MAIN_XH (optioneel secundair)

| Pin | Signaal | Stroom |
|---|---|---|
| 1 | 5V_MAIN | Label: *max 2 A* |
| 2 | GND | |

### J_LED1 / J_LED2 / J_LED3 — JST-XH 3p

| Pin | Signaal | Stroom |
|---|---|---|
| 1 | **5V_LED** | LED-stroom (kan A’s zijn) — dikke spoor naar MAIN |
| 2 | **GND** | Terug |
| 3 | **DATA** | Via 330 Ω + AHCT125 |

Silkscreen op PCB (groot): `5V | GND | DATA`

### J_SERVO1 / J_SERVO2 — JST-XH 3p

| Pin | Signaal | Stroom |
|---|---|---|
| 1 | **GND** | Terug — breed naar GND pour |
| 2 | **5V_SERVO** | Piek tot ~2 A/servo |
| 3 | **PWM** | Signaal &lt; 1 mA |

Silkscreen: `GND | 5V | PWM`

### J_LD2450 — JST-XH 4p

| Pin | Signaal | Opmerking |
|---|---|---|
| 1 | **5V** | 5V_LOGIC |
| 2 | **GND** | |
| 3 | **ESP_RX** | Verbind met **TX** van LD2450 |
| 4 | **ESP_TX** | Verbind met **RX** van LD2450 |

Silkscreen dubbel label:  
`Pin3 ESP_RX ← LD_TX`  
`Pin4 ESP_TX → LD_RX`

### J_OLED_EXT / J_I2C — JST-XH 4p

| Pin | Signaal |
|---|---|
| 1 | GND |
| 2 | 3V3 |
| 3 | SDA (GPIO8) |
| 4 | SCL (GPIO9) |

### J_BTN — JST-XH 4p

| Pin | Signaal |
|---|---|
| 1 | GND |
| 2 | BTN1 (GPIO1) |
| 3 | BTN2 (GPIO2) |
| 4 | BTN3 (GPIO42) |

Externe knop: tussen pin en GND sluiten.

### J_ENC — JST-XH 5p

| Pin | Signaal |
|---|---|
| 1 | GND |
| 2 | 3V3 |
| 3 | CLK (GPIO6) |
| 4 | DT (GPIO7) |
| 5 | SW (GPIO40) |

### J_W5500 — JST-XH 8p (OPTIONAL / NOT POPULATED)

| Pin | Signaal | ESP32 GPIO |
|---|---|---|
| 1 | **3V3** | DevKit 3V3 |
| 2 | **GND** | GND |
| 3 | **SPI_SCK** | GPIO5 |
| 4 | **SPI_MOSI** | GPIO13 |
| 5 | **SPI_MISO** | GPIO14 |
| 6 | **ETH_CS** | GPIO47 |
| 7 | **ETH_RST** | GPIO4 |
| 8 | **ETH_INT** | GPIO39 |

Silkscreen: `W5500 OPTIONAL` · `NOT POPULATED`. Geen 5V op deze header (module 3V3 only).

### F_OLED direct (pinheader)

| Pin | Signaal |
|---|---|
| 1 | GND |
| 2 | 3V3 |
| 3 | SDA |
| 4 | SCL |

**Let op:** sommige OLED-modules hebben VCC op pin1 — **meet module** vóór definitieve footprint.

---

## SJ_SERVO (geen JST)

| Pad | Net |
|---|---|
| 1 | 5V_MAIN |
| 2 | 5V_SERVO |

Default: **gesloten** (0 Ω bridge / gesoldeerd). Open = servo's alleen extern voeden, signaal blijft.

---

## Stroomrisico-samenvatting

| Scenario | Risico | Mitigatie |
|---|---|---|
| 2 servo's + 500 LED @ 5V | **Hoog** op MAIN | JST-VH of schroefklem + brede sporen + C_MAIN/C_SERVO |
| Alleen 1 servo + sensor | **Midden** | JST-VH aanbevolen; XH kan met voorbehoud |
| Alleen LED data (externe PSU op strips) | **Laag** op DATA; 5V pin nog steeds midden | Documenteer dat LED-VCC apart mag |
| LD2450 + OLED | **Laag** | Standaard XH 4p OK |

---

## KiCad footprint namen (voorstel, nog te valideren)

| Footprint ID | Omschrijving |
|---|---|
| `Connector_JST:JST_XH_B2B-XH-A_1x03_P2.50mm_Vertical` | 3p XH |
| `Connector_JST:JST_XH_B2B-XH-A_1x04_P2.50mm_Vertical` | 4p |
| `Connector_JST:JST_XH_B2B-XH-A_1x05_P2.50mm_Vertical` | 5p |
| `Connector_JST:JST_XH_B2B-XH-A_1x08_P2.50mm_Vertical` | 8p (legacy) |
| `carrier:JST_W5500_1x08_Placeholder` | W5500 opt. |
| `Connector_JST:JST_VH_B2B-VH-A_1x02_P3.96mm_Vertical` | 2p MAIN |
| `Connector_PinHeader_2.54mm:PinHeader_1x20_P2.54mm_Vertical` | ESP32 **placeholder** |
