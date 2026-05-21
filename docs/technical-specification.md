# Technische specificatie — ESP32-S3 Utility Carrier PCB v1

Versie: **0.2 (placeholder)**  
Datum: 2026-05-21  
Status: **GEEN productie-PCB** · **GEEN Gerbers** · ESP32-footprint **VOORLOPIG** (Espressif-ref = diymore B0F3XMYYQY; [meting later](../hardware/measurements.md))

---

## 1. Doel en scope

### 1.1 Doel

Soldeerbare **carrier-PCB** voor een **ESP32-S3 DevKit** (plug-in via twee pin-headers), bedoeld voor interactieve installaties met:

- 1× 5 V hoofdvoeding
- 3× levelshifted LED/data-uitgangen (5 V)
- 2× servo-uitgangen
- 1× HLK-LD2450 UART-sensorpoort
- SH1106 I2C OLED (direct + extern)
- 3× drukknoppen
- EC11 rotary encoder (detents + push)
- Extra GPIO / I2C / power pads + klein proto-vak

### 1.2 Buiten scope v1

- Geen losse ESP32-WROOM-module met eigen USB
- Geen SMD-only ontwerp
- Geen PCBA/assembly (alleen kale PCB)
- Geen definitieve productiebestanden

### 1.3 Target DevKit

| Item | Waarde |
|---|---|
| Referentie | [Espressif ESP32-S3-DevKitC-1 v1.1](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32s3/esp32-s3-devkitc-1/user_guide_v1.1.html) |
| Gebruikersboard | diymore / Amazon clone, ESP32-S3-WROOM-1-**N16R8** (vermoedelijk) |
| Footprint carrier | 2× 1×20 @ **2,54 mm**, rij **22,86 mm** — **VOORLOPIG** (zie `hardware/measurements.md`) |
| USB | DevKit USB-C moet aan **rand carrier** bereikbaar blijven (beide poorten indien aanwezig) |

---

## 2. Elektrische architectuur

### 2.1 Voeding (blokdiagram)

```text
[J_MAIN 5V] ──► (F_MAIN optioneel) ──► 5V_MAIN bus
                      │
        ┌─────────────┼─────────────┬──────────────┐
        ▼             ▼             ▼              ▼
   5V_LOGIC      5V_LED       SJ_SERVO ──► 5V_SERVO
   (ESP32 VIN,   (LED JST,     (solder       (servo JST,
    AHCT125,      AHCT VCC)     jumper)       dikke sporen)
    LD2450 5V)
        │
        └──► ESP32 onboard 3V3 LDO ──► 3V3_LOGIC (OLED, I2C, encoder 3V3)
```

### 2.2 Rails

| Rail | Bron | Verbruikers | Opmerking |
|---|---|---|---|
| **5V_MAIN** | J_MAIN | Verdeeld naar sub-rails | Breedte sporen/pour afhankelijk van stroom |
| **5V_LOGIC** | 5V_MAIN | ESP32 **5V/VIN**, SN74AHCT125 VCC, LD2450 5V | Geen directe servo-last hier |
| **5V_LED** | 5V_MAIN | LED JST pin 5V (×3) | Kan viazelfde pour als MAIN; logisch gescheiden label |
| **5V_SERVO** | 5V_MAIN via **SJ_SERVO** | Servo JST 5V (×2) | Standaard **gesloten** jumper; openen = servo extern voeden |
| **3V3_LOGIC** | DevKit header 3V3 | OLED, I2C, encoder 3V3 | Geen eigen LDO op carrier v1 |
| **GND** | Common | Alles | Star-point bij J_MAIN + pour |

### 2.3 Hoofdvoeding connector (besluit v1)

| Prioriteit | Connector | Reden |
|---|---|---|
| **Primair** | **JST-VH 2-pin** (3,96 mm) of **schroefklem 2-pin 5,08 mm** | Hogere stroom, robuuster voor servo+LED |
| **Parallel** | Grote **solder pads** 5V + GND | Noodvoeding / dikke draden |
| **Secundair (optioneel)** | JST-XH 2-pin | Alleen met label *≤ ~2 A totaal* |

### 2.4 Condensatoren en bescherming

| Ref | Waarde | Plaats | Status |
|---|---|---|---|
| C_MAIN | 1000 µF / ≥10 V elco | bij J_MAIN | **Aanbevolen verplicht** |
| C_SERVO | 1000–2200 µF / ≥10 V elco | bij J_SERVO1/2 | **Aanbevolen verplicht** bij servo's |
| C_AHCT | 100 nF keramisch | direct bij U2 VCC–GND | **Verplicht** |
| C_LD / C_OLED | 100 nF | bij 4-pin headers | Optioneel |
| F_MAIN | PTC of fuse-link footprint | in 5V_MAIN | Optioneel |
| SJ_SERVO | 2-pad solder jumper | tussen 5V_MAIN en 5V_SERVO | **Verplicht footprint** |

### 2.5 Stroombudget (conservatief ontwerp)

| Last | Richtwaarde | Opmerking |
|---|---|---|
| ESP32-S3 + Wi-Fi | 100–500 mA piek | Via DevKit VIN |
| 3× LED data (AHCT) | &lt; 50 mA | Data-lijnen, geen LED-stroom via GPIO |
| WS2812/externe LED 5V | **User dependent** | Stroom via 5V_LED, niet via ESP32 |
| 2× servo | 500 mA–2 A **each peak** | Bepaalt MAIN connector keuze |
| LD2450 | ~150 mA typ. | 5V op sensor header |
| OLED + I2C | &lt; 50 mA | 3V3 van DevKit |

**Ontwerpdoel sporen:** 5V_MAIN / 5V_SERVO **≥ 1,0 mm** (1 oz) of equivalent copper pour; servo-GND even breed.

---

## 3. Functionele blokken

### 3.1 LED / data (×4: 3 actief + 1 AUX)

- **U2:** SN74AHCT125N (DIP-14), VCC = 5V, GND common.
- **~OE1–4:** pins **1, 4, 10, 13** → **GND** (outputs altijd enabled).
- Signaalpad: `ESP32 GPIO` → `AHCT Ax` → `AHCT Yx` → `Rx 330 Ω` → `J_LEDx DATA`.
- **GPIO:** OUT1=**18**, OUT2=**17**, OUT3=**21** (3× actieve buizen), OUT4/AUX=**12** (reserve).
- Alle vier kanalen naar **J_LED1..J_LED4** (JST-XH 3p).

### 3.2 Servo (×2)

- Voeding: **5V_SERVO** + **GND**; signaal: **PWM** van ESP32.
- **GPIO15** = SERVO1, **GPIO16** = SERVO2 (LEDC in firmware).
- Pinvolgorde JST: **GND | 5V | PWM** (pin 1 = GND).

### 3.3 HLK-LD2450

- 4-pin: **5V, GND, ESP_RX, ESP_TX** (silkscreen ook **LD_TX → ESP_RX**).
- UART: **UART1**, default mapping **GPIO10 = RX**, **GPIO11 = TX** (ESP-IDF `uart_set_pin`).
- **Niet** op GPIO43/44 (UART0 debug).

### 3.4 SH1106 OLED

- I2C: **SDA=GPIO8**, **SCL=GPIO9**.
- **J_OLED_EXT** 4-pin: GND, 3V3, SDA, SCL.
- **F_OLED** footprint: 1×4 of 1×4+1 pin header voor direct montage (0,96" OLED pin spacing controleren bij KiCad — typ. 2,54 mm).

### 3.5 Knoppen (×3)

- Active-low naar GND; firmware: `INPUT_PULLUP`.
- On-board tactile footprints + **J_BTN** 4-pin: GND | BTN1 | BTN2 | BTN3.
- GPIO: **1, 2, 42**.

### 3.6 EC11 rotary encoder

- On-board EC11 footprint + **J_ENC** 5-pin: GND | 3V3 | CLK | DT | SW.
- GPIO: **CLK=6**, **DT=7**, **SW=40**.
- Pull-ups: firmware internal; optionele **10 kΩ** footprints naar 3V3 (DNP default).

### 3.7 Optionele W5500 Ethernet (NOT POPULATED)

- **J_W5500** 8-pin JST-XH placeholder: **3V3 | GND | SPI_SCK | SPI_MOSI | SPI_MISO | ETH_CS | ETH_RST | ETH_INT**.
- **GPIO (v0.2):** SCK=**5**, MOSI=**13**, MISO=**14**, CS=**47**, RST=**4**, INT=**39**.
- Bedoeld voor **bedrade** W5500-module (geen SMD PHY op carrier v0.2).
- Silk/value: **W5500 OPTIONAL / NOT POPULATED** — geen module in BOM.
- Firmware: SPI host (bijv. SPI2); geen conflict met LED/LD2450/I2C/encoder/servo (zie pinout-tabel).

### 3.8 Overig

- **J_I2C** 4-pin (dup van OLED bus).
- **Proto:** min. 6×7 gaten 2,54 mm (layoutplan).
- **4× montagegat** M3 (3,2 mm drill) in hoeken.

---

## 4. GPIO-beleid (samenvatting)

| Categorie | GPIO | Actie |
|---|---|---|
| USB D± | 19, 20 | **Niet gebruiken** |
| UART0 debug | 43, 44 | **Niet gebruiken** |
| Octal flash/PSRAM (N16R8) | 35, 36, 37 | **Niet gebruiken** |
| Onboard RGB (DevKit v1.1) | 38 | **Niet gebruiken** |
| Strapping | 0, 3, 45, 46 | **Niet gebruiken** |
| DevKit LED (typ.) | 48 | **Niet gebruiken** |
| LED data | 18, 17, 21, 12 | Gebruikt (12 = AUX) |
| I2C | 8, 9 | Gebruikt |
| Servo PWM | 15, 16 | Gebruikt |
| LD2450 UART | 10, 11 | Gebruikt |
| Knoppen | 1, 2, 42 | Gebruikt |
| Encoder | 6, 7, 40 | Gebruikt |
| W5500 SPI (optioneel) | 5, 13, 14, 47, 4, 39 | J_W5500 — niet gemonteerd |

Volledige tabel: `hardware/pinout-table.md`.

---

## 5. PCB-eisen

| Eis | Waarde |
|---|---|
| Lagen | 2 (v1) |
| Dikte | 1,6 mm |
| Koper | 1 oz (overweeg 2 oz pour bij J_MAIN — optioneel v1.1) |
| Montage | Through-hole waar mogelijk; DIP-14, radial elco’s |
| Silkscreen | Pin1 vierkant; pinvolgorde **groot** per connector |
| Keep-out | USB-C DevKit + antenne-zone module — **pas na meting** |

Layout-detail: `hardware/pcb-layout-plan.md`.

---

## 6. Firmware-aannames (documentatie, geen code)

- LED: `RMT` of bit-bang op 18/17/21.
- Servo: LEDC 50 Hz op 15/16.
- LD2450: UART1 @ 256000 baud (datasheet HLK).
- OLED: I2C0, SH1106 128×64, adres 0x3C typ.
- Knoppen/encoder: debounce in software.

---

## 7. Acceptatie vóór productie (samenvatting)

Zie `docs/risk-checklist-pre-production.md`. Minimaal:

- [ ] Metingen ESP32 ingevuld
- [ ] Pinout continuity-test carrier ↔ DevKit
- [ ] Stroomconnector gekozen na lastenschatting
- [ ] ERC/DRC KiCad groen
- [ ] Prototype 1× handmatig getest per rail

---

## 8. Gerelateerde documenten

| Document | |
|---|---|
| Pinout | `hardware/pinout-table.md` |
| Connectors | `hardware/connector-list.md` |
| BOM | `hardware/bom.md` |
| Schema | `hardware/schematic-netlist.md` |
| Layout | `hardware/pcb-layout-plan.md` |
| Risico’s | `docs/risk-checklist-pre-production.md` |
| KiCad | `docs/kicad-next-steps.md` |
