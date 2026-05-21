# Featurelijst

Dit board wordt de standaard ESP32-basisprint voor lampen, LED-buizen, servo-objecten en sensoren.

## Wat zit erop? (v0.9)

- ESP32-S3 DevKit aansluiting (**footprint nog te meten**).
- Eén 5V-voedingsingang (JST-VH primair + optioneel XH + soldeerpads).
- Drie LED/data-uitgangen met **SN74AHCT125N** levelshifter (5 V).
- Twee servo-aansluitingen op **5V_SERVO** rail (solder jumper vanaf MAIN).
- HLK-LD2450 UART (GPIO10/11).
- SH1106 OLED I2C (GPIO8/9), direct of extern.
- Drie drukknoppen (on-board en/of 4-pin JST).
- EC11 rotary encoder (on-board en/of 5-pin JST).
- Extra GPIO (8-pin), I2C (4-pin), power pads, proto-vak 6×7.
- Vier M3 montagegaten.

## Modulair gebruik

- LED-only · servo-only · sensor-only · display/controller-only · volledig gecombineerd.
- Niet-gebruikte connectors hoeven niet gesoldeerd te worden (footprints blijven op PCB).

## Stekkers

- Signaal en lichte voeding: **JST-XH 2,54 mm** (2/3/4/5/8 polig).
- Hoofdvoeding: **JST-VH** of schroefklem (stroom).

Details: [hardware/connector-list.md](../hardware/connector-list.md)
