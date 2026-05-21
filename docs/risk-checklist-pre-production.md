# Risico-checklist vóór productie

Gebruik deze lijst **vóór** bestellen van kale PCB’s of maken van Gerbers. Alles moet afgevinkt zijn of bewust geaccepteerd.

---

## A. Mechanisch / footprint

| # | Check | Status |
|---|---|---|
| A1 | Alle maten in `hardware/measurements.md` ingevuld op **echt** Amazon/DevKit board | ☐ |
| A2 | Afstand tussen pinrijen gemeten (hart-op-hart) | ☐ |
| A3 | USB-C positie en uitstek t.o.v. carrier-rand getekend | ☐ |
| A4 | ESP32-footprint in KiCad gemarkeerd **DEFINITIEF** (na A1–A3) | ☐ |
| A5 | Behuizing/paneel: hoogte module + USB + headers past | ☐ |
| A6 | Antenne keep-out zone vrij van copper (top + bottom) | ☐ |

---

## B. Elektrisch / pinout

| # | Check | Status |
|---|---|---|
| B1 | Geen carrier-verbinding naar GPIO19/20/35–38/43/44/0/3/45/46/48 | ☐ |
| B2 | Continuity: elke functie in `hardware/pinout-table.md` → juiste headerpin | ☐ |
| B3 | SN74AHCT125: VCC=5V, **alle ~OE naar GND** (1,4,10,13) | ☐ |
| B4 | LED-pad: GPIO → AHCT → 330Ω → DATA (geen bypass AHCT) | ☐ |
| B5 | LD2450: TX sensor → ESP_RX (GPIO10), RX sensor ← ESP_TX (GPIO11) | ☐ |
| B6 | I2C: GPIO8/9, pull-ups in firmware of DNP 10k geplaatst | ☐ |
| B7 | Servo PWM op GPIO15/16 zonder UART-conflict in test-firmware | ☐ |
| B8 | 3V3 belasting geschat &lt; 150 mA op peripherals | ☐ |

---

## C. Voeding / stroom

| # | Check | Status |
|---|---|---|
| C1 | Verwachte piekstroom installatie berekend (servo + LED + ESP) | ☐ |
| C2 | J_MAIN connector gekozen: **VH / schroefklem / XT30** indien &gt; ~2 A | ☐ |
| C3 | JST-XH op MAIN alleen met silkscreen limiet of niet geplaatst | ☐ |
| C4 | C_MAIN en C_SERVO aanwezig en juiste polariteit | ☐ |
| C5 | SJ_SERVO gedrag getest (open = geen 5V op servo JST) | ☐ |
| C6 | 5V sporen breedte ≥ ontwerp (1,0–1,2 mm of pour) | ☐ |
| C7 | GND geen lange dunne terugweg naar J_MAIN | ☐ |
| C8 | Geen 5V op 3V3 pin DevKit | ☐ |

---

## D. KiCad / fabricage

| # | Check | Status |
|---|---|---|
| D1 | ERC: geen errors (warnings beoordeeld) | ☐ |
| D2 | DRC: clearance, drill, courtyards OK voor gekozen fab | ☐ |
| D3 | Footprint namen = werkelijke onderdelen (JST pitch, elco pitch) | ☐ |
| D4 | Silkscreen pin1 + volgorde op **alle** connectoren | ☐ |
| D5 | BOM export gecontroleerd (geen verkeerde 74HC125) | ☐ |
| D6 | STEP of print PDF 1:1 met DevKit overlay (optioneel maar sterk aanbevolen) | ☐ |

---

## E. Prototype test (v1 handmatig)

| # | Test | Status |
|---|---|---|
| E1 | Alleen 5V in: geen kort, 5V op rails | ☐ |
| E2 | ESP32 boot + USB serial debug werkt (UART0 vrij) | ☐ |
| E3 | 1 LED DATA output oscilloscope/logic: ~5V high | ☐ |
| E4 | 1 servo beweegt zonder brown-out (met C_SERVO) | ☐ |
| E5 | LD2450 UART data (256000 baud) | ☐ |
| E6 | OLED I2C scan + display | ☐ |
| E7 | Knoppen + encoder debounce OK | ☐ |
| E8 | Warmte J_MAIN connector bij piek — acceptabel | ☐ |

---

## F. Proces / verwachting

| # | Check | Status |
|---|---|---|
| F1 | Geen “productie klaar” claim naar derden zonder E-sectie | ☐ |
| F2 | v1 = kale PCB; assembly pas v2/v3 | ☐ |
| F3 | Documentatieversie vastgelegd in README | ☐ |

---

## Risico-register (samenvatting)

| ID | Risico | Impact | Mitigatie |
|---|---|---|---|
| R1 | Clone footprint afwijkend | DevKit past niet / USB geblokkeerd | Metingen + geen Gerber tot groen |
| R2 | JST-XH MAIN te licht | Connector smelt / spanningsval | VH + brede sporen |
| R3 | N16R8 GPIO35–37 gebruikt | Chip crash / geen boot | Niet routen |
| R4 | UART0 bezet | Geen flash/debug | LD2450 op 10/11 |
| R5 | 3V3 overbelast | Brown-out OLED | Stroombudget + aparte PSU later |
| R6 | Verkeerde LD2450 TX/RX silk | Geen sensor data | Dubbele silk + test E5 |

**Go / No-Go productie:** alle **A**, **B**, **C**, **D** verplicht; **E** op eerste prototype vóór serie &gt; 3 stuks.
