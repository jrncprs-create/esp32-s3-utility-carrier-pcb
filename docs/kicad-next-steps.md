# Volgende veilige stap richting KiCad

**Nu doen:** schema + placeholder PCB **zonder** bestellen van PCB’s.

---

## 1. Projectstructuur (aanmaken)

```text
kicad/
  esp32-s3-utility-carrier.kicad_pro
  esp32-s3-utility-carrier.kicad_sch
  esp32-s3-utility-carrier.kicad_pcb
  sym-lib-table
  fp-lib-table
  libraries/
    carrier.kicad_sym
    carrier.pretty/
```

---

## 2. Volgorde

| Stap | Actie | Blokkeerder |
|---|---|---|
| 1 | Symbolen: AHCT125, JST footprints, R, C, SJ | Geen |
| 2 | Sheet `power.sch`: J_MAIN, rails, C_MAIN, SJ_SERVO, C_SERVO | Connectorkeuze VH OK |
| 3 | Sheet `esp32_interface.sch`: **F_ESP als generic 2×20** met alleen gebruikte pins | Metingen |
| 4 | Sheets `led`, `servo`, `sensor`, `ui` per `schematic-netlist.md` | Geen |
| 5 | ERC op hele hierarchy | Pin conflicts |
| 6 | PCB: outline **tijdelijk** 90×65 mm + **TBD** ESP + USB keep-out | **measurements.md** |
| 7 | Place TH components per `pcb-layout-plan.md` | Geen |
| 8 | DRC met fab rules (JLC 6/6 mil default) | Geen |
| 9 | Export **PDF** 1:1 overlay met fysiek DevKit | Metingen |
| 10 | Pas **alleen** F_ESP en boardgrootte aan → markeer DEFINITIEF | Metingen groen |
| 11 | Herhaal ERC/DRC + risico-checklist | Alles groen |
| 12 | **Dan pas** Gerber export voor bestelling v1 prototype | User go |

---

## 3. Placeholder ESP32 footprint

- Gebruik **twee** `PinHeader_1x20_P2.54mm_Vertical` op afstand **`TBD_MM`** (officiële Espressif referentie ~25,4 mm boardbreedte, rij-afstand **nog meten** — vaak ~22,86 mm tussen rijen bij DevKitC, **niet blind overnemen**).
- Tekst op silk: `ESP32 FOOTPRINT NIET DEFINITIEF`.
- Teken **USB keep-out** rechthoek op Edge.Cuts.User of Dwgs.User.

---

## 4. Design rules (start)

| Regel | Waarde |
|---|---|
| Min track | 0,15 mm signaal |
| Min power | 0,4 mm (tijdelijk) → 1,0 mm voor 5V |
| Min clearance | 0,15 mm |
| Via drill | 0,3 mm |

---

## 5. Wat **niet** doen in KiCad v0.1

- Geen Gerber upload naar fab
- Geen “productie ready” title block
- Geen custom 3D model claim
- Geen routing onder antenne vóór meting

---

## 6. Referenties in repo

Koppel KiCad netlabels 1:1 aan `hardware/schematic-netlist.md` netnamen (`5V_MAIN`, `LED1_DATA`, …).
