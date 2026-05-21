# Pinout notes (samenvatting)

Volledige tabel: **[hardware/pinout-table.md](pinout-table.md)**

## Toewijzing v0.9 phase 2

| Functie | GPIO |
|---|---|
| LED OUT 1–3 | 18, 17, 21 (via 74AHCT125; ch4 DNP) |
| I2C SDA / SCL | 8, 9 |
| LD2450 UART | 10 (RX), 11 (TX) |
| Servo PWM | 15, 16 |
| Knoppen (J_BTN) | 1, 2, 42 |
| Encoder (J_ENC) | 6, 7, 40 |
| W5500 SPI (optioneel) | 5, 13, 14, 47, 4, 39 |
| **Vrij** | **12** (geen LED4) |

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

- VCC = 5 V; **~OE → GND**; kanalen 1–3 actief; **kanaal 4 DNP/NC**.
- Zie [hardware/schematic-netlist.md](schematic-netlist.md).

## Footprint

**VOORLOPIG** (Espressif = diymore; meting later) — zie [hardware/measurements.md](measurements.md).
