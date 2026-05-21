# Pinout notes (samenvatting)

Volledige tabel: **[hardware/pinout-table.md](pinout-table.md)**

## Voorlopige toewijzing v0.9

| Functie | GPIO |
|---|---|
| LED OUT 1–3 | 18, 17, 21 (via 74AHCT125) |
| I2C SDA / SCL | 8, 9 |
| LD2450 UART | 10 (RX), 11 (TX) |
| Servo PWM | 15, 16 |
| Knoppen | 1, 2, 42 |
| Encoder CLK / DT / SW | 6, 7, 40 |
| Extra GPIO | 12, 13, 14, 47 |

## Vermijden (verboden op carrier)

| GPIO | Reden |
|---|---|
| 19, 20 | USB D-/D+ |
| 43, 44 | UART0 (USB-serial debug) |
| 35, 36, 37 | Octal flash/PSRAM (N16R8) |
| 38 | Onboard RGB (DevKitC-1 v1.1) |
| 0, 3, 45, 46 | Strapping |
| 48 | Onboard LED (typ. DevKit) |

## 74AHCT125

- VCC = 5 V; **~OE pins 1, 4, 10, 13 → GND**.
- Zie [hardware/schematic-netlist.md](schematic-netlist.md).

## Footprint

**VOORLOPIG** (Espressif = diymore; meting later) — zie [hardware/measurements.md](measurements.md).
