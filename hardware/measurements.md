# ESP32 boardmetingen — meetformulier

**Status footprint:** `NIET DEFINITIEF`  
**Invullen door:** Jeroen (werkplaats)  
**Board:** diymore / Amazon clone — vergelijk met [DevKitC-1 v1.1](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32s3/esp32-s3-devkitc-1/user_guide_v1.1.html)

Amazon: https://www.amazon.nl/dp/B0F3XMYYQY

---

## Meetinstructies

- Meet in **mm** met schuifmaat, 0,1 mm nauwkeurigheid waar mogelijk.
- **Hart-op-hart** voor pinafstanden.
- Foto’s: bovenaanzicht, zijaanzicht USB-kant, onderkant headers.
- Noteer module marking (bijv. `ESP32-S3-WROOM-1-N16R8`).

---

## A. Module-identificatie

| Veld | Waarde (invullen) |
|---|---|
| Datum meting | |
| Module tekst | |
| DevKit versie silkscreen | |
| Aantal USB-C poorten | |
| USB-C posities (boven/onder/links/rechts t.o.v. headers) | |
| Onboard RGB LED aanwezig? (GPIO38) | ja / nee |
| Pin silkscreen = GPIO-nummer? | ja / nee / deels |

---

## B. Mechanisch (verplicht vóór KiCad footprint)

| # | Meting | Officiële Espressif ref. (niet blind gebruiken) | Jouw meting (mm) |
|---|---|---|---|
| B1 | Pin pitch | 2,54 | |
| B2 | Aantal pins per rij | 20 | |
| B3 | Afstand **hart-op-hart** linker ↔ rechter rij | ~18,0–23,0 (clone!) | |
| B4 | Lengte pinrij (pin1 → pin20 hart-op-hart) | 19×2,54 = 48,26 | |
| B5 | Totale PCB-lengte | ~52,5 | |
| B6 | Totale PCB-breedte | ~25,4 | |
| B7 | Afstand pin1-rij tot dichtstbijzijnde boardrand | | |
| B8 | Afstand USB-C center tot boardrand (elke USB) | | |
| B9 | USB-C connector uitstek buiten PCB-plane | | |
| B10 | Hoogte totaal (header + module + USB) | | |
| B11 | Antenne-zone lengte op PCB (keep-out) | | |
| B12 | Offset pin1 t.o.v. module centrum (optioneel) | | |

---

## C. Carrier planning (na B)

| Veld | Waarde |
|---|---|
| Gewenste USB-kant op carrier-rand | |
| Min. clearance USB plug in behuizing | |
| Max. carrier board X × Y (mm) | |
| M3 gat patroon (mm van hoek) | |

---

## D. Elektrische sanity (optioneel maar aanbevolen)

| Check | OK? |
|---|---|
| Continuity header “18” ↔ bekend GPIO18 testpunt | ☐ |
| Pins 35, 36, 37 **niet** gebruiken als GPIO (N16R8) | bevestigd ☐ |
| 5V en GND header niet kort | ☐ |

---

## E. Na invullen

1. Zet in KiCad footprint status → **DEFINITIEF** (alleen als B1–B10 compleet).
2. Update `hardware/pinout-table.md` als clone silkscreen afwijkt.
3. Doorloop `docs/risk-checklist-pre-production.md` sectie A.

**Espressif referentiewaarden** (alleen ter vergelijking): DevKitC-1 PCB ca. 25,4 × 52,5 mm, 2×20 @ 2,54 mm.
