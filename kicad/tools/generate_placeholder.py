#!/usr/bin/env python3
"""Generate KiCad placeholder project for ESP32-S3 Utility Carrier."""
from __future__ import annotations

import json
import re
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIBS = ROOT / "libraries"
PRETTY = LIBS / "carrier.pretty"
PROJECT = "esp32-s3-utility-carrier"
DOC_REV = "0.3-placeholder"

# PCB placeholder layout (mm). Origin = board lower-left; outline 0..BOARD_W × 0..BOARD_H.
BOARD_W = 90.0
BOARD_H = 65.0
BOARD_MARGIN = 2.0

# Approximate (width, height) from footprint pad-1 origin for bounds checks.
FOOTPRINT_EXTENTS: dict[str, tuple[float, float]] = {
    "carrier:JST_VH_1x02_Placeholder": (5.0, 2.5),
    "carrier:JST_XH_1x03_Placeholder": (5.0, 2.5),
    "carrier:JST_XH_1x04_Placeholder": (7.5, 2.5),
    "carrier:JST_XH_1x05_Placeholder": (10.0, 2.5),
    "carrier:JST_W5500_1x08_Placeholder": (17.5, 2.5),
    "carrier:F_ESP_2x20_Placeholder": (22.86, 50.8),
    "carrier:SolderJumper_2_Bridged": (3.0, 2.0),
    "Package_DIP:DIP-14_W7.62mm": (7.62, 19.0),
    "Capacitor_THT:CP_Radial_D5.0mm_P2.50mm": (5.0, 5.0),
    "Capacitor_THT:C_Disc_D3mm_W2mm_Horizontal": (3.5, 3.5),
    "Resistor_THT:R_AXIAL-0.4_D5.1mm_L12.0mm_Horizontal": (12.0, 3.5),
    "Button_Switch_THT:SW_PUSH_6mm": (6.0, 6.0),
    "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical": (7.5, 4.0),
}

# Canonical GPIO map (ESP32-S3 N16R8 / DevKitC-1) — single source for docs + KiCad labels.
PINOUT: dict[str, int] = {
    "LED1": 18,
    "LED2": 17,
    "LED3": 21,
    "LED4": 12,
    "I2C_SDA": 8,
    "I2C_SCL": 9,
    "LD_ESP_RX": 10,
    "LD_ESP_TX": 11,
    "SERVO1_PWM": 15,
    "SERVO2_PWM": 16,
    "BTN1": 1,
    "BTN2": 2,
    "BTN3": 42,
    "ENC_CLK": 6,
    "ENC_DT": 7,
    "ENC_SW": 40,
    "SPI_SCK": 5,
    "SPI_MOSI": 13,
    "SPI_MISO": 14,
    "ETH_CS": 47,
    "ETH_RST": 4,
    "ETH_INT": 39,
}

FORBIDDEN_GPIO = frozenset({0, 3, 19, 20, 35, 36, 37, 38, 43, 44, 45, 46, 48})


def uid() -> str:
    return str(uuid.uuid4())


def s(*parts: str) -> str:
    return "\n".join(parts)


def pin_orientation(x: float, y: float) -> int:
    """KiCad pin graphic orientation in degrees (0=right, 90=up, 180=left, 270=down)."""
    if x <= -5.0:
        return 180
    if x >= 5.0:
        return 0
    if y > 0:
        return 90
    if y < 0:
        return 270
    return 0


def pin_at(x: float, y: float) -> str:
    return f"(at {x} {y} {pin_orientation(x, y)})"


# Match (at X Y) on pin lines only — not (at X Y Z) already complete.
_PIN_AT_TWO_RE = re.compile(
    r"(\(pin [^\n]*?)\(at (-?[0-9.]+) (-?[0-9.]+)\)(?! *-?[0-9.])( \(length)"
)


def fix_pin_orientations(text: str) -> str:
    def repl(m: re.Match[str]) -> str:
        x, y = float(m.group(2)), float(m.group(3))
        return f"{m.group(1)}{pin_at(x, y)}{m.group(4)}"

    return _PIN_AT_TWO_RE.sub(repl, text)


# --- Custom symbol library ---
def write_carrier_sym() -> None:
    # SN74AHCT125N DIP-14 + F_ESP placeholder (used GPIO pins only)
    content = f"""(kicad_symbol_lib
  (version 20231120)
  (generator "generate_placeholder.py")
  (symbol "SN74AHCT125N"
    (pin_names (offset 0.254))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 11.43 0) (effects (font (size 1.27 1.27))))
    (property "Value" "SN74AHCT125N" (at 0 10.16 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DIP:DIP-14_W7.62mm" (at 0 -13.97 0)
      (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "https://www.ti.com/product/SN74AHCT125" (at 0 -15.24 0)
      (effects (font (size 1.27 1.27)) hide))
    (symbol "SN74AHCT125N_0_1"
      (rectangle (start -12.7 7.62) (end 12.7 -7.62)
        (stroke (width 0.254) (type default))
        (fill (type background))
      )
    )
    (symbol "SN74AHCT125N_1_1"
      (pin input line (at -15.24 5.08) (length 2.54) (name "1~OE" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
      (pin input line (at -15.24 2.54) (length 2.54) (name "1A" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
      (pin output line (at 15.24 5.08) (length 2.54) (name "1Y" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
      (pin input line (at -15.24 0) (length 2.54) (name "2~OE" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
      (pin input line (at -15.24 -2.54) (length 2.54) (name "2A" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
      (pin output line (at 15.24 2.54) (length 2.54) (name "2Y" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
      (pin power_in line (at 0 -10.16) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27))))
        (alternate "GND" passive line)
      )
      (pin output line (at 15.24 0) (length 2.54) (name "3Y" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
      (pin input line (at -15.24 -5.08) (length 2.54) (name "3A" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
      (pin input line (at -15.24 -7.62) (length 2.54) (name "4~OE" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
      (pin input line (at -15.24 -10.16) (length 2.54) (name "4A" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
      (pin output line (at 15.24 -2.54) (length 2.54) (name "4Y" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
      (pin input line (at -15.24 7.62) (length 2.54) (name "3~OE" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
      (pin power_in line (at 0 10.16) (length 2.54) (name "VCC" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27))))
        (alternate "VCC" passive line)
      )
    )
  )
  (symbol "F_ESP"
    (pin_names (offset 0.254))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "F_ESP" (at 0 35.56 0) (effects (font (size 1.27 1.27))))
    (property "Value" "ESP32-S3 DevKit 2x20 PLACEHOLDER" (at 0 33.02 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "carrier:F_ESP_2x20_Placeholder" (at 0 -35.56 0)
      (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 -38.1 0) (effects (font (size 1.27 1.27)) hide))
    (property "ki_description" "2x20 DevKitC-1 placeholder - NOT FINAL" (at 0 -40.64 0)
      (effects (font (size 1.27 1.27)) hide))
    (symbol "F_ESP_0_1"
      (rectangle (start -15.24 31.75) (end 15.24 -31.75)
        (stroke (width 0.254) (type default))
        (fill (type background))
      )
      (text "ESP32-S3 DevKit" (at 0 27.94 0) (effects (font (size 1.27 1.27))))
      (text "2x20 PLACEHOLDER" (at 0 25.4 0) (effects (font (size 1.016 1.016))))
    )
    (symbol "F_ESP_1_1"
      (pin bidirectional line (at -17.78 22.86) (length 2.54) (name "GPIO18" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at -17.78 20.32) (length 2.54) (name "GPIO17" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at -17.78 17.78) (length 2.54) (name "GPIO21" (effects (font (size 1.016 1.016)))) (number "21" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at -17.78 15.24) (length 2.54) (name "GPIO12" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at -17.78 12.7) (length 2.54) (name "GPIO8" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at -17.78 10.16) (length 2.54) (name "GPIO9" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at -17.78 7.62) (length 2.54) (name "GPIO10" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at -17.78 5.08) (length 2.54) (name "GPIO11" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at -17.78 2.54) (length 2.54) (name "GPIO15" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at -17.78 0) (length 2.54) (name "GPIO16" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at -17.78 -2.54) (length 2.54) (name "GPIO6" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at -17.78 -5.08) (length 2.54) (name "GPIO7" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at -17.78 -7.62) (length 2.54) (name "GPIO40" (effects (font (size 1.016 1.016)))) (number "40" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at 17.78 22.86) (length 2.54) (name "GPIO1" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at 17.78 20.32) (length 2.54) (name "GPIO2" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at 17.78 17.78) (length 2.54) (name "GPIO42" (effects (font (size 1.016 1.016)))) (number "42" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at 17.78 15.24) (length 2.54) (name "GPIO4" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at 17.78 12.7) (length 2.54) (name "GPIO5" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at 17.78 10.16) (length 2.54) (name "GPIO13" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at 17.78 7.62) (length 2.54) (name "GPIO14" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at 17.78 5.08) (length 2.54) (name "GPIO47" (effects (font (size 1.016 1.016)))) (number "47" (effects (font (size 1.016 1.016)))))
      (pin bidirectional line (at 17.78 2.54) (length 2.54) (name "GPIO39" (effects (font (size 1.016 1.016)))) (number "39" (effects (font (size 1.016 1.016)))))
      (pin power_in line (at 17.78 0) (length 2.54) (name "5V" (effects (font (size 1.016 1.016)))) (number "5V" (effects (font (size 1.016 1.016)))))
      (pin power_in line (at 17.78 -2.54) (length 2.54) (name "5V2" (effects (font (size 1.016 1.016)))) (number "5V2" (effects (font (size 1.016 1.016)))))
      (pin power_in line (at 17.78 -5.08) (length 2.54) (name "3V3" (effects (font (size 1.016 1.016)))) (number "3V3" (effects (font (size 1.016 1.016)))))
      (pin power_in line (at 17.78 -7.62) (length 2.54) (name "3V32" (effects (font (size 1.016 1.016)))) (number "3V32" (effects (font (size 1.016 1.016)))))
      (pin power_in line (at 17.78 -10.16) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "GND" (effects (font (size 1.016 1.016)))))
      (pin power_in line (at 17.78 -12.7) (length 2.54) (name "GND2" (effects (font (size 1.016 1.016)))) (number "GND2" (effects (font (size 1.016 1.016)))))
      (pin power_in line (at 17.78 -15.24) (length 2.54) (name "GND3" (effects (font (size 1.016 1.016)))) (number "GND3" (effects (font (size 1.016 1.016)))))
      (pin power_in line (at 17.78 -17.78) (length 2.54) (name "GND4" (effects (font (size 1.016 1.016)))) (number "GND4" (effects (font (size 1.016 1.016)))))
    )
  )
  (symbol "SJ_SERVO"
    (pin_names (offset 0.254))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "SJ" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
    (property "Value" "SJ_SERVO" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "carrier:SolderJumper_2_Bridged" (at 0 -5.08 0)
      (effects (font (size 1.27 1.27)) hide))
    (symbol "SJ_SERVO_0_1"
      (rectangle (start -5.08 2.54) (end 5.08 -2.54)
        (stroke (width 0.254) (type default))
        (fill (type background))
      )
    )
    (symbol "SJ_SERVO_1_1"
      (pin passive line (at -7.62 0) (length 2.54) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
      (pin passive line (at 7.62 0) (length 2.54) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
  )
)
"""
    (LIBS / "carrier.kicad_sym").write_text(fix_pin_orientations(content), encoding="utf-8")


def write_footprints() -> None:
    PRETTY.mkdir(parents=True, exist_ok=True)

    def fp(name: str, body: str) -> None:
        (PRETTY / f"{name}.kicad_mod").write_text(
            f'(footprint "{name}" (version 20240108) (generator "generate_placeholder.py")\n{body}\n)',
            encoding="utf-8",
        )

    # Generate F_ESP footprint with all 40 pads
    lines = [
        '(footprint "F_ESP_2x20_Placeholder" (version 20240108) (generator "generate_placeholder.py")',
        '  (descr "ESP32 DevKit 2x20 - row spacing 22.86mm - NOT FINAL")',
        '  (tags "ESP32 DevKit")',
        "  (attr through_hole)",
        '  (fp_text reference "F_ESP" (at 11.43 -4) (layer "F.SilkS")',
        '    (effects (font (size 1 1) (thickness 0.15))))',
        '  (fp_text value "F_ESP_2x20" (at 11.43 52) (layer "F.Fab") hide)',
        '  (fp_text user "ESP32 FOOTPRINT NIET DEFINITIEF" (at 11.43 50) (layer "F.SilkS")',
        '    (effects (font (size 0.9 0.9) (thickness 0.15))))',
        '  (fp_text user "NIET BESTELLEN ZONDER METINGEN" (at 11.43 47.5) (layer "F.SilkS")',
        '    (effects (font (size 0.8 0.8) (thickness 0.12))))',
    ]
    for i in range(20):
        y = i * 2.54
        num = i + 1
        shape = "rect" if num == 1 else "circle"
        lines.append(
            f'  (pad "{num}" thru_hole {shape} (at 0 {y}) (size 1.7 1.7) (drill 1.0) '
            f'(layers "*.Cu" "*.Mask") (pinfunction "{num}") (pintype "passive"))'
        )
    for i in range(20):
        y = i * 2.54
        num = i + 21
        shape = "rect" if num == 21 else "circle"
        lines.append(
            f'  (pad "{num}" thru_hole {shape} (at 22.86 {y}) (size 1.7 1.7) (drill 1.0) '
            f'(layers "*.Cu" "*.Mask") (pinfunction "{num}") (pintype "passive"))'
        )
    lines.append(")")
    (PRETTY / "F_ESP_2x20_Placeholder.kicad_mod").write_text("\n".join(lines) + "\n", encoding="utf-8")

    fp(
        "SolderJumper_2_Bridged",
        """
  (descr "Solder jumper 2-pad bridged default")
  (tags "solder jumper")
  (attr smd)
  (fp_text reference "SJ" (at 0 -2) (layer "F.SilkS"))
  (fp_text value "SJ_SERVO" (at 0 2) (layer "F.Fab") hide)
  (pad "1" smd roundrect (at -1.5 0) (size 1.5 1.2) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25))
  (pad "2" smd roundrect (at 1.5 0) (size 1.5 1.2) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25))
  (fp_line (start -0.3 0) (end 0.3 0) (stroke (width 0.2) (type default)) (layer "F.Cu"))
""",
    )

    fp(
        "JST_XH_1x03_Placeholder",
        """
  (descr "JST-XH 3p placeholder 2.50mm pitch")
  (tags "JST XH")
  (attr through_hole)
  (fp_text reference "J" (at 2.5 -3) (layer "F.SilkS"))
  (fp_text value "JST_XH_3" (at 2.5 3) (layer "F.Fab") hide)
  (pad "1" thru_hole rect (at 0 0) (size 1.8 1.8) (drill 1.1) (layers "*.Cu" "*.Mask"))
  (pad "2" thru_hole oval (at 2.5 0) (size 1.8 1.8) (drill 1.1) (layers "*.Cu" "*.Mask"))
  (pad "3" thru_hole oval (at 5.0 0) (size 1.8 1.8) (drill 1.1) (layers "*.Cu" "*.Mask"))
""",
    )

    fp(
        "JST_W5500_1x08_Placeholder",
        """
  (descr "W5500 module 8p - OPTIONAL NOT POPULATED")
  (tags "W5500 Ethernet")
  (attr through_hole)
  (fp_text reference "J_W5500" (at 8.75 -4) (layer "F.SilkS"))
  (fp_text value "W5500_OPT_NP" (at 8.75 4) (layer "F.Fab") hide)
  (fp_text user "W5500 OPTIONAL" (at 8.75 -2.5) (layer "F.SilkS")
    (effects (font (size 0.8 0.8) (thickness 0.12))))
  (fp_text user "NOT POPULATED" (at 8.75 2.5) (layer "F.SilkS")
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (pad "1" thru_hole rect (at 0 0) (size 1.8 1.8) (drill 1.1) (layers "*.Cu" "*.Mask"))
  (pad "2" thru_hole oval (at 2.5 0) (size 1.8 1.8) (drill 1.1) (layers "*.Cu" "*.Mask"))
  (pad "3" thru_hole oval (at 5.0 0) (size 1.8 1.8) (drill 1.1) (layers "*.Cu" "*.Mask"))
  (pad "4" thru_hole oval (at 7.5 0) (size 1.8 1.8) (drill 1.1) (layers "*.Cu" "*.Mask"))
  (pad "5" thru_hole oval (at 10.0 0) (size 1.8 1.8) (drill 1.1) (layers "*.Cu" "*.Mask"))
  (pad "6" thru_hole oval (at 12.5 0) (size 1.8 1.8) (drill 1.1) (layers "*.Cu" "*.Mask"))
  (pad "7" thru_hole oval (at 15.0 0) (size 1.8 1.8) (drill 1.1) (layers "*.Cu" "*.Mask"))
  (pad "8" thru_hole oval (at 17.5 0) (size 1.8 1.8) (drill 1.1) (layers "*.Cu" "*.Mask"))
""",
    )

    for n in (2, 4, 5, 8):
        pads = []
        pitch = 2.5
        for i in range(n):
            pads.append(
                f'  (pad "{i+1}" thru_hole {"rect" if i==0 else "oval"} (at {i*pitch} 0) '
                f'(size 1.8 1.8) (drill 1.1) (layers "*.Cu" "*.Mask"))'
            )
        fp(
            f"JST_XH_1x0{n}_Placeholder",
            f"""
  (descr "JST-XH {n}p placeholder")
  (tags "JST XH")
  (attr through_hole)
  (fp_text reference "J" (at {((n-1)*pitch)/2} -3) (layer "F.SilkS"))
  (fp_text value "JST_XH_{n}" (at {((n-1)*pitch)/2} 3) (layer "F.Fab") hide)
{chr(10).join(pads)}
""",
        )

    fp(
        "JST_VH_1x02_Placeholder",
        """
  (descr "JST-VH 2p main power placeholder 3.96mm pitch")
  (tags "JST VH power")
  (attr through_hole)
  (fp_text reference "J_MAIN" (at 1.98 -4) (layer "F.SilkS"))
  (fp_text value "5V_MAIN" (at 1.98 4) (layer "F.Fab") hide)
  (pad "1" thru_hole rect (at 0 0) (size 2.0 2.0) (drill 1.2) (layers "*.Cu" "*.Mask"))
  (pad "2" thru_hole oval (at 3.96 0) (size 2.0 2.0) (drill 1.2) (layers "*.Cu" "*.Mask"))
""",
    )


def write_lib_tables() -> None:
    (ROOT / "sym-lib-table").write_text(
        """(sym_lib_table
  (version 7)
  (lib (name "carrier")(type "KiCad")(uri "${KICAD9_SYMBOL_DIR}/../libraries/carrier.kicad_sym")(options "")(descr "Carrier symbols"))
  (lib (name "carrier-local")(type "KiCad")(uri "${KIPRJMOD}/libraries/carrier.kicad_sym")(options "")(descr "Carrier local"))
)
""".replace(
            "${KIPRJMOD}/libraries/carrier.kicad_sym", "${KIPRJMOD}/libraries/carrier.kicad_sym"
        ),
        encoding="utf-8",
    )
    # Fix sym table - only project relative
    (ROOT / "sym-lib-table").write_text(
        """(sym_lib_table
  (version 7)
  (lib (name "carrier")(type "KiCad")(uri "${KIPRJMOD}/libraries/carrier.kicad_sym")(options "")(descr "Carrier placeholder symbols"))
)
""",
        encoding="utf-8",
    )
    (ROOT / "fp-lib-table").write_text(
        """(fp_lib_table
  (version 7)
  (lib (name "carrier")(type "KiCad")(uri "${KIPRJMOD}/libraries/carrier.pretty")(options "")(descr "Carrier placeholder footprints"))
)
""",
        encoding="utf-8",
    )


def write_project() -> None:
    pro = {
        "board": {
            "design_settings": {
                "defaults": {
                    "board_outline_line_width": 0.1,
                    "copper_line_width": 0.2,
                    "copper_text_size_h": 1.5,
                    "copper_text_size_v": 1.5,
                    "copper_text_thickness": 0.3,
                    "other_line_width": 0.15,
                    "silk_line_width": 0.15,
                    "silk_text_size_h": 1.0,
                    "silk_text_size_v": 1.0,
                    "silk_text_thickness": 0.15,
                },
                "diff_pair_dimensions": [],
                "drc_exclusions": [],
                "meta": {"version": 2},
                "rule_severities": {},
                "track_widths": [0.25, 0.5, 1.0, 1.2],
                "via_dimensions": [],
            },
            "ipc2581": {"dist": "", "distpn": "", "internal_id": "", "mfg": "", "mpn": ""},
            "layer_presets": [],
            "viewports": [],
        },
        "boards": [],
        "cvpcb": {"equivalence_files": []},
        "erc": {
            "erc_exclusions": [],
            "meta": {"version": 0},
            "pin_map": [
                [1, 4, 2, 3, 0],
                [1, 4, 2, 3, 0],
                [1, 4, 2, 3, 0],
                [1, 4, 2, 3, 0],
                [1, 4, 2, 3, 0],
                [1, 4, 2, 3, 0],
                [1, 4, 2, 3, 0],
                [1, 4, 2, 3, 0],
            ],
            "rule_severities": {},
        },
        "libraries": {
            "pinned_footprint_libs": [],
            "pinned_symbol_libs": [],
        },
        "meta": {"filename": f"{PROJECT}.kicad_pro", "version": 3},
        "net_settings": {
            "classes": [
                {
                    "bus_width": 12,
                    "clearance": 0.15,
                    "diff_pair_gap": 0.25,
                    "diff_pair_via_gap": 0.25,
                    "diff_pair_width": 0.2,
                    "line_style": 0,
                    "microvia_diameter": 0.3,
                    "microvia_drill": 0.1,
                    "name": "Default",
                    "pcb_color": "rgba(0, 0, 0, 0.000)",
                    "priority": 2147483647,
                    "schematic_color": "rgba(0, 0, 0, 0.000)",
                    "track_width": 0.25,
                    "via_diameter": 0.6,
                    "via_drill": 0.3,
                    "wire_width": 6,
                },
                {
                    "clearance": 0.15,
                    "line_style": 0,
                    "name": "Power",
                    "priority": 0,
                    "track_width": 1.0,
                    "via_diameter": 0.8,
                    "via_drill": 0.4,
                    "wire_width": 6,
                },
            ],
            "meta": {"version": 4},
            "netclass_assignments": None,
            "netclass_patterns": [],
        },
        "pcbnew": {
            "last_paths": {
                "gencad": "",
                "idf": "",
                "netlist": "",
                "plot": "",
                "pos_files": "",
                "specctra_dsn": "",
                "step": "",
                "svg": "",
                "vrml": "",
            },
            "page_layout_descr_file": "",
        },
        "schematic": {
            "legacy_lib_dir": "",
            "legacy_lib_list": [],
        },
        "sheets": [["root", f"{PROJECT}.kicad_sch"]],
        "text_variables": {
            "PROJECT": "ESP32-S3 Utility Carrier v1",
            "STATUS": "v0.2 PLACEHOLDER - NOT FOR PRODUCTION",
        },
    }
    (ROOT / f"{PROJECT}.kicad_pro").write_text(json.dumps(pro, indent=2) + "\n", encoding="utf-8")


class SchBuilder:
    def __init__(self) -> None:
        self.lib_symbols: dict[str, str] = {}
        self.items: list[str] = []
        self.x = 0
        self.y = 0
        self.root_uuid = uid()

    def add_lib_symbol_device_r(self) -> None:
        if "Device:R" in self.lib_symbols:
            return
        self.lib_symbols["Device:R"] = """
  (symbol "Device:R"
    (pin_numbers hide) (pin_names (offset 0)) (exclude_from_sim no) (in_bom yes) (on_board yes)
    (property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
    (property "Value" "R" (at 0 0 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at -1.778 0 90) (effects (font (size 1.27 1.27)) hide))
    (symbol "R_0_1" (rectangle (start -1.016 -2.54) (end 1.016 2.54) (stroke (width 0.2032) (type default)) (fill (type none))))
    (symbol "R_1_1"
      (pin passive line (at 0 3.81 90) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
      (pin passive line (at 0 -3.81 270) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
  )"""

    def sym(
        self,
        lib_id: str,
        ref: str,
        value: str,
        at_x: float,
        at_y: float,
        footprint: str = "",
        unit: int = 1,
    ) -> tuple[float, float]:
        u = uid()
        fp_prop = ""
        if footprint:
            fp_prop = f"""
    (property "Footprint" "{footprint}" (at {at_x} {at_y} 0)
      (effects (font (size 1.27 1.27)) hide))"""
        self.items.append(
            f"""
  (symbol (lib_id "{lib_id}") (at {at_x} {at_y} 0) (unit {unit})
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no) (fields_autoplaced)
    (uuid {u})
    (property "Reference" "{ref}" (at {at_x} {at_y - 2.54} 0)
      (effects (font (size 1.27 1.27))))
    (property "Value" "{value}" (at {at_x} {at_y + 2.54} 0)
      (effects (font (size 1.27 1.27)))){fp_prop}
  )"""
        )
        return at_x, at_y

    def glabel(self, name: str, x: float, y: float, rot: int = 0) -> None:
        shape = "output" if rot == 0 else "input"
        self.items.append(
            f"""
  (global_label "{name}" (shape {shape}) (at {x} {y} {rot}) (fields_autoplaced)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid {uid()})
  )"""
        )

    def wire(self, x1: float, y1: float, x2: float, y2: float) -> None:
        self.items.append(
            f"  (wire (pts (xy {x1} {y1}) (xy {x2} {y2}))\n"
            f"    (stroke (width 0) (type default))\n"
            f"    (uuid {uid()})\n  )"
        )

    def build(self) -> str:
        lib_body = "\n".join(self.lib_symbols.values())
        # KiCad section order: lib_symbols, then sheet content (symbols/wires/labels), sheet_instances last.
        return f"""(kicad_sch (version 20231120) (generator "generate_placeholder.py")
  (uuid {self.root_uuid})
  (paper "A3")
  (title_block
    (title "ESP32-S3 Utility Carrier v1")
    (date "2026-05-21")
    (rev "{DOC_REV}")
    (comment 1 "NOT FOR PRODUCTION - ESP footprint NOT FINAL")
    (comment 2 "See hardware/measurements.md before ordering PCB")
  )
  (lib_symbols
{lib_body}
  )
{"".join(self.items)}
  (sheet_instances
    (path "/{self.root_uuid}" (page "1"))
  )
)
"""


def _conn_sym(name: str, pins: int) -> str:
    pads = []
    for i in range(pins):
        y = (i - (pins - 1) / 2) * 2.54
        pads.append(
            f"      (pin passive line {pin_at(-5.08, y)} (length 2.54) (name \"{i + 1}\" "
            f"(effects (font (size 1.27 1.27)))) (number \"{i + 1}\" (effects (font (size 1.27 1.27)))))"
        )
    return f"""
  (symbol "Connector:{name}"
    (pin_names (offset 1.016) hide) (pin_numbers hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
    (property "Reference" "J" (at 0 0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "{name}" (at 0 0 0) (effects (font (size 1.27 1.27))))
    (symbol "{name}_0_1"
      (rectangle (start -5.08 {(pins-1)*1.27}) (end 0 {-(pins-1)*1.27})
        (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "{name}_1_1"
{chr(10).join(pads)}
    )
  )"""


def write_schematic() -> None:
    b = SchBuilder()
    # Embed minimal lib copies for power + connector used on sheet
    b.lib_symbols["power:GND"] = """
  (symbol "power:GND" (power) (pin_names (offset 0)) (in_bom yes) (on_board yes)
    (property "Reference" "#PWR" (at 0 -6.35 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
    (symbol "GND_0_1" (polyline (pts (xy 0 0) (xy 0 -1.27) (xy 1.27 -1.27) (xy 0 -2.54) (xy -1.27 -1.27) (xy 0 -1.27))
      (stroke (width 0) (type default)) (fill (type none))))
    (symbol "GND_1_1" (pin power_in line (at 0 0 0) (length 0) (name "GND") (number "1")))
  )"""
    b.lib_symbols["power:+5V"] = """
  (symbol "power:+5V" (power) (pin_names (offset 0)) (in_bom yes) (on_board yes)
    (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+5V" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
    (symbol "+5V_0_1" (polyline (pts (xy -0.762 1.27) (xy 0 2.54) (xy 0.762 1.27))
      (stroke (width 0) (type default)) (fill (type none))))
    (symbol "+5V_1_1" (pin power_in line (at 0 0 90) (length 0) (name "+5V") (number "1")))
  )"""
    b.lib_symbols["power:+3V3"] = """
  (symbol "power:+3V3" (power) (pin_names (offset 0)) (in_bom yes) (on_board yes)
    (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
    (symbol "+3V3_1_1" (pin power_in line (at 0 0 90) (length 0) (name "+3V3") (number "1")))
  )"""
    b.add_lib_symbol_device_r()
    for n in (2, 3, 4, 5, 8):
        b.lib_symbols[f"Connector:Conn_01x0{n}_Pin"] = _conn_sym(f"Conn_01x0{n}_Pin", n)
    b.lib_symbols["Device:C"] = """
  (symbol "Device:C"
    (pin_numbers hide) (pin_names (offset 0.254)) (exclude_from_sim no) (in_bom yes) (on_board yes)
    (property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27))))
    (property "Value" "C" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27))))
    (symbol "C_0_1" (rectangle (start -2.032 -0.762) (end 2.032 0.762)
      (stroke (width 0.508) (type default)) (fill (type none))))
    (symbol "C_1_1"
      (pin passive line (at 0 3.81 90) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
      (pin passive line (at 0 -3.81 270) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
  )"""
    b.lib_symbols["Device:CP"] = """
  (symbol "Device:CP"
    (pin_numbers hide) (pin_names (offset 0.254)) (exclude_from_sim no) (in_bom yes) (on_board yes)
    (property "Reference" "C" (at 0.635 5.08 0) (effects (font (size 1.27 1.27))))
    (property "Value" "CP" (at 0.635 -5.08 0) (effects (font (size 1.27 1.27))))
    (symbol "CP_1_1"
      (pin passive line (at 0 5.08 90) (length 2.54) (name "+" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
      (pin passive line (at 0 -5.08 270) (length 2.54) (name "-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
  )"""
    b.lib_symbols["Switch:SW_Push"] = """
  (symbol "Switch:SW_Push"
    (pin_numbers hide) (pin_names (offset 0) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
    (property "Reference" "SW" (at 3.175 2.54 0) (effects (font (size 1.27 1.27))))
    (property "Value" "SW_Push" (at 3.175 -2.54 0) (effects (font (size 1.27 1.27))))
    (symbol "SW_Push_1_1"
      (pin passive line (at 0 0 180) (length 2.54) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
      (pin passive line (at 5.08 0 0) (length 2.54) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
  )"""
    csym = (LIBS / "carrier.kicad_sym").read_text(encoding="utf-8")
    names = ("SN74AHCT125N", "F_ESP", "SJ_SERVO")
    lib_close = csym.rfind("\n)")
    for i, sname in enumerate(names):
        marker = f'(symbol "{sname}"'
        start = csym.index(marker)
        if i + 1 < len(names):
            end = csym.index(f'(symbol "{names[i + 1]}"', start)
        else:
            close = csym.rfind("\n  )", start, lib_close)
            end = close + len("\n  )") if close != -1 else lib_close
        chunk = csym[start:end].strip()
        chunk = chunk.replace(f'(symbol "{sname}"', f'(symbol "carrier:{sname}"', 1)
        b.lib_symbols[f"carrier:{sname}"] = f"  {chunk}\n"

    # --- Power section (left) ---
    px, py = 50, 40
    b.sym("Connector:Conn_01x02_Pin", "J_MAIN", "5V_MAIN_IN", px, py, "carrier:JST_VH_1x02_Placeholder")
    b.wire(px - 2.54, py, px - 10, py)
    b.glabel("5V_MAIN", px - 10, py, 180)
    b.wire(px - 2.54, py + 2.54, px - 10, py + 2.54)
    b.glabel("GND", px - 10, py + 2.54, 180)

    b.sym("Device:CP", "C_MAIN", "1000uF", px, py + 15, "Capacitor_THT:CP_Radial_D5.0mm_P2.50mm")
    b.glabel("5V_MAIN", px - 5, py + 12, 180)
    b.glabel("GND", px - 5, py + 18, 180)

    b.sym("carrier:SJ_SERVO", "SJ_SERVO", "SJ_SERVO", px + 25, py, "carrier:SolderJumper_2_Bridged")
    b.glabel("5V_MAIN", px + 15, py, 180)
    b.glabel("5V_SERVO", px + 35, py, 0)

    b.sym("Device:CP", "C_SERVO", "1000-2200uF", px + 25, py + 15, "Capacitor_THT:CP_Radial_D5.0mm_P2.50mm")
    b.glabel("5V_SERVO", px + 18, py + 12, 180)
    b.glabel("GND", px + 18, py + 18, 180)

    # Power symbols cluster
    for i, ny in enumerate([60, 70, 80, 90, 100]):
        b.sym("power:+5V", f"#PWR{i+1}", "+5V", 25, ny)
    b.sym("power:GND", "#PWRGND1", "GND", 25, 110)
    b.glabel("5V_LOGIC", 35, 60, 0)
    b.glabel("5V_LED", 35, 70, 0)
    b.glabel("3V3", 35, 80, 0)

    # --- ESP32 placeholder (center) ---
    ex, ey = 120, 70
    b.sym("carrier:F_ESP", "F_ESP", "ESP32-S3 DevKit 2x20", ex, ey, "carrier:F_ESP_2x20_Placeholder")
    b.glabel("5V_LOGIC", ex - 20, ey - 10, 180)
    b.glabel("3V3", ex - 20, ey, 180)
    b.glabel("GND", ex - 20, ey + 10, 180)
    # GPIO labels
    gpio_map = [
        ("LED1_IN", ex - 22, ey - 15),
        ("LED2_IN", ex - 22, ey - 12),
        ("LED3_IN", ex - 22, ey - 9),
        ("LED4_IN", ex - 22, ey - 6),
        ("I2C_SDA", ex - 22, ey - 3),
        ("I2C_SCL", ex - 22, ey),
        ("LD_ESP_RX", ex - 22, ey + 3),
        ("LD_ESP_TX", ex - 22, ey + 6),
        ("SERVO1_PWM", ex - 22, ey + 9),
        ("SERVO2_PWM", ex - 22, ey + 12),
        ("BTN1", ex + 22, ey - 15),
        ("BTN2", ex + 22, ey - 12),
        ("BTN3", ex + 22, ey - 9),
        ("ENC_CLK", ex + 22, ey - 6),
        ("ENC_DT", ex + 22, ey - 3),
        ("ENC_SW", ex + 22, ey),
        ("SPI_SCK", ex + 22, ey + 3),
        ("SPI_MOSI", ex + 22, ey + 6),
        ("SPI_MISO", ex + 22, ey + 9),
        ("ETH_CS", ex + 22, ey + 12),
        ("ETH_RST", ex + 22, ey + 15),
        ("ETH_INT", ex + 22, ey + 18),
    ]
    for name, gx, gy in gpio_map:
        b.glabel(name, gx, gy, 0 if gx > ex else 180)

    # --- AHCT125 (right of ESP) ---
    ux, uy = 170, 55
    b.sym("carrier:SN74AHCT125N", "U2", "SN74AHCT125N", ux, uy, "Package_DIP:DIP-14_W7.62mm")
    b.glabel("5V_LOGIC", ux, uy - 15, 90)
    b.glabel("GND", ux, uy + 18, 90)
    # OE to GND
    for oy in [5.08, 0, -7.62, 7.62]:
        b.wire(ux - 17.78, uy + oy / 2.54 * 2.54, ux - 25, uy + oy)
        b.glabel("GND", ux - 25, uy + oy, 180)
    b.glabel("LED1_IN", ux - 20, uy + 2, 180)
    b.glabel("LED2_IN", ux - 20, uy, 180)
    b.glabel("LED3_IN", ux - 20, uy - 2, 180)
    b.glabel("LED4_IN", ux - 20, uy - 4, 180)
    b.glabel("LED1_DATA", ux + 20, uy + 2, 0)
    b.glabel("LED2_DATA", ux + 20, uy, 0)
    b.glabel("LED3_DATA", ux + 20, uy - 2, 0)
    b.glabel("LED4_DATA", ux + 20, uy - 4, 0)

    b.sym("Device:C", "C_AHCT", "100nF", ux + 15, uy + 20, "Capacitor_THT:C_Disc_D3mm_W2mm_Horizontal")
    b.glabel("5V_LOGIC", ux + 10, uy + 18, 180)
    b.glabel("GND", ux + 10, uy + 22, 180)

    # --- LED chain ---
    lx, ly = 220, 40
    for i in range(1, 5):
        b.sym("Device:R", f"R_LED{i}", "330", lx + (i - 1) * 25, ly, "Resistor_THT:R_AXIAL-0.4_D5.1mm_L12.0mm_Horizontal")
        b.glabel(f"LED{i}_DATA", lx + (i - 1) * 25 - 8, ly, 180)
        b.sym(
            "Connector:Conn_01x03_Pin",
            f"J_LED{i}",
            f"LED{i} 5V|GND|DATA",
            lx + (i - 1) * 25,
            ly + 12,
            "carrier:JST_XH_1x03_Placeholder",
        )
        b.glabel("5V_LED", lx + (i - 1) * 25 - 8, ly + 10, 180)
        b.glabel("GND", lx + (i - 1) * 25 - 8, ly + 14, 180)

    # --- Servo ---
    sx, sy = 220, 90
    for i in range(1, 3):
        b.sym(
            "Connector:Conn_01x03_Pin",
            f"J_SERVO{i}",
            f"SERVO{i}",
            sx + (i - 1) * 30,
            sy,
            "carrier:JST_XH_1x03_Placeholder",
        )
        b.glabel("GND", sx + (i - 1) * 30 - 8, sy, 180)
        b.glabel("5V_SERVO", sx + (i - 1) * 30 - 8, sy + 2.54, 180)
        b.glabel(f"SERVO{i}_PWM", sx + (i - 1) * 30 - 8, sy + 5.08, 180)

    # --- LD2450 ---
    b.sym("Connector:Conn_01x04_Pin", "J_LD2450", "LD2450", 220, 120, "carrier:JST_XH_1x04_Placeholder")
    b.glabel("5V_LOGIC", 210, 118, 180)
    b.glabel("GND", 210, 122, 180)
    b.glabel("LD_ESP_RX", 210, 126, 180)
    b.glabel("LD_ESP_TX", 210, 130, 180)

    # --- OLED / I2C ---
    b.sym("Connector:Conn_01x04_Pin", "J_OLED_EXT", "OLED_EXT", 270, 120, "carrier:JST_XH_1x04_Placeholder")
    b.sym("Connector:Conn_01x04_Pin", "J_I2C", "I2C_EXT", 270, 140, "carrier:JST_XH_1x04_Placeholder")
    b.sym("Connector:Conn_01x04_Pin", "F_OLED", "OLED_DIRECT", 300, 120, "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical")
    for lbl, yy in [("GND", 118), ("3V3", 122), ("I2C_SDA", 126), ("I2C_SCL", 130)]:
        b.glabel(lbl, 260, yy, 180)

    # --- Buttons ---
    bx, by = 50, 140
    b.sym("Connector:Conn_01x04_Pin", "J_BTN", "BTN_EXT", bx, by, "carrier:JST_XH_1x04_Placeholder")
    for i in range(1, 4):
        b.sym("Switch:SW_Push", f"SW{i}", f"BTN{i}", bx + 30 + i * 12, by, "Button_Switch_THT:SW_PUSH_6mm")
        b.glabel(f"BTN{i}", bx + 20 + i * 12, by, 180)
        b.glabel("GND", bx + 20 + i * 12, by + 5, 180)

    # --- Encoder ---
    b.sym("Connector:Conn_01x05_Pin", "J_ENC", "ENC_EXT", 50, 165, "carrier:JST_XH_1x05_Placeholder")
    b.glabel("ENC_CLK", 40, 163, 180)
    b.glabel("ENC_DT", 40, 166, 180)
    b.glabel("ENC_SW", 40, 169, 180)

    # --- W5500 optional Ethernet module (NOT POPULATED) ---
    wx, wy = 300, 55
    b.sym(
        "Connector:Conn_01x08_Pin",
        "J_W5500",
        "W5500_OPTIONAL_NP",
        wx,
        wy,
        "carrier:JST_W5500_1x08_Placeholder",
    )
    w5500_pins = [
        ("3V3", 0),
        ("GND", 2.54),
        ("SPI_SCK", 5.08),
        ("SPI_MOSI", 7.62),
        ("SPI_MISO", 10.16),
        ("ETH_CS", 12.7),
        ("ETH_RST", 15.24),
        ("ETH_INT", 17.78),
    ]
    for net, dy in w5500_pins:
        b.glabel(net, wx - 12, wy + dy, 180)
    b.items.append(
        f'  (text "W5500 OPTIONAL / NOT POPULATED\\n'
        f"Bedrade module voor toekomstige Art-Net/sACN route\\n"
        f"SPI: GPIO5/13/14 CS47 RST4 INT39 (zie pinout-table.md)\\n"
        f"    (at {wx - 5} {wy - 12} 0) (effects (font (size 1.2 1.2)) (justify left)) (uuid {uid()}))\n"
    )

    # Notes
    b.items.append(
        f'  (text "PLACEHOLDER SCHEMATIC v0.2 - run ERC in KiCad\\n'
        f"ESP32 footprint NOT FINAL - see measurements.md\\n"
        f'Do NOT order PCB / no Gerbers"\n'
        f"    (at 30 30 0) (effects (font (size 1.5 1.5)) (justify left)) (uuid {uid()}))\n"
    )

    (ROOT / f"{PROJECT}.kicad_sch").write_text(fix_pin_orientations(b.build()), encoding="utf-8")


def _pcb_gr_text(text: str, x: float, y: float, size: float = 0.8, layer: str = "F.SilkS") -> str:
    return (
        f'  (gr_text "{text}" (at {x} {y} 0) (layer "{layer}") (tstamp 0)\n'
        f"    (effects (font (size {size} {size}) (thickness {max(size * 0.12, 0.1)}))))\n"
    )


def verify_pcb_layout(placements: list[tuple[str, str, str, float, float]]) -> None:
    for ref, _val, libfp, x, y in placements:
        w, h = FOOTPRINT_EXTENTS.get(libfp, (8.0, 8.0))
        if x < BOARD_MARGIN or y < BOARD_MARGIN:
            raise RuntimeError(f"{ref}: placement ({x},{y}) inside margin")
        if x + w > BOARD_W - BOARD_MARGIN or y + h > BOARD_H - BOARD_MARGIN:
            raise RuntimeError(f"{ref}: extends outside board ({x}+{w}, {y}+{h})")


def write_pcb() -> None:
    nets = [
        "",
        "5V_MAIN",
        "GND",
        "5V_LOGIC",
        "5V_LED",
        "5V_SERVO",
        "3V3",
        "LED1_IN",
        "LED1_DATA",
        "LED2_IN",
        "LED2_DATA",
        "LED3_IN",
        "LED3_DATA",
        "LED4_IN",
        "LED4_DATA",
        "I2C_SDA",
        "I2C_SCL",
        "LD_ESP_RX",
        "LD_ESP_TX",
        "SERVO1_PWM",
        "SERVO2_PWM",
        "BTN1",
        "BTN2",
        "BTN3",
        "ENC_CLK",
        "ENC_DT",
        "ENC_SW",
        "SPI_SCK",
        "SPI_MOSI",
        "SPI_MISO",
        "ETH_CS",
        "ETH_RST",
        "ETH_INT",
    ]
    net_lines = []
    for i, n in enumerate(nets):
        net_lines.append(f'  (net {i} "{n}")')

    def fp(ref: str, value: str, footprint: str, x: float, y: float, layer: str = "F.Cu") -> str:
        ts = uid()
        return f"""
  (footprint "{footprint}" (version 20240108) (generator "pcbnew")
    (layer "{layer}") (uuid {uid()}) (at {x} {y})
    (descr "") (tags "") (property "Reference" "{ref}")
    (property "Value" "{value}")
    (property "Footprint" "{footprint}")
    (path "/{ts}")
    (attr through_hole)
  )"""

    items = []
    items.append(
        f"""
  (gr_rect (start 0 0) (end {BOARD_W} {BOARD_H}) (stroke (width 0.15) (type default))
    (fill none) (layer "Edge.Cuts") (tstamp 0))
"""
    )

    # ESP zone (center) — keep-outs on Dwgs.User only
    esp_x, esp_y = 28.0, 10.0
    esp_w, esp_h = FOOTPRINT_EXTENTS["carrier:F_ESP_2x20_Placeholder"]
    items.append(
        f"""
  (gr_rect (start {esp_x} {esp_y}) (end {esp_x + esp_w} {esp_y + esp_h})
    (stroke (width 0.15) (type default)) (fill none) (layer "Dwgs.User") (tstamp 0))
  (gr_rect (start {esp_x + 2} {esp_y - 2}) (end {esp_x + esp_w - 2} {esp_y + 6})
    (stroke (width 0.2) (type default)) (fill none) (layer "Dwgs.User") (tstamp 0))
  (gr_text "USB KEEP-OUT" (at {esp_x + esp_w / 2} {esp_y + 2} 0) (layer "Dwgs.User") (tstamp 0)
    (effects (font (size 0.8 0.8) (thickness 0.1))))
  (gr_rect (start {esp_x + 4} {esp_y + 2}) (end {esp_x + esp_w - 4} {esp_y + 14})
    (stroke (width 0.2) (type dash)) (fill none) (layer "Dwgs.User") (tstamp 0))
  (gr_text "ANTENNA KEEP-OUT" (at {esp_x + esp_w / 2} {esp_y + 8} 0) (layer "Dwgs.User") (tstamp 0)
    (effects (font (size 0.75 0.75) (thickness 0.1))))
"""
    )

    # Zone labels (F.SilkS)
    items.append(_pcb_gr_text("ESP32-S3 Utility Carrier v0.3 PLACEHOLDER", 45, 1.2, 1.0))
    items.append(_pcb_gr_text("ESP FOOTPRINT NIET DEFINITIEF", esp_x + 1, esp_y + esp_h + 1.2, 0.75))
    items.append(_pcb_gr_text("POWER", 3, 2.5, 0.7))
    items.append(_pcb_gr_text("LED OUTPUTS (right)", 72, 2.5, 0.7))
    items.append(_pcb_gr_text("LED1-3: 5-TUBE OUTPUT", 68, 7.5, 0.65))
    items.append(_pcb_gr_text("LED4: AUX / RESERVE", 68, 43.5, 0.65))
    items.append(_pcb_gr_text("SENSOR / OLED / I2C", 3, 41.5, 0.65))
    items.append(_pcb_gr_text("UI: BTN + ENC", 48, 41.5, 0.65))
    items.append(_pcb_gr_text("SERVO", 3, 31.5, 0.65))
    items.append(_pcb_gr_text("W5500 OPTIONAL / NOT POPULATED", 6, 54.5, 0.65))

    # v0.3 placement map (all connectors inside outline)
    placements = [
        # Power — top-left
        ("J_MAIN", "5V_MAIN_IN", "carrier:JST_VH_1x02_Placeholder", 3, 4),
        ("C_MAIN", "1000uF", "Capacitor_THT:CP_Radial_D5.0mm_P2.50mm", 10, 4),
        ("SJ_SERVO", "SJ_SERVO", "carrier:SolderJumper_2_Bridged", 17, 4),
        ("C_SERVO", "2200uF", "Capacitor_THT:CP_Radial_D5.0mm_P2.50mm", 24, 4),
        # ESP — center
        ("F_ESP", "ESP32_2x20", "carrier:F_ESP_2x20_Placeholder", esp_x, esp_y),
        # AHCT — between ESP and LED column
        ("U2", "SN74AHCT125N", "Package_DIP:DIP-14_W7.62mm", 54, 14),
        ("C_AHCT", "100nF", "Capacitor_THT:C_Disc_D3mm_W2mm_Horizontal", 62, 30),
        # LED1–4 — right edge, grouped
        ("R_LED1", "330", "Resistor_THT:R_AXIAL-0.4_D5.1mm_L12.0mm_Horizontal", 68, 10),
        ("J_LED1", "LED1", "carrier:JST_XH_1x03_Placeholder", 78, 10),
        ("R_LED2", "330", "Resistor_THT:R_AXIAL-0.4_D5.1mm_L12.0mm_Horizontal", 68, 20),
        ("J_LED2", "LED2", "carrier:JST_XH_1x03_Placeholder", 78, 20),
        ("R_LED3", "330", "Resistor_THT:R_AXIAL-0.4_D5.1mm_L12.0mm_Horizontal", 68, 30),
        ("J_LED3", "LED3", "carrier:JST_XH_1x03_Placeholder", 78, 30),
        ("R_LED4", "330", "Resistor_THT:R_AXIAL-0.4_D5.1mm_L12.0mm_Horizontal", 68, 40),
        ("J_LED4", "LED4_AUX", "carrier:JST_XH_1x03_Placeholder", 78, 40),
        # Servo — left, below power
        ("J_SERVO1", "SERVO1", "carrier:JST_XH_1x03_Placeholder", 3, 34),
        ("J_SERVO2", "SERVO2", "carrier:JST_XH_1x03_Placeholder", 11, 34),
        # Sensor / OLED / I2C — lower-left cluster
        ("J_LD2450", "LD2450", "carrier:JST_XH_1x04_Placeholder", 3, 44),
        ("J_OLED_EXT", "OLED", "carrier:JST_XH_1x04_Placeholder", 12, 44),
        ("J_I2C", "I2C", "carrier:JST_XH_1x04_Placeholder", 21, 44),
        ("F_OLED", "OLED_DIR", "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical", 12, 52),
        # UI — bottom center
        ("SW1", "BTN1", "Button_Switch_THT:SW_PUSH_6mm", 48, 48),
        ("SW2", "BTN2", "Button_Switch_THT:SW_PUSH_6mm", 56, 48),
        ("SW3", "BTN3", "Button_Switch_THT:SW_PUSH_6mm", 64, 48),
        ("J_BTN", "BTN_EXT", "carrier:JST_XH_1x04_Placeholder", 48, 56),
        ("J_ENC", "ENC", "carrier:JST_XH_1x05_Placeholder", 58, 56),
        # W5500 — bottom-left, clear of UI cluster
        ("J_W5500", "W5500_OPT_NP", "carrier:JST_W5500_1x08_Placeholder", 8, 57),
    ]
    verify_pcb_layout(placements)
    for ref, val, libfp, x, y in placements:
        items.append(fp(ref, val, libfp, x, y))

    # Short power stubs only (no diagonal placeholder routes); rest = airwires in KiCad.
    items.append(
        """
  (segment (start 3 5) (end 28 5) (width 1.0) (layer "F.Cu") (net 1) (tstamp 0))
  (segment (start 3 6) (end 28 6) (width 0.8) (layer "F.Cu") (net 2) (tstamp 0))
  (zone (net 2) (net_name "GND") (layer "F.Cu") (hatch edge 0.508)
    (connect_pads (clearance 0.3))
    (min_thickness 0.25)
    (fill yes (thermal_gap 0.5) (thermal_bridge_width 0.5))
    (polygon (pts (xy 1 1) (xy 89 1) (xy 89 64) (xy 1 64)))
    (uuid 00000000-0000-0000-0000-000000000001))
"""
    )

    pcb = f"""(kicad_pcb (version 20240108) (generator "generate_placeholder.py")
  (general (thickness 1.6) (legacy_teardrops no))
  (paper "A3")
  (layers
    (0 "F.Cu" signal)
    (31 "B.Cu" signal)
    (32 "B.Adhes" user "B.Adhesive")
    (33 "F.Adhes" user "F.Adhesive")
    (34 "B.Paste" user)
    (35 "F.Paste" user)
    (36 "B.SilkS" user "B.Silk screen")
    (37 "F.SilkS" user "F.Silk screen")
    (38 "B.Mask" user)
    (39 "F.Mask" user)
    (40 "Dwgs.User" user "User.Drawings")
    (41 "Cmts.User" user "User.Comments")
    (44 "Edge.Cuts" user)
  )
  (setup
    (pad_to_mask_clearance 0)
    (allow_soldermask_bridges_in_footprints no)
    (pcbplotparams
      (layerselection 0x00010fc_ffffffff)
      (plot_on_all_layers_selection 0x0000000_00000001)
      (disableapertmacros no)
      (usegerberattributes yes)
      (usegerberadvancedattributes yes)
      (creategerberjobfile no)
      (dashed_line_dash_ratio 12.000000)
      (dashed_line_gap_ratio 3.000000)
      (svgprecision 4)
      (plotframeref no)
      (viasonmask no)
      (mode 1)
      (useauxorigin no)
      (hpglpennumber 1)
      (hpglpenspeed 20)
      (hpglpendiameter 15.000000)
      (pdf_front_fp_property_popups yes)
      (pdf_back_fp_property_popups yes)
      (dxfpolygonmode yes)
      (dxfimperialunits yes)
      (dxfusepcbnewfont yes)
      (psnegative no)
      (psa4output no)
      (plotreference yes)
      (plotvalue yes)
      (plotfptext yes)
      (plotinvisibletext no)
      (sketchpadsonfab no)
      (subtractmaskfromsilk no)
      (outputformat 1)
      (mirror no)
      (drillshape 1)
      (scaleselection 1)
      (outputdirectory "")
    )
  )
{chr(10).join(net_lines)}
{"".join(items)}
)
"""
    (ROOT / f"{PROJECT}.kicad_pcb").write_text(pcb, encoding="utf-8")


def write_readme_kicad() -> None:
    (ROOT / "README.md").write_text(
        """# KiCad project — ESP32-S3 Utility Carrier v1 (placeholder)

**Status:** learning / visual placeholder only — **NOT production-ready**.

Open in KiCad:

1. Open `esp32-s3-utility-carrier.kicad_pro` in this folder.
2. Run **Tools → Update PCB from Schematic** if symbols show broken (first open).
3. Run ERC (schematic) and DRC (PCB) — expect warnings on incomplete routing.

## Do NOT

- Export Gerbers for fabrication yet.
- Order PCB before `../hardware/measurements.md` is verified on the real DevKit.
- Treat `F_ESP` footprint as final (silk: **NIET DEFINITIEF**).

## Files

| File | Purpose |
|---|---|
| `esp32-s3-utility-carrier.kicad_pro` | Project root |
| `esp32-s3-utility-carrier.kicad_sch` | Placeholder schematic |
| `esp32-s3-utility-carrier.kicad_pcb` | Placeholder PCB (90×65 mm) |
| `libraries/carrier.kicad_sym` | F_ESP, SN74AHCT125N, SJ_SERVO |
| `libraries/carrier.pretty/` | Placeholder footprints |

Regenerate (optional): `python3 tools/generate_placeholder.py`

See `../docs/kicad-next-steps.md` and `../hardware/measurements.md`.
""",
        encoding="utf-8",
    )


def verify_schematic_layout(path: Path) -> None:
    """sheet_instances must come after lib_symbols and sheet symbol instances."""
    text = path.read_text(encoding="utf-8")
    lib_end = text.index("  )\n", text.index("(lib_symbols"))
    sheet_inst = text.index("(sheet_instances")
    first_inst = text.index('(symbol (lib_id "', lib_end)
    if sheet_inst < first_inst:
        raise RuntimeError(f"{path}: sheet_instances before placed symbols")


def verify_pin_orientations() -> None:
    """Raise if any pin (at X Y) lacks a third orientation value."""
    pin_at_re = re.compile(r"\(pin [^\n]*?\(at (-?[0-9.]+) (-?[0-9.]+)\)(?! *-?[0-9.])( \(length)")
    for path in (LIBS / "carrier.kicad_sym", ROOT / f"{PROJECT}.kicad_sch"):
        text = path.read_text(encoding="utf-8")
        hits = pin_at_re.findall(text)
        if hits:
            raise RuntimeError(f"{path}: {len(hits)} pin(s) missing orientation")


def verify_pinout() -> None:
    used = set(PINOUT.values())
    overlap = used & FORBIDDEN_GPIO
    if overlap:
        raise RuntimeError(f"PINOUT uses forbidden GPIO: {sorted(overlap)}")
    if len(used) != len(PINOUT):
        raise RuntimeError("PINOUT has duplicate GPIO assignments")


def main() -> None:
    verify_pinout()
    LIBS.mkdir(parents=True, exist_ok=True)
    write_carrier_sym()
    write_footprints()
    write_lib_tables()
    write_project()
    write_schematic()
    write_pcb()
    write_readme_kicad()
    verify_pin_orientations()
    verify_schematic_layout(ROOT / f"{PROJECT}.kicad_sch")
    text = (ROOT / f"{PROJECT}.kicad_pcb").read_text(encoding="utf-8")
    if "(justify center)" in text:
        raise RuntimeError("PCB still contains invalid (justify center)")
    print(f"Generated KiCad placeholder in {ROOT}")


if __name__ == "__main__":
    main()
