# ESP32 boardmetingen

## Status footprint

| Veld | Waarde |
|---|---|
| **KiCad / carrier** | `VOORLOPIG` — Espressif DevKitC-1 referentie |
| **Aanname** | diymore = zelfde maat als Espressif (Jeroen meet later ter verificatie) |
| **Definitief** | Pas na invullen kolom “Jouw meting” en bevestiging |

## Target board (gekozen)

| Item | Waarde |
|---|---|
| Merk | diymore |
| Type | ESP32-S3-DevKitC-1 N16R8 |
| Module | ESP32-S3-WROOM-1-N16R8 (verwacht) |
| Amazon | [B0F3XMYYQY](https://www.amazon.nl/-/en/diymore-DevKitC-1-S3-1-N16R8-development-connectable/dp/B0F3XMYYQY) |
| Mechanische referentie | [Espressif DevKitC-1 Dimensions (PDF)](https://dl.espressif.com/dl/PCB_ESP32-S3-DevKitC-1_V1_20210312CB.pdf) · [User guide v1.1](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32s3/esp32-s3-devkitc-1/user_guide_v1.1.html) |

---

## Werkwaarden v0.9 (Espressif = diymore, tot meting)

Gebruik deze waarden **voor KiCad-placeholder en carrier-layout**. Vervang door “Jouw meting” zodra gemeten.

| # | Meting | Werkwaarde (mm) | Bron | Jouw meting (mm) |
|---|---|---:|---|---|
| B1 | Pin pitch | **2,54** | Espressif | |
| B2 | Aantal pins per rij | **20** | Espressif | |
| B3 | Afstand hart-op-hart linker ↔ rechter pinrij | **22,86** | Espressif / standaard DevKitC-1 | |
| B4 | Lengte pinrij (pin1 → pin20 hart-op-hart) | **48,26** | 19 × 2,54 | |
| B5 | Totale PCB-lengte (zonder USB-uitsteek) | **52,50** | Espressif user guide / PCB outline | |
| B5b | Totale lengte incl. USB-zone (ref.) | **62,74** | Espressif PCB PDF (max. envelope) | |
| B6 | Totale PCB-breedte | **25,40** | Espressif | |
| B7 | Afstand pin1-rij tot dichtstbijzijnde boardrand | **TBD** | Meet later | |
| B8 | USB-C center tot boardrand (per poort) | **TBD** | Meet later (keep-out carrier) | |
| B9 | USB-C uitstek buiten PCB-plane | **TBD** | Meet later | |
| B10 | Hoogte totaal (header + module + USB) | **TBD** | Meet later | |
| B11 | Antenne keep-out lengte | **TBD** | Meet later | |
| B12 | Offset pin1 t.o.v. module centrum | optioneel | | |

### KiCad placeholder (samenvatting)

```text
2× PinHeader 1×20, pitch 2,54 mm
Rij-afstand (center-to-center): 22,86 mm
Pinrij-lengte: 48,26 mm
PCB envelope (DevKit): 25,40 × 52,50 mm
Reserveer extra lengte t.o.v. 62,74 mm voor USB-C keep-out tot B8/B9 gemeten zijn
```

---

## A. Module-identificatie

| Veld | Werkwaarde / aanname | Jouw meting / check |
|---|---|---|
| Datum meting | — (later) | |
| Module tekst | ESP32-S3-WROOM-1-N16R8 | |
| DevKit versie silkscreen | DevKitC-1 v1.1-achtig | |
| Aantal USB-C poorten | 2 | |
| USB-C posities | Espressif-layout (meet later) | |
| Onboard RGB LED (GPIO38) | ja (v1.1) | |
| Pin silkscreen = GPIO-nummer | ja (verwacht) | |

---

## C. Carrier planning (voorlopig)

| Veld | Werkwaarde |
|---|---|
| USB-kant op carrier-rand | Nog te kiezen na B8/B9 meting |
| Min. clearance USB plug | **12 mm** conservatief tot gemeten |
| Max. carrier board (v0.9) | **130 × 85 mm** |
| M3 gatpatroon | 4 hoeken, 3,2 mm boring (afstand na behuizing) |

---

## D. Elektrische sanity (na levering)

| Check | OK? |
|---|---|
| Continuity header “18” ↔ GPIO18 | ☐ |
| Pins 35–37 niet als GPIO gebruiken (N16R8) | ☐ |
| 5V en GND header niet kort | ☐ |

---

## E. Na definitieve meting

1. Vul kolom **Jouw meting** in; afwijkingen noteren.
2. Pas KiCad-footprint aan → status **DEFINITIEF**.
3. Update `docs/risk-checklist-pre-production.md` sectie A.
4. Bij afwijking &gt; 0,5 mm op B3/B5/B6: carrier-PCB footprint herzien vóór productie.

---

## Meetinstructies (werkplaats)

- Meet in **mm**, 0,1 mm nauwkeurigheid.
- **Hart-op-hart** voor pinafstanden.
- Foto’s: bovenaanzicht, USB-kant, onderkant headers.
- Vergelijk met werkwaarden-tabel hierboven; noteer delta.
