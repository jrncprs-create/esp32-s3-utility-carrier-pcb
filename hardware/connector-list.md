# Connectorlijst (v0.9 phase 2)

**Hoofdvoeding + LED:** schroefklem **5,08 mm** (placeholder in KiCad).  
**Overige signalen:** JST-XH 2,54 mm through-hole waar mogelijk.

**Pin 1 = vierkant pad** (kijkend naar connector-front).

---

## Overzicht

| Ref | Naam | Polen | Footprint | Opmerking |
|---|---|---|---|---|
| J_MAIN | 5V MAIN IN | 2 | Schroefklem 5,08 mm | **Geen** fuse; 5V\|GND |
| J_LED1–3 | LED OUT | 3 | Schroefklem 5,08 mm | 5V\|GND\|DATA |
| J_SERVO1–2 | Servo | 3 | JST-XH 3p | GND\|5V\|PWM |
| J_LD2450 | LD2450 | 4 | JST-XH 4p | |
| J_OLED_EXT | OLED extern | 4 | JST-XH 4p | Geen F_OLED |
| J_I2C | I2C | 4 | JST-XH 4p | |
| J_BTN | Knoppen extern | 4 | JST-XH 4p | Geen SW1–3 |
| J_ENC | Encoder extern | 5 | JST-XH 5p | Geen ENC1 footprint |
| J_W5500 | W5500 module | 8 | SBC-USR-ES1 placeholder | **NOT POPULATED** |
| F_ESP | DevKitC-1 | 2×20 | 25,4×52,5 mm TBD | Verify clone |

**Verwijderd:** F_MAIN, J_MAIN JST-VH-only, J_LED4, F_OLED, SW1–3, ENC1.

---

## Pinvolgorde

### J_MAIN — schroefklem 2p 5,08 mm

| Pin | Signaal |
|---|---|
| 1 | **5V_MAIN** |
| 2 | **GND** |

### J_LED1–3 — schroefklem 3p 5,08 mm

| Pin | Signaal |
|---|---|
| 1 | **5V_LED** |
| 2 | **GND** |
| 3 | **DATA** (330 Ω + AHCT) |

Silk: `5V | GND | DATA`

### J_SERVO1/2 — JST-XH 3p

| Pin | Signaal |
|---|---|
| 1 | GND |
| 2 | 5V_SERVO |
| 3 | PWM |

### J_LD2450 — JST-XH 4p

| Pin | Signaal |
|---|---|
| 1 | 5V_LOGIC |
| 2 | GND |
| 3 | ESP_RX ← LD_TX |
| 4 | ESP_TX → LD_RX |

### J_OLED_EXT / J_I2C — JST-XH 4p

| Pin | Signaal |
|---|---|
| 1 | GND |
| 2 | 3V3 |
| 3 | SDA |
| 4 | SCL |

### J_BTN — JST-XH 4p

| Pin | Signaal |
|---|---|
| 1 | GND |
| 2 | BTN1 |
| 3 | BTN2 |
| 4 | BTN3 |

### J_ENC — JST-XH 5p

| Pin | Signaal |
|---|---|
| 1 | GND |
| 2 | 3V3 |
| 3 | CLK |
| 4 | DT |
| 5 | SW |

### J_W5500 — SBC-USR-ES1 (header TBD)

| Pin | Net | GPIO |
|---|---|---|
| 1 | 3V3 | DevKit |
| 2 | GND | |
| 3 | SPI_SCK | 5 |
| 4 | SPI_MOSI | 13 |
| 5 | SPI_MISO | 14 |
| 6 | ETH_CS | 47 |
| 7 | ETH_RST | 4 |
| 8 | ETH_INT | 39 |

Module **23×29×24 mm**; RJ45 naar boardrand; meet header vóór fab.

### F_ESP — DevKitC-1

| Parameter | Waarde |
|---|---|
| PCB | **25,4 × 52,5 mm** (Espressif official) |
| Pinrij | 2×20 @ 2,54 mm |
| Rij-afstand | **22,86 mm** |

Label op PCB: *DevKitC-1 dims assumed — verify clone before fab*.
