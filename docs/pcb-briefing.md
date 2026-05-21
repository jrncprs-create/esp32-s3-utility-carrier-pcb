# Complete briefing voor Cursor / Claude

> **Status:** Oorspronkelijke briefing (archief). Uitgewerkte specificatie v0.9 staat in:
> [technical-specification.md](technical-specification.md),
> [briefing-review.md](briefing-review.md),
> en `hardware/` + `docs/risk-checklist-pre-production.md`.

We gaan een custom PCB ontwerpen: ESP32-S3 Utility Carrier v1.

## Doel

Maak een soldeerbare carrier-PCB voor een ESP32-S3 DevKit board met dubbele USB-C. Het board is bedoeld voor kleine interactieve installaties met LED-data, servo's, HLK-LD2450 mmWave sensor, SH1106 OLED-display, knoppen en een rotary encoder.

De gebruiker wil uiteindelijk alleen de onderdelen op de PCB solderen en daarna kabels met stekkers aansluiten. Hij wil niet zelf in KiCad werken.

## Belangrijk

- Maak nog GEEN definitieve Gerbers voor productie zonder controle.
- Lever eerst een volledige technische specificatie, pinout, schema-opzet, footprintlijst, BOM en KiCad-ontwerpplan.
- Gebruik through-hole onderdelen waar logisch/mogelijk.
- Ontwerp soldeervriendelijk, robuust en overzichtelijk.
- Geen losse ESP32-WROOM module ontwerpen.
- Gebruik een bestaande ESP32-S3 DevKit als plug-in/soldered module.
- USB-C van de ESP32 moet bereikbaar blijven aan de rand van de PCB.
- Het board moet modulair werken: LED-only, servo-only, sensor-only, display/controller-only of alles tegelijk.

## ESP32-board

Target board:
- diymore ESP32-S3 DevKitC-1 N16R8 / ESP32-S3-WROOM-1-N16R8 clone volgens Amazon-link van gebruiker.
- Vergelijk met officiële Espressif ESP32-S3-DevKitC-1 v1.1 documentatie.
- Gebruik twee lange header/footprint-rijen voor het ESP32-board.
- Controleer exact de pinout, pinvolgorde, pin pitch, boardbreedte en USB-C positie voordat er productie-output wordt gemaakt.
- Voor nu mag je op basis van de foto/pinout-afbeelding en Espressif DevKitC-1 v1.1 pinout een voorlopige pinout voorstellen.
- Vermijd conflicten met USB, bootstrapping pins en ongeschikte pins.
- Geef per gekozen GPIO aan of er risico's zijn.

## Connectorstrategie

De gebruiker wil zoveel mogelijk dezelfde soort klikstekkers op de PCB, in 2-, 3-, 4- en 5-polige varianten.

Gebruik bij voorkeur:
- JST-XH 2.54mm through-hole PCB headers, recht of haaks afhankelijk van de layout.
- Kies één connectorfamilie voor consistentie.
- Gebruik 2-pin, 3-pin, 4-pin en 5-pin JST-XH waar nodig.
- Alle connectoren moeten duidelijke silkscreen labels krijgen.
- Zet pinvolgorde groot en leesbaar op de PCB.

Let op:
- Als de gebruiker “JST-SM” zegt, bedoelt hij waarschijnlijk praktische JST-achtige klikstekkers.
- Voor PCB-montage is JST-XH waarschijnlijk beter dan JST-SM.
- Voor hoge stroom naar veel LEDs/servo's moet de stroomrating gecontroleerd worden.
- Als JST-XH voor 5V MAIN IN te licht is, geef dan een alternatief zoals JST-VH, XT30, schroefterminal of extra power pads. Maar behoud de voorkeur voor één nette connectorstijl waar mogelijk.

## Voeding

- Eén hoofdvoeding: 5V MAIN IN.
- Geen aparte verplichte servo-voeding.
- 5V MAIN IN voedt:
  - ESP32 VIN/5V
  - LED 5V outputs
  - 74AHCT125 levelshifter
  - LD2450 sensorpoort
  - SH1106 OLED/display
  - knoppen/encoder indien nodig
  - servo rail
- Intern wel aparte rails/banen maken:
  - 5V_LOGIC
  - 5V_LED
  - 5V_SERVO
  - common GND
- 5V_SERVO komt standaard vanaf 5V MAIN IN.
- Voeg een solder jumper / fuse-link optie toe tussen 5V_MAIN en 5V_SERVO, zodat servo-rail later eventueel gescheiden kan worden.
- Alle GND's gemeenschappelijk.
- Gebruik brede voedingsbanen of copper pours voor 5V en GND.
- Ontwerp conservatief voor servo-pieken en LED-stroom.
- Voeg extra power pads toe voor 5V, 3V3 en GND.

## Condensators / bescherming

Plaats vaste soldeerplekken voor:
- C_MAIN: 1000µF electrolytic over 5V/GND bij power input.
- C_SERVO: 1000-2200µF electrolytic bij servo-uitgangen.
- C_AHCT: 100nF decoupling dicht bij de 74AHCT125.
- Eventueel 100nF bij sensor/display headers.
- Markeer polariteit duidelijk op silkscreen.
- Overweeg footprint voor polyfuse of fuse-link in de main 5V rail.
- Geef aan welke onderdelen verplicht zijn en welke optioneel.

## LED/data

- 3 levelshifted LED/data-uitgangen.
- Gebruik SN74AHCT125N / 74AHCT125 DIP-14 footprint, through-hole, liefst geschikt voor IC-voetje.
- 74AHCT125 wordt gevoed met 5V.
- OE-pinnen moeten correct laag/actief worden gezet volgens datasheet.
- Per LED-output:
  ESP32 GPIO → 74AHCT125 input → 74AHCT125 output → 330Ω serieweerstand → connector DATA.
- Plaats vaste soldeerplekken voor:
  - R_LED1 = 330Ω
  - R_LED2 = 330Ω
  - R_LED3 = 330Ω
- LED-output connectors:
  - JST-XH 3-pin
  - pinnen: 5V / DATA / GND of 5V / GND / DATA
  - kies één vaste volgorde en zet die groot op silkscreen.
- Gebruik bij voorkeur GPIO18 als LED OUT 1 default.
- Kies logische veilige GPIO's voor LED OUT 2 en OUT 3.
- Voeg eventueel solder jumpers toe om LED OUT 2/3 later op andere GPIO's te zetten, maar maak het niet onnodig complex.

## Servo's

- 2 servo-uitgangen.
- Elke servo-uitgang via JST-XH 3-pin en/of standaard servoheader als alternatief.
- Pinout:
  - GND
  - 5V_SERVO
  - PWM
- Servo's worden standaard gevoed vanuit 5V MAIN IN via 5V_SERVO rail.
- Gebruik dikke 5V_SERVO en GND banen.
- Plaats C_SERVO dicht bij de servo-connectors.
- Kies twee veilige ESP32 GPIO's voor PWM.
- Voorstel mag GPIO15 en GPIO16 zijn, maar controleer op ESP32-S3 boot/strapping/USB-conflicten.
- Silkscreen duidelijk: SERVO1 en SERVO2 + GND/5V/PWM.

## Sensor

- Hoofdsensor: HLK-LD2450 24GHz mmWave.
- Sensor wordt niet vast op de PCB gesoldeerd; hij wordt via kabel aangesloten zodat hij gericht kan worden.
- Sensorpoort:
  - JST-XH 4-pin
  - 5V
  - GND
  - ESP_RX
  - ESP_TX
- Silkscreen duidelijk:
  - LD2450 TX → ESP_RX
  - LD2450 RX → ESP_TX
- Kies UART-pinnen die logisch zijn en niet conflicteren.
- Vermijd bij voorkeur UART0 RX/TX zodat debug beschikbaar blijft.
- Voeg optioneel een extra universele sensor/GPIO/I2C header toe voor later.

## Display

- Display: SH1106 I2C OLED.
- Ondersteun twee montage-opties:
  1. Direct-mount header/footprint op PCB.
  2. Externe OLED-header voor montage in doosje/frontpaneel.
- Gebruik JST-XH 4-pin of 5-pin voor externe OLED.
- Standaard OLED pinout:
  - GND
  - 3V3
  - SDA
  - SCL
- Eventueel 5V als extra optionele pin bij de externe header:
  - GND
  - 3V3
  - 5V
  - SDA
  - SCL
- Markeer 3V3 als standaard/veilig.
- Voeg extra I2C header toe:
  - GND
  - 3V3
  - SDA
  - SCL
- Voorstel I2C:
  - SDA = GPIO8
  - SCL = GPIO9
  Controleer of dit veilig is voor ESP32-S3 en het specifieke board.

## Knoppen

- 3 momentary pushbuttons:
  - BTN1
  - BTN2
  - BTN3
- Elke knop werkt als GPIO naar GND, met interne pull-up in firmware als uitgangspunt.
- Voorzie zowel:
  - footprint voor knop direct op PCB
  - connector/header optie voor externe knop in behuizing
- Externe knopconnectoren:
  - optie A: per knop JST-XH 2-pin: GND / BTNx
  - optie B: één JST-XH 4-pin: GND / BTN1 / BTN2 / BTN3
- Kies wat layout-technisch het handigst en netst is.
- Silkscreen duidelijk.

## Rotary encoder

- Ondersteun EC11 rotary encoder met detents/klikjes en push switch.
- Voorzie zowel:
  - footprint voor EC11 direct op PCB
  - externe connector voor montage in doosje/frontpaneel
- Externe connector:
  - JST-XH 5-pin
  - GND
  - 3V3
  - CLK
  - DT
  - SW
- Gebruik interne pull-ups in firmware als uitgangspunt, tenzij externe pull-ups duidelijk beter zijn.
- Kies veilige GPIO's voor CLK/DT/SW.
- Silkscreen duidelijk: ROTARY / CLK / DT / SW / GND / 3V3.

## Extra just-in-case

- Extra GPIO header met minimaal 4 vrije GPIO's + 3V3 + 5V + GND.
- Extra I2C header.
- Extra power pads:
  - 5V
  - 3V3
  - GND
- Klein proto-area met through-hole pad grid.
- 4 montagegaten.
- Duidelijke labels op de hele print.
- Markeer polariteit van condensators.
- Markeer connector pinouts consequent en groot.
- Reserveer ruimte rond connectoren zodat kabels en vingers erbij kunnen.

## Modulaire werking

Het board moet bruikbaar zijn als:
- LED-only controller
- servo-only controller
- sensor-only controller
- display/menu-controller
- volledige controller met LED + servo + sensor + OLED + knoppen + rotary encoder

Niet-geplaatste of ongebruikte secties mogen de rest niet blokkeren.

## PCB-layout eisen

- ESP32 centraal of iets links van midden.
- USB-C connectors van ESP32 aan boardrand bereikbaar.
- 5V MAIN IN aan één duidelijke rand.
- LED outputs gegroepeerd aan één rand.
- Servo outputs gegroepeerd.
- LD2450 sensorpoort aan een rand.
- OLED/controls bij voorkeur aan een rand of onderzijde, zodat frontpaneel/doosje logisch is.
- 4 montagegaten.
- Ruimte rond USB-connectors.
- Geen extreem kleine SMD-onderdelen tenzij echt nodig.
- Through-hole of grote footprints prefereren.
- Voedingssporen breed genoeg voor servo/LED-stroom.
- Gebruik copper pours voor GND en eventueel 5V waar logisch.
- Houd signaalsporen kort en overzichtelijk.
- Houd levelshifter dicht bij ESP32/LED-output routing.
- Houd C_AHCT dicht bij de 74AHCT125.
- Houd C_SERVO dicht bij servoheaders.
- Houd C_MAIN dicht bij 5V input.

## Gewenste output nu

Maak nog geen Gerbers.
Lever eerst:

1. Volledige technische specificatie.
2. Voorgestelde pinout-tabel met:
   - functie
   - ESP32 GPIO
   - connector/component
   - reden
   - risico/opmerking
3. BOM met:
   - component
   - waarde/type
   - footprint
   - verplicht/optioneel
4. Connectorlijst met:
   - connectornaam
   - aantal pinnen
   - voorgestelde JST-XH footprint
   - pinvolgorde
5. Schema/netlist in mensentaal.
6. PCB-layoutplan in tekst.
7. Checklist met risico's vóór productie.
8. Daarna pas voorstel voor KiCad-projectstructuur.
9. Lever volledige teksten/bestanden terug, geen losse snippets.

## Niet doen

- Geen artist impression.
- Geen “ongeveer goed” PCB als eindproduct.
- Geen definitieve Gerber zonder ERC/DRC/footprintcontrole.
- Geen losse ESP32-module-design.
- Geen SMD-only ontwerp.
- Geen meerdere verschillende connectorfamilies tenzij technisch nodig.
