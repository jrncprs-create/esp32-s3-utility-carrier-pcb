# Chat project context: doel → uitvoering

Dit document bewaart de belangrijkste beslissingen uit de ChatGPT/Cursor-voorbereiding voor het project **ESP32-S3 Utility Carrier PCB v1**. Het is bedoeld als overdracht en contextanker naast de technische specificaties.

## 1. Aanleiding

Jeroen had een ESP32 netjes op een prepboard gesoldeerd zodat het robuuster werd en in een doosje gebruikt kon worden. Het werkte praktisch, maar miste nog nette vaste voorzieningen zoals levelshifter, connectors, sensorpoorten en betrouwbare voeding. De vraag was of er kant-en-klare lege ESP/USB/PCB-borden bestaan waarop je alles netjes op de juiste plek kunt solderen.

Na verkennen bleek dat universele ESP32 breakout/prototype boards bestaan, maar meestal niet precies passen bij Jeroens combinatie van LED-data, servo’s, LD2450, OLED, knoppen, encoder en modulaire toepassingen. Daarom is besloten om een eigen carrier-PCB te ontwerpen.

## 2. Hoofddoel

Ontwerp een **ESP32-S3 Utility Carrier PCB v1**: een soldeerbare basisprint voor kleine interactieve installaties.

De print moet bedoeld zijn voor:

- LED-buizen / addressable LED-data;
- kleine servo-objecten;
- mmWave/person-tracking sensor;
- display/menu/teststand;
- knoppen en draaiknop;
- snelle uitbreidingen en experimenten.

Het board moet niet één project oplossen, maar een praktische standaardbasis worden voor meerdere Jeroen-projecten.

## 3. Belangrijkste architectuurbesluit

Gebruik **geen losse ESP32-WROOM module** op de PCB.

Gebruik in plaats daarvan een bestaande **ESP32-S3 DevKit** als module op de carrier-PCB.

Reden:

- USB-C/programmeren blijft makkelijk;
- geen eigen USB-serial, boot/reset-circuit, regulator en antenne-layout nodig;
- ESP-board is vervangbaar;
- v1 blijft soldeerbaar en fouttoleranter.

Target board op dit moment:

- Amazon B0F3XMYYQY;
- vermoedelijk diymore ESP32-S3 DevKitC-1 N16R8 / ESP32-S3-WROOM-1-N16R8 clone;
- vergelijken met officiële Espressif ESP32-S3-DevKitC-1 v1.1 documentatie;
- clone-maten niet blind vertrouwen.

## 4. Modulaire werking

Het board moet kunnen werken als:

- LED-only controller;
- servo-only controller;
- sensor-only controller;
- display/menu-controller;
- volledige controller met LED + servo + sensor + OLED + knoppen + rotary encoder.

Niet geplaatste of ongebruikte secties mogen de rest niet blokkeren.

Voorbeelden:

- als servo’s niet geplaatst zijn, moet LED-only gewoon werken;
- als levelshifter/LED-sectie niet bestukt is, moet servo/sensor/display nog kunnen werken;
- als sensor niet geplaatst is, moet de rest werken;
- display/knoppen/encoder zijn handig, maar niet verplicht voor basiswerking.

## 5. Voeding

Besluit: standaard **5V**.

Jeroen wil liever geen losse servo-voedingsinput als standaard. Er komt dus één hoofdvoeding:

- `5V MAIN IN`.

Intern wordt die verdeeld naar:

- ESP32 VIN/5V;
- LED 5V outputs;
- 74AHCT125 levelshifter;
- LD2450 sensor;
- OLED/display;
- servo rail;
- extra 5V-pads.

Belangrijke nuance:

- één input betekent niet één dun spoor;
- intern moeten er duidelijke rails/banen zijn: `5V_LOGIC`, `5V_LED`, `5V_SERVO`, common GND;
- servo’s krijgen een stevige interne rail, dikke sporen en eigen condensator;
- er komt bij voorkeur een solder jumper/fuse-link tussen `5V_MAIN` en `5V_SERVO`, zodat servo-voeding later eventueel gescheiden kan worden.

Hoofdvoeding is kritisch. JST-XH kan te licht zijn als LED’s en servo’s samen veel stroom trekken. Voor `5V MAIN IN` is JST-VH, XT30, schroefterminal of extra power pads technisch veiliger. Voor signaal/kleine uitgangen blijft JST-XH de voorkeur.

## 6. Connectorstrategie

Jeroen wil het liefst overal dezelfde soort klikstekkers op het board, in 2-, 3-, 4- en 5-polig.

Eerste gedachte was JST-SM, maar technisch is geconcludeerd:

- JST-SM is meestal kabel-naar-kabel;
- voor PCB-montage is **JST-XH 2.54mm through-hole** praktischer en logischer;
- één connectorfamilie houdt het board overzichtelijk.

Besluit:

- zoveel mogelijk JST-XH 2.54mm through-hole PCB headers;
- 2-pin voor simpele voeding/knoppen;
- 3-pin voor LED/servo;
- 4-pin voor LD2450/OLED/I2C;
- 5-pin voor rotary encoder;
- alle pinvolgordes groot en duidelijk op silkscreen.

Uitzondering:

- `5V MAIN IN` mag afwijken als de stroom hoger is dan JST-XH veilig aankan.

## 7. LED/data

De print krijgt **3 levelshifted LED/data-uitgangen**.

Per uitgang:

- ESP32 GPIO → 74AHCT125 input;
- 74AHCT125 output → 330 Ω serieweerstand;
- weerstand → connector DATA.

Componenten:

- SN74AHCT125N / 74AHCT125 DIP-14, through-hole;
- geschikt voor IC-voetje;
- R_LED1/R_LED2/R_LED3 = 330 Ω;
- 100nF ontkoppeling dicht bij de 74AHCT125;
- alle ~OE-pinnen van de 74AHCT125 correct naar GND.

Belangrijk: als de OE-pinnen vergeten worden, doet de levelshifter niets.

## 8. Servo’s

De print krijgt **2 servo-uitgangen**.

Per servo:

- GND;
- 5V_SERVO;
- PWM.

Servo’s worden standaard gevoed vanuit `5V MAIN IN`, maar via een eigen interne servo-rail met dikke sporen en C_SERVO dichtbij de servoheaders.

Er moet rekening worden gehouden met servo-pieken: resets/storing op ESP32 voorkomen door goede voeding, GND en condensatorplaatsing.

## 9. Sensor

Na vergelijking tussen HLK-LD2450 en C4001 is gekozen voor:

- **JMT / Hi-Link HLK-LD2450 24GHz mmWave** als hoofdsensor.

Reden:

- Jeroen wil vaak niet alleen presence, maar ook waar iemand ongeveer is;
- LD2450 past beter bij target tracking, links/rechts, afstand/hoek en objectgedrag;
- geschikt voor lampjes/wezentjes/servo’s die iemand kunnen volgen of ruimtelijk reageren.

C4001 blijft interessant voor presence/microbeweging, maar niet als hoofdkeuze voor deze PCB.

Sensorpoort:

- JST-XH 4-pin;
- 5V;
- GND;
- ESP_RX;
- ESP_TX;
- duidelijk silkscreen: LD2450 TX → ESP_RX, LD2450 RX → ESP_TX.

De LD2450 wordt niet vast op de PCB geplaatst, maar via kabel, zodat hij gericht kan worden.

## 10. OLED-display

Display:

- **SH1106 I2C OLED**.

Er moeten twee opties zijn:

1. display direct op de PCB;
2. display extern in het doosje/frontpaneel via connector.

Standaard I2C:

- GND;
- 3V3;
- SDA;
- SCL.

Eventueel 5V als extra optionele pin op externe header, maar 3V3 blijft de veilige standaard.

Voorlopige I2C-pinnen:

- SDA = GPIO8;
- SCL = GPIO9;
- nog definitief controleren tegen gekozen ESP32-S3 board.

## 11. Knoppen en rotary encoder

Toevoegen:

- 3 momentary pushbuttons;
- EC11 rotary encoder met detents/klikjes en push switch.

Knoppen:

- GPIO naar GND;
- interne pull-ups in firmware als uitgangspunt;
- liefst zowel PCB-footprint als externe connectoroptie.

Rotary encoder:

- direct footprint op PCB;
- externe JST-XH 5-pin header voor montage in doosje/frontpaneel;
- GND, 3V3, CLK, DT, SW;
- geschikt voor menu, helderheid, modus, servo-test, sensorinstelling.

## 12. Extra just-in-case aansluitingen

Toevoegen voor flexibiliteit:

- extra GPIO header met minimaal 4 vrije GPIO’s + 3V3 + 5V + GND;
- extra I2C header;
- extra 5V / 3V3 / GND pads;
- klein proto-area met through-hole grid;
- 4 montagegaten;
- duidelijke silkscreen labels overal.

Niet te universeel maken: extra’s zijn handig, maar het board moet overzichtelijk en soldeervriendelijk blijven.

## 13. ESP32-footprint en meetstap

Dit is de belangrijkste open technische stap.

De pinout-afbeelding en Amazon-link zijn genoeg voor richting, maar niet voor productie. Voor een PCB moet de fysieke footprint kloppen.

Nog meten in de werkplaats:

- aantal pinnen per zijde;
- pin pitch;
- hart-op-hart afstand tussen pinrijen;
- totale lengte;
- totale breedte;
- afstand eerste pin tot USB-kant;
- USB-C positie/overhang;
- mechanische hoogte voor doosje;
- montage/ruimte rondom USB.

Zonder deze metingen mag geen definitieve carrier-footprint of Gerber gemaakt worden.

## 14. Risicopinnen / pinout-aandacht

Belangrijke waarschuwingen die uit de discussie kwamen:

- GPIO19/20 liever vrijhouden: USB D-/D+;
- GPIO43/44 liever vrijhouden voor UART0/debug;
- GPIO35/36/37 oppassen/vermijden bij N16R8/Octal PSRAM;
- GPIO0/3/45/46 oppassen vanwege boot/strapping/gevoelige functies;
- GPIO38/48 kunnen onboard LED/rgb-functies hebben;
- GPIO16 werd genoemd als mogelijk riskant bij sommige ESP32-S3 varianten en moet gecontroleerd worden.

LD2450 liever op andere UART-pinnen dan UART0 zodat debugging beschikbaar blijft.

## 15. Productieroute

Besluit:

### v1

- kale PCB laten maken;
- zelf solderen;
- doel: footprint, pinout, connectoren, voeding en praktische montage testen.

### Niet meteen doen

- geen PCBA/assembly voor v1;
- geen volledige kant-en-klare assembly zolang ontwerp niet bewezen is.

### Mogelijke leveranciers

- JLCPCB: goedkoop, snel, goede prototype-route;
- PCBWay: vergelijkbaar, iets meer service/maatwerk;
- Aisler: Europees/Duits, duurder, minder importgedoe;
- Eurocircuits: professioneel Europees, duurder;
- Conrad PCB-service: handige Europese uploadroute, controleren wat ze exact ondersteunen.

### Assembly pas later

PCBA/assembly pas overwegen bij v2/v3 of als:

- ontwerp bewezen is;
- meerdere identieke boards nodig zijn;
- solderen te veel tijd kost;
- componenten/connectoren definitief zijn;
- er meer SMD op komt.

## 16. Workflow met ChatGPT, Claude/Cursor en GitHub

Besloten workflow:

- ChatGPT bewaakt doel, architectuur, keuzes, risico’s en projectcontext;
- Claude/Cursor voert lange technische documenten en later KiCad-bestanden uit;
- GitHub wordt bron van waarheid;
- geen productie-output zonder meetdata en checks.

Cursor heeft inmiddels een repo opgezet:

- repository: `jrncprs-create/esp32-s3-utility-carrier-pcb`;
- branch: `main`;
- commit: `Initial PCB project briefing`;
- bevat documentatie en hardware-specificaties;
- geen Gerbers, geen KiCad-bestanden, geen productie-PCB.

## 17. Huidige status

Status na deze chat:

- doel bepaald;
- features bepaald;
- connectorstrategie bepaald;
- sensor gekozen;
- voedingstrategie bepaald;
- productieroute bepaald;
- Cursor/GitHub projectmap gemaakt;
- technische documentatie staat in GitHub;
- ESP32-footprint nog niet definitief;
- fysieke meting in werkplaats is de volgende harde stap.

## 18. Volgende veilige stap

Wanneer Jeroen weer in de werkplaats is:

1. ESP32-board meten met schuifmaat;
2. `hardware/measurements.md` invullen;
3. Cursor vragen om op basis daarvan een KiCad-skelet te maken;
4. schema/ERC en layout/DRC controleren;
5. footprint en connector-current controleren;
6. pas daarna Gerbers exporteren voor kale PCB v1.

Tot die tijd: geen footprint gokken en geen PCB bestellen.
