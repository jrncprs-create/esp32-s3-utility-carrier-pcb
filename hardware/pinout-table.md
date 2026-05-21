# Pinout-tabel (voorstel v0.9)

**Status:** logische toewijzing op basis van ESP32-S3-DevKitC-1 v1.1 + N16R8-aannames.  
**Voorlopig** — footprint = Espressif DevKitC-1-ref (diymore B0F3XMYYQY); fysieke meting en continuity-check volgen later.

Legenda risico: **Laag** | **Midden** | **Hoog** | **Verboden**

| Functie | ESP32 GPIO | DevKit-header (v1.1 ref.) | Connector / component | Reden | Risico / opmerking |
|---|---|---|---|---|---|
| LED DATA OUT 1 | **GPIO18** | Pin “18” | U2 ch1 → R_LED1 → J_LED1 | Door gebruiker gewenst; header beschikbaar; AHCT 5V uit | **Midden:** default UART2 TX op sommige pin-tabellen — in firmware gewone GPIO |
| LED DATA OUT 2 | **GPIO17** | Pin “17” | U2 ch2 → R_LED2 → J_LED2 | Vrij op N16R8; naast OUT1 | **Midden:** UART2 TX default — remap in code |
| LED DATA OUT 3 | **GPIO21** | Pin “21” | U2 ch3 → R_LED3 → J_LED3 | Vrij; geen USB/strapping | **Laag** |
| AHCT125 kanaal 4 | — | — | U2 ch4 NC / TP4 | Reserve test | **Laag** |
| I2C SDA | **GPIO8** | Pin “8” | J_OLED, J_I2C, F_OLED | Standaard veilige header-I2C | **Laag** — clone-label controleren |
| I2C SCL | **GPIO9** | Pin “9” | J_OLED, J_I2C, F_OLED | Idem | **Laag** |
| Knop BTN1 | **GPIO1** | Pin “1” (rechter rij) | SW1 of J_BTN pin2 | Geen strapping; ADC-capable | **Laag** |
| Knop BTN2 | **GPIO2** | Pin “2” | SW2 of J_BTN pin3 | Idem | **Laag** |
| Knop BTN3 | **GPIO42** | Pin “42” | SW3 of J_BTN pin4 | Vrij op DevKit | **Laag** |
| Encoder CLK | **GPIO6** | Pin “6” | ENC1 / J_ENC pin3 | Geen kritieke functie | **Laag** |
| Encoder DT | **GPIO7** | Pin “7” | ENC1 / J_ENC pin4 | Idem | **Laag** |
| Encoder SW | **GPIO40** | Pin “40” | ENC1 / J_ENC pin5 | Push switch | **Laag** |
| Servo PWM 1 | **GPIO15** | Pin “15” | J_SERVO1 pin3 | LEDC-capable | **Laag** — niet als UART2 RX gebruiken |
| Servo PWM 2 | **GPIO16** | Pin “16” | J_SERVO2 pin3 | LEDC-capable | **Midden:** HW UART2 RX default op sommige docs — alleen PWM in v1 |
| LD2450 → ESP (RX) | **GPIO10** | Pin “10” | J_LD2450 pin3 (ESP_RX) | UART1 RX; weg van UART0 | **Laag** — kabel: LD **TX** hier |
| ESP → LD2450 (TX) | **GPIO11** | Pin “11” | J_LD2450 pin4 (ESP_TX) | UART1 TX | **Laag** — kabel: LD **RX** hier |
| Extra GPIO A | **GPIO12** | Pin “12” | J_GPIO | Vrij | **Laag** |
| Extra GPIO B | **GPIO13** | Pin “13” | J_GPIO | Vrij | **Laag** |
| Extra GPIO C | **GPIO14** | Pin “14” | J_GPIO | Vrij | **Laag** |
| Extra GPIO D | **GPIO47** | Pin “47” | J_GPIO | Vrij | **Laag** |
| ESP32 5V in | — | 5V pins (×2) | 5V_LOGIC van 5V_MAIN | Voed DevKit + interne 3V3 LDO | **Midden:** totale stroom via DevKit pins |
| ESP32 GND | — | GND (×4) | GND pour | Sterpunt bij main | **Laag** |
| 3V3 distributie | — | 3V3 (×2) | J_OLED, J_I2C, J_ENC | Van DevKit LDO | **Midden:** budget ~150 mA voor peripherals |
| USB D- | **GPIO19** | — | **Niet aangesloten** | USB fysiek op DevKit | **Verboden** op carrier |
| USB D+ | **GPIO20** | — | **Niet aangesloten** | Idem | **Verboden** |
| UART0 TX | **GPIO43** | “TX” | **Niet aangesloten** | USB-serial debug | **Verboden** |
| UART0 RX | **GPIO44** | “RX” | **Niet aangesloten** | Idem | **Verboden** |
| Octal mem | **GPIO35–37** | Pins 35–37 | **Niet aangesloten** | N16R8 intern flash/PSRAM | **Verboden** |
| RGB LED | **GPIO38** | Pin “38” | **Niet aangesloten** | Onboard DevKit LED | **Verboden** |
| Strapping | **GPIO0,3,45,46** | 0,3,45,46 | **Niet aangesloten** | Boot mode | **Verboden** |
| Board LED | **GPIO48** | Pin “48” | **Niet aangesloten** | DevKit power LED | **Verboden** |

## SN74AHCT125N koppeling

| AHCT kanaal | ~OE → GND | A (in) | Y → R 330Ω → DATA |
|---|---|---|---|
| 1 | pin 1 | GPIO18 | J_LED1 |
| 2 | pin 4 | GPIO17 | J_LED2 |
| 3 | pin 13 | GPIO21 | J_LED3 |
| 4 | pin 10 | NC | — |

**Let op pin 13 = 3~OE** en **pin 10 = 4~OE** op SN74AHCT125N — beide naar GND samen met pin 1 en 4.

## GPIO’s bewust vrijgehouden

GPIO4, 5, 39, 41, and others not in table — beschikbaar voor v2 of re-routing via solder jumpers (niet in v1 tenzij proto-area).

## Clone-check (werkplaats)

1. Multimeter: DevKit header pin “18” ↔ module pin GPIO18 (continuity of silkscreen diagram).
2. Bevestig dat header **geen** GPIO35–37 naar buiten routeert als bruikbare I/O (bij N16R8 vaak wel fysiek aanwezig maar **niet gebruiken**).
3. Meet of **dubbele USB-C** aan dezelfde kant zitten als Espressif v1.1 tekening.
