# Bill of Materials — ESP32-S3 Utility Carrier v1 (v0.9)

**Geen productie-BOM** — footprints en ESP32-header **NIET DEFINITIEF**.

| Ref | Component | Waarde / type | Footprint (voorstel) | Verplicht | Opmerking |
|---|---|---|---|---|---|
| — | **DevKit (niet op BOM PCB)** | ESP32-S3-DevKitC-1 N16R8 clone | — | **Ja** | Door gebruiker; USB blijft op DevKit |
| F_ESP1 | Pinheader female | 1×20 ×2, 2,54 mm | `PinHeader_1x20_2.54` **TBD** | **Ja** | Afstand rijen **na meting** |
| F_ESP2 | Pinheader male op DevKit | — | — | **Ja** | Op DevKit zelf |
| U2 | Levelshifter | SN74AHCT125N / 74AHCT125 | `DIP-14_W7.62mm` + optioneel IC-socket | **Ja** | 5 V voeding; OE → GND |
| SKT2 | IC-socket | 14-pin DIP | `Socket_14` | Optioneel | Aanbevolen voor service |
| R_LED1 | Weerstand | 330 Ω ¼ W | `Resistor_THT:AXIAL-0.4` | **Ja** | LED DATA 1 |
| R_LED2 | Weerstand | 330 Ω ¼ W | `Resistor_THT:AXIAL-0.4` | **Ja** | LED DATA 2 |
| R_LED3 | Weerstand | 330 Ω ¼ W | `Resistor_THT:AXIAL-0.4` | **Ja** | LED DATA 3 |
| C_MAIN | Elektrolyt | 1000 µF, ≥10 V, laag ESR | `Capacitor_THT:CP_Radial_D10mm_P5mm` | **Ja** | Bij J_MAIN, polariteit |
| C_SERVO | Elektrolyt | 1000–2200 µF, ≥10 V | `Capacitor_THT:CP_Radial_D10mm_P5mm` of D12 | **Ja** * | *Verplicht bij servo-gebruik |
| C_AHCT | Keramisch | 100 nF | `Capacitor_THT:C_Disc_D3mm_W2mm` | **Ja** | Decoupling U2 |
| C_LD1 | Keramisch | 100 nF | Disc 3 mm | Optioneel | J_LD2450 |
| C_OLED1 | Keramisch | 100 nF | Disc 3 mm | Optioneel | J_OLED / F_OLED |
| F_MAIN | PTC resettable | 1,1–2 A hold (voorstel) | `Fuseholder` / 1812 placeholder | Optioneel | Main 5V bescherming |
| SJ_SERVO | Solder jumper | 2-pad bridge | `SolderJumper_2_Open` | **Ja** | 5V_MAIN ↔ 5V_SERVO |
| J_MAIN | Connector power | JST-VH 2p 3,96 mm | `JST_VH_B2B-VH-A_1x02` | **Ja** | Primaire invoer |
| J_MAIN_XH | Connector power alt. | JST-XH 2p | `JST_XH_B2B-XH-A_1x02` | Optioneel | Label max stroom |
| PAD_PWR1–2 | Solder pads | 5V + GND | Custom 3×6 mm | **Ja** | Extra power |
| J_LED1 | Connector | JST-XH 3p | `JST_XH_1x03` | Optioneel* | *Min. 1 als LED gebruikt |
| J_LED2 | Connector | JST-XH 3p | `JST_XH_1x03` | Optioneel | |
| J_LED3 | Connector | JST-XH 3p | `JST_XH_1x03` | Optioneel | |
| J_SERVO1 | Connector | JST-XH 3p | `JST_XH_1x03` | Optioneel* | *Bij servo |
| J_SERVO2 | Connector | JST-XH 3p | `JST_XH_1x03` | Optioneel | |
| H_SERVO1–2 | Servo header alt. | 2,54 mm 1×3 rechte pins | `PinHeader_1x03` | Optioneel | Alternatief naast JST |
| J_LD2450 | Connector | JST-XH 4p | `JST_XH_1x04` | Optioneel* | *Bij sensor |
| J_OLED_EXT | Connector | JST-XH 4p | `JST_XH_1x04` | Optioneel | Extern OLED |
| F_OLED | OLED header | 1×4 2,54 mm | `PinHeader_1x04` | Optioneel | Direct mount |
| J_I2C | Connector | JST-XH 4p | `JST_XH_1x04` | Optioneel | Extra I2C |
| J_BTN | Connector | JST-XH 4p | `JST_XH_1x04` | Optioneel | Externe knoppen |
| SW1 | Tact switch | 6×6 mm | `SW_PUSH_6mm` | Optioneel | On-board BTN1 |
| SW2 | Tact switch | 6×6 mm | `SW_PUSH_6mm` | Optioneel | BTN2 |
| SW3 | Tact switch | 6×6 mm | `SW_PUSH_6mm` | Optioneel | BTN3 |
| ENC1 | Rotary encoder | EC11 20 mm, detents | `RotaryEncoder_EC11` | Optioneel | On-board |
| J_ENC | Connector | JST-XH 5p | `JST_XH_1x05` | Optioneel | Externe encoder |
| J_GPIO | Connector | JST-XH 8p | `JST_XH_1x08` | Optioneel | Extra GPIO |
| R_ENC1–3 | Pull-up | 10 kΩ | Axial 0,4 | Optioneel | DNP; firmware pull-up default |
| — | PCB | 2-layer FR4 1,6 mm | — | **Ja** | 1 oz; pour GND |
| — | Montage | M3 standoff + schroef | 3,2 mm hole | Optioneel | 4 hoeken |

## Aantal connectoren (typische volledige build)

| Item | Aantal |
|---|---|
| JST-VH 2p | 1 |
| JST-XH 3p | 3–5 (3 LED + 2 servo) |
| JST-XH 4p | 3–4 |
| JST-XH 5p | 0–1 |
| JST-XH 8p | 0–1 |

## Niet plaatsen (DNP) strategie

Voor modulaire builds mogen alleen de benodigde JST’s gesoldeerd worden; footprints blijven op PCB.

## Inkoopnotities

- **74AHCT125N** (niet HC125): 5 V-tolerant output high naar WS2812/SPI-achtige inputs.
- Elco’s: lage profiel indien behuizing laag is — footprint pas **na** behuizingmeting.
- JST-huisjes + contacten apart bestellen bij handmatig solderen van draden.

Zie ook: `hardware/bom-draft.md` (verwijzing).
