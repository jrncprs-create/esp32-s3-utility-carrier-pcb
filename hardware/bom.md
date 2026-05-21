# Bill of Materials — ESP32-S3 Utility Carrier v1 (v0.9 phase 2)

**Geen productie-BOM** — W5500-header en ESP32-footprint **TBD** (meten vóór fab).

| Ref | Component | Waarde / type | Footprint (voorstel) | Verplicht | Opmerking |
|---|---|---|---|---|---|
| — | **DevKit (niet op BOM PCB)** | ESP32-S3-DevKitC-1 N16R8 clone | — | **Ja** | Door gebruiker; USB blijft op DevKit |
| F_ESP1 | Pinheader female | 1×20 ×2, 2,54 mm | `PinHeader_1x20_2.54` **TBD** | **Ja** | Rij-afstand **22,86 mm** (Espressif-ref) |
| F_ESP2 | Pinheader male op DevKit | — | — | **Ja** | Op DevKit zelf |
| U2 | Levelshifter | SN74AHCT125N / 74AHCT125 | `DIP-14_W7.62mm` + optioneel IC-socket | **Ja** | 5 V; OE → GND; **kanaal 4 DNP/NC** |
| SKT2 | IC-socket | 14-pin DIP | `Socket_14` | Optioneel | Aanbevolen voor service |
| R_LED1 | Weerstand | 330 Ω ¼ W | `Resistor_THT:AXIAL-0.4` | **Ja** | LED DATA 1 |
| R_LED2 | Weerstand | 330 Ω ¼ W | `Resistor_THT:AXIAL-0.4` | **Ja** | LED DATA 2 |
| R_LED3 | Weerstand | 330 Ω ¼ W | `Resistor_THT:AXIAL-0.4` | **Ja** | LED DATA 3 |
| C_MAIN | Elektrolyt | 1000 µF, ≥10 V, laag ESR | `Capacitor_THT:CP_Radial` | **Ja** | Bij J_MAIN, polariteit |
| C_SERVO | Elektrolyt | 1000–2200 µF, ≥10 V | `Capacitor_THT:CP_Radial` | **Ja** * | *Verplicht bij servo-gebruik |
| C_AHCT | Keramisch | 100 nF | `Capacitor_THT:C_Disc_D3mm_W2mm` | **Ja** | Decoupling U2 |
| C_LD1 | Keramisch | 100 nF | Disc 3 mm | Optioneel | J_LD2450 |
| SJ_SERVO | Solder jumper | 2-pad bridge | `SolderJumper_2_Open` | **Ja** | 5V_MAIN ↔ 5V_SERVO |
| J_MAIN | Schroefklem | 2p **5,08 mm** | `TerminalBlock` / placeholder | **Ja** | **5V | GND** — geen polyfuse |
| J_LED1–3 | Schroefklem | 3p **5,08 mm** | `TerminalBlock_3p` | **Ja** * | *Min. 1 als LED gebruikt; **5V\|GND\|DATA** |
| J_SERVO1 | Connector | JST-XH 3p | `JST_XH_1x03` | Optioneel* | *Bij servo |
| J_SERVO2 | Connector | JST-XH 3p | `JST_XH_1x03` | Optioneel | |
| J_LD2450 | Connector | JST-XH 4p | `JST_XH_1x04` | Optioneel* | *Bij sensor |
| J_OLED_EXT | Connector | JST-XH 4p | `JST_XH_1x04` | Optioneel | Extern OLED |
| J_I2C | Connector | JST-XH 4p | `JST_XH_1x04` | Optioneel | Extra I2C |
| J_BTN | Connector | JST-XH 4p | `JST_XH_1x04` | Optioneel | **Alleen** externe knoppen |
| J_ENC | Connector | JST-XH 5p | `JST_XH_1x05` | Optioneel | **Alleen** externe EC11 |
| J_W5500 | Module + header | SBC-USR-ES1 W5500 | Placeholder **23×29 mm** | Optioneel | **NOT POPULATED**; header TBD |
| — | PCB | 2-layer FR4 1,6 mm | — | **Ja** | 130×85 mm; geen GND-pour |
| — | Montage | M3 standoff + schroef | 3,2 mm hole | Optioneel | 4 hoeken |

## Verwijderd t.o.v. v0.8 (niet op PCB)

| Ref | Reden |
|---|---|
| F_MAIN / polyfuse | Geen fuse in actieve BOM of layout |
| SW1–SW3 | Geen on-board tact switches |
| ENC1 | Geen on-board EC11 footprint |
| F_OLED | Geen direct-mount OLED header |
| J_LED4 / R_LED4 | Max **3** LED-uitgangen; GPIO12 vrij |

## Aantal connectoren (typische build)

| Item | Aantal |
|---|---|
| Schroefklem 2p 5,08 mm | 1 (J_MAIN) |
| Schroefklem 3p 5,08 mm | 3 (J_LED1–3) |
| JST-XH 3p | 0–2 (servo) |
| JST-XH 4p | 2–4 (sensor/OLED/I2C/BTN) |
| JST-XH 5p | 0–1 (encoder) |
| W5500 module | 0–1 (optioneel) |

Zie ook: `hardware/connector-list.md`, `hardware/measurements.md`.
