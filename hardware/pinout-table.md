# Pinout-tabel (v0.9 phase 2)

**Status:** 3× LED actief; GPIO12 **vrij**; UI alleen via J_BTN / J_ENC; W5500 optioneel.  
**Footprint:** Espressif DevKitC-1 **25,4×52,5 mm**, rij **22,86 mm** — verify clone.

Legenda risico: **Laag** | **Midden** | **Hoog** | **Verboden**

## Gebruikte GPIO

| Functie | ESP32 GPIO | DevKit-header | Connector / component | Opmerking | Risico |
|---|---|---|---|---|---|
| LED DATA OUT 1 | **GPIO18** | Pin “18” | U2 ch1 → R_LED1 → J_LED1 | 3×5 buis #1 | **Midden** (UART2 TX default) |
| LED DATA OUT 2 | **GPIO17** | Pin “17” | U2 ch2 → R_LED2 → J_LED2 | #2 | **Midden** |
| LED DATA OUT 3 | **GPIO21** | Pin “21” | U2 ch3 → R_LED3 → J_LED3 | #3 | **Laag** |
| I2C SDA | **GPIO8** | Pin “8” | J_OLED_EXT, J_I2C | I2C bus | **Laag** |
| I2C SCL | **GPIO9** | Pin “9” | J_OLED_EXT, J_I2C | I2C bus | **Laag** |
| Knop BTN1 | **GPIO1** | Pin “1” | J_BTN | Extern | **Laag** |
| Knop BTN2 | **GPIO2** | Pin “2” | J_BTN | Extern | **Laag** |
| Knop BTN3 | **GPIO42** | Pin “42” | J_BTN | Extern | **Laag** |
| Encoder CLK | **GPIO6** | Pin “6” | J_ENC | Extern EC11 | **Laag** |
| Encoder DT | **GPIO7** | Pin “7” | J_ENC | Extern | **Laag** |
| Encoder SW | **GPIO40** | Pin “40” | J_ENC | Extern | **Laag** |
| Servo PWM 1 | **GPIO15** | Pin “15” | J_SERVO1 | LEDC | **Laag** |
| Servo PWM 2 | **GPIO16** | Pin “16” | J_SERVO2 | LEDC | **Midden** |
| LD2450 → ESP RX | **GPIO10** | Pin “10” | J_LD2450 | UART1 | **Laag** |
| ESP → LD2450 TX | **GPIO11** | Pin “11” | J_LD2450 | UART1 | **Laag** |
| W5500 SPI_SCK | **GPIO5** | Pin “5” | J_W5500 | Optioneel | **Laag** |
| W5500 SPI_MOSI | **GPIO13** | Pin “13” | J_W5500 | Optioneel | **Laag** |
| W5500 SPI_MISO | **GPIO14** | Pin “14” | J_W5500 | Optioneel | **Laag** |
| W5500 ETH_CS | **GPIO47** | Pin “47” | J_W5500 | Optioneel | **Laag** |
| W5500 ETH_RST | **GPIO4** | Pin “4” | J_W5500 | Optioneel | **Laag** |
| W5500 ETH_INT | **GPIO39** | Pin “39” | J_W5500 | Optioneel | **Midden** |

## SN74AHCT125N (3 actieve kanalen + ch4 DNP)

| Kanaal | ~OE → GND | A (in) | Y → R 330 Ω → DATA |
|---|---|---|---|
| 1 | pin 1 | GPIO18 | J_LED1 |
| 2 | pin 4 | GPIO17 | J_LED2 |
| 3 | pin 13 | GPIO21 | J_LED3 |
| 4 | pin 10 | — | **DNP/NC** (4A/4Y niet gerouteerd) |

## GPIO12

**Niet gebruikt** op carrier — vrij voor firmware/proto; niet als LED4/AUX.

## W5500 (optioneel)

Zie v0.2 tabel (J_W5500 3V3, GND, SPI, CS/RST/INT). Module **SBC-USR-ES1** — header **TBD**.

## Verboden GPIO (N16R8)

19, 20, 35–37, 43, 44, 0, 3, 45, 46, 38, 48 — zie technical-spec.

Bron: `kicad/tools/generate_placeholder.py` → `PINOUT`.
