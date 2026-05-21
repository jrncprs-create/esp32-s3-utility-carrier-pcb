# Pinout-tabel (v0.2)

**Status:** logische toewijzing na conflict-check (LED ×4, LD2450, I2C, knoppen, encoder, servo’s, **optionele W5500**).  
**Voorlopig** — footprint = Espressif DevKitC-1-ref (diymore B0F3XMYYQY); fysieke meting volgt later.

Legenda risico: **Laag** | **Midden** | **Hoog** | **Verboden**

## Gebruikte GPIO (geen overlap)

| Functie | ESP32 GPIO | DevKit-header (v1.1 ref.) | Connector / component | Reden | Risico / opmerking |
|---|---|---|---|---|---|
| LED DATA OUT 1 | **GPIO18** | Pin “18” | U2 ch1 → R_LED1 → J_LED1 | 3×5 buis #1 | **Midden:** UART2 TX default — firmware als GPIO |
| LED DATA OUT 2 | **GPIO17** | Pin “17” | U2 ch2 → R_LED2 → J_LED2 | 3×5 buis #2 | **Midden:** UART2 TX default — firmware als GPIO |
| LED DATA OUT 3 | **GPIO21** | Pin “21” | U2 ch3 → R_LED3 → J_LED3 | 3×5 buis #3 | **Laag** |
| LED DATA OUT 4 (AUX) | **GPIO12** | Pin “12” | U2 ch4 → R_LED4 → J_LED4 | Reserve / 4e strip | **Laag** — niet delen met W5500 |
| I2C SDA | **GPIO8** | Pin “8” | J_OLED, J_I2C, F_OLED | I2C bus | **Laag** |
| I2C SCL | **GPIO9** | Pin “9” | J_OLED, J_I2C, F_OLED | I2C bus | **Laag** |
| Knop BTN1 | **GPIO1** | Pin “1” | SW1 / J_BTN | Geen strapping | **Laag** |
| Knop BTN2 | **GPIO2** | Pin “2” | SW2 / J_BTN | Geen strapping | **Laag** |
| Knop BTN3 | **GPIO42** | Pin “42” | SW3 / J_BTN | Vrij op DevKit | **Laag** |
| Encoder CLK | **GPIO6** | Pin “6” | ENC1 / J_ENC | Quadrature | **Laag** |
| Encoder DT | **GPIO7** | Pin “7” | ENC1 / J_ENC | Quadrature | **Laag** |
| Encoder SW | **GPIO40** | Pin “40” | ENC1 / J_ENC | Push | **Laag** |
| Servo PWM 1 | **GPIO15** | Pin “15” | J_SERVO1 pin3 | LEDC | **Laag** |
| Servo PWM 2 | **GPIO16** | Pin “16” | J_SERVO2 pin3 | LEDC | **Midden:** UART2 RX default op sommige docs |
| LD2450 → ESP (RX) | **GPIO10** | Pin “10” | J_LD2450 pin3 | UART1 RX | **Laag** — LD **TX** hier |
| ESP → LD2450 (TX) | **GPIO11** | Pin “11” | J_LD2450 pin4 | UART1 TX | **Laag** — LD **RX** hier |
| W5500 SPI_SCK | **GPIO5** | Pin “5” | J_W5500 pin3 | Dedicated SPI2 | **Laag** — alleen bij populated W5500 |
| W5500 SPI_MOSI | **GPIO13** | Pin “13” | J_W5500 pin4 | SPI data out | **Laag** |
| W5500 SPI_MISO | **GPIO14** | Pin “14” | J_W5500 pin5 | SPI data in | **Laag** |
| W5500 ETH_CS | **GPIO47** | Pin “47” | J_W5500 pin6 | Chip select | **Laag** |
| W5500 ETH_RST | **GPIO4** | Pin “4” | J_W5500 pin7 | Reset | **Laag** |
| W5500 ETH_INT | **GPIO39** | Pin “39” | J_W5500 pin8 | IRQ | **Midden:** niet op alle clones gebroken uit — meten |

## SN74AHCT125N koppeling (4 kanalen)

| AHCT kanaal | ~OE → GND | A (in) | Y → R 330 Ω → DATA |
|---|---|---|---|
| 1 | pin 1 | GPIO18 | J_LED1 |
| 2 | pin 4 | GPIO17 | J_LED2 |
| 3 | pin 13 | GPIO21 | J_LED3 |
| 4 | pin 10 | GPIO12 | J_LED4 (AUX) |

**~OE:** pins **1, 4, 10, 13** → GND (altijd enabled).

## W5500 header (optioneel, niet geplaatst)

| J_W5500 pin | Net | ESP32 |
|---|---|---|
| 1 | 3V3 | DevKit 3V3 |
| 2 | GND | GND |
| 3 | SPI_SCK | GPIO5 |
| 4 | SPI_MOSI | GPIO13 |
| 5 | SPI_MISO | GPIO14 |
| 6 | ETH_CS | GPIO47 |
| 7 | ETH_RST | GPIO4 |
| 8 | ETH_INT | GPIO39 |

Silk / value: **W5500 OPTIONAL / NOT POPULATED**.

## Verboden / niet gebruiken (N16R8)

| GPIO | Reden |
|---|---|
| 19, 20 | USB D± op DevKit |
| 35, 36, 37 | Octal flash/PSRAM |
| 43, 44 | UART0 debug |
| 0, 3, 45, 46 | Strapping |
| 38, 48 | Onboard LED’s DevKit |

## Conflict-check v0.2 (samenvatting)

- **Geen dubbele GPIO** tussen LED, LD2450, I2C, knoppen, encoder, servo’s en W5500-SPI.
- **GPIO12** alleen LED4 (AHCT ch4), niet W5500.
- **GPIO13/14/47/4/5/39** alleen W5500-route (header leeg = vrij in firmware zolang module niet gemonteerd).
- **J_GPIO** (v0.1) vervangen door **J_W5500** — geen generieke 8p GPIO-header meer.

## GPIO’s bewust vrijgehouden

GPIO41, en overige niet in tabel — proto / toekomstige jumpers.

## Clone-check (werkplaats)

1. Continuity: header pin ↔ module GPIO (minimaal LED18, I2C8/9, W5500 pin3↔GPIO5).
2. Bevestig **geen** gebruik van GPIO35–37 in firmware of bedrading.
3. Controleer of **GPIO39** fysiek op header zit (W5500 INT).

Bron in repo: `kicad/tools/generate_placeholder.py` → `PINOUT` dict.
