"""PCB pad coordinates and v0.7 visible routing for generate_placeholder.py."""
from __future__ import annotations

import math
from typing import Iterable

# Pad offsets (mm) from footprint anchor at (0,0), pad "1" / pin 1 unless noted.
PAD_OFFSETS: dict[str, dict[str, tuple[float, float]]] = {
    "carrier:JST_VH_1x02_Placeholder": {"1": (0, 0), "2": (3.96, 0)},
    "carrier:JST_XH_1x03_Placeholder": {"1": (0, 0), "2": (2.5, 0), "3": (5.0, 0)},
    "carrier:JST_XH_1x04_Placeholder": {
        "1": (0, 0),
        "2": (2.5, 0),
        "3": (5.0, 0),
        "4": (7.5, 0),
    },
    "carrier:JST_XH_1x05_Placeholder": {
        "1": (0, 0),
        "2": (2.5, 0),
        "3": (5.0, 0),
        "4": (7.5, 0),
        "5": (10.0, 0),
    },
    "carrier:JST_W5500_1x08_Placeholder": {str(i): ((i - 1) * 2.5, 0) for i in range(1, 9)},
    "carrier:F_ESP_2x20_Placeholder": {
        **{str(i): (0, (i - 1) * 2.54) for i in range(1, 21)},
        **{str(i): (22.86, (i - 21) * 2.54) for i in range(21, 41)},
    },
    "carrier:SolderJumper_2_Bridged": {"1": (-1.5, 0), "2": (1.5, 0)},
    "Package_DIP:DIP-14_W7.62mm": {
        "1": (0, 0),
        "2": (0, 2.54),
        "3": (0, 5.08),
        "4": (0, 7.62),
        "5": (0, 10.16),
        "6": (0, 12.7),
        "7": (0, 15.24),
        "8": (7.62, 15.24),
        "9": (7.62, 12.7),
        "10": (7.62, 10.16),
        "11": (7.62, 7.62),
        "12": (7.62, 5.08),
        "13": (7.62, 2.54),
        "14": (7.62, 0),
    },
    "Capacitor_THT:CP_Radial_D5.0mm_P2.50mm": {"1": (0, 0), "2": (2.5, 0)},
    "Capacitor_THT:C_Disc_D3mm_W2mm_Horizontal": {"1": (0, 0), "2": (3.0, 0)},
    "Resistor_THT:R_AXIAL-0.4_D5.1mm_L12.0mm_Horizontal": {"1": (0, 0), "2": (12.0, 0)},
    "Button_Switch_THT:SW_PUSH_6mm": {"1": (-2.54, 0), "2": (2.54, 0)},
    "carrier:M3_MountingHole": {},
}

# (reference, pad_number) -> net name
REF_PAD_NETS: dict[tuple[str, str], str] = {
    ("J_MAIN", "1"): "5V_MAIN",
    ("J_MAIN", "2"): "GND",
    ("C_MAIN", "1"): "5V_MAIN",
    ("C_MAIN", "2"): "GND",
    ("SJ_SERVO", "1"): "5V_MAIN",
    ("SJ_SERVO", "2"): "5V_SERVO",
    ("C_SERVO", "1"): "5V_SERVO",
    ("C_SERVO", "2"): "GND",
    ("J_SERVO1", "1"): "5V_SERVO",
    ("J_SERVO1", "2"): "GND",
    ("J_SERVO1", "3"): "SERVO1_PWM",
    ("J_SERVO2", "1"): "5V_SERVO",
    ("J_SERVO2", "2"): "GND",
    ("J_SERVO2", "3"): "SERVO2_PWM",
    ("U2", "14"): "5V_LOGIC",
    ("U2", "7"): "GND",
    ("U2", "1"): "GND",
    ("U2", "4"): "GND",
    ("U2", "10"): "GND",
    ("U2", "13"): "GND",
    ("U2", "2"): "LED1_IN",
    ("U2", "5"): "LED2_IN",
    ("U2", "9"): "LED3_IN",
    ("U2", "11"): "LED4_IN",
    ("U2", "3"): "LED1_DATA",
    ("U2", "6"): "LED2_DATA",
    ("U2", "8"): "LED3_DATA",
    ("U2", "12"): "LED4_DATA",
    ("C_AHCT", "1"): "5V_LOGIC",
    ("C_AHCT", "2"): "GND",
    ("R_LED1", "1"): "LED1_DATA",
    ("R_LED1", "2"): "LED1_DATA",
    ("R_LED2", "1"): "LED2_DATA",
    ("R_LED2", "2"): "LED2_DATA",
    ("R_LED3", "1"): "LED3_DATA",
    ("R_LED3", "2"): "LED3_DATA",
    ("R_LED4", "1"): "LED4_DATA",
    ("R_LED4", "2"): "LED4_DATA",
    ("J_LED1", "1"): "5V_LED",
    ("J_LED1", "2"): "GND",
    ("J_LED1", "3"): "LED1_DATA",
    ("J_LED2", "1"): "5V_LED",
    ("J_LED2", "2"): "GND",
    ("J_LED2", "3"): "LED2_DATA",
    ("J_LED3", "1"): "5V_LED",
    ("J_LED3", "2"): "GND",
    ("J_LED3", "3"): "LED3_DATA",
    ("J_LED4", "1"): "5V_LED",
    ("J_LED4", "2"): "GND",
    ("J_LED4", "3"): "LED4_DATA",
    ("F_ESP", "18"): "LED1_IN",
    ("F_ESP", "17"): "LED2_IN",
    ("F_ESP", "21"): "LED3_IN",
    ("F_ESP", "12"): "LED4_IN",
    ("F_ESP", "15"): "SERVO1_PWM",
    ("F_ESP", "16"): "SERVO2_PWM",
    ("F_ESP", "10"): "LD_ESP_RX",
    ("F_ESP", "11"): "LD_ESP_TX",
    ("F_ESP", "8"): "I2C_SDA",
    ("F_ESP", "9"): "I2C_SCL",
    ("F_ESP", "1"): "BTN1",
    ("F_ESP", "2"): "BTN2",
    ("F_ESP", "42"): "BTN3",
    ("F_ESP", "6"): "ENC_CLK",
    ("F_ESP", "7"): "ENC_DT",
    ("F_ESP", "40"): "ENC_SW",
    ("F_ESP", "5"): "SPI_SCK",
    ("F_ESP", "13"): "SPI_MOSI",
    ("F_ESP", "14"): "SPI_MISO",
    ("F_ESP", "47"): "ETH_CS",
    ("F_ESP", "4"): "ETH_RST",
    ("F_ESP", "39"): "ETH_INT",
}

TRACK_SIG = 0.25
TRACK_PWR = 1.0
TRACK_GND = 0.8


def pad_xy(
    ref: str,
    pad: str,
    libfp: str,
    ox: float,
    oy: float,
    angle: float = 0.0,
) -> tuple[float, float]:
    dx, dy = PAD_OFFSETS[libfp][pad]
    if angle % 360 == 180.0:
        return (ox - dx, oy + dy)
    return (ox + dx, oy + dy)


def _ortho_route(points: list[tuple[float, float]]) -> list[tuple[float, float, float, float]]:
    """Expand polyline to axis-aligned segments."""
    segs: list[tuple[float, float, float, float]] = []
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        if abs(x1 - x2) < 0.01 or abs(y1 - y2) < 0.01:
            segs.append((x1, y1, x2, y2))
        else:
            segs.append((x1, y1, x2, y1))
            segs.append((x2, y1, x2, y2))
    return segs


def _seg(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    width: float,
    net_id: int,
    layer: str = "F.Cu",
) -> str:
    return (
        f'  (segment (start {x1} {y1}) (end {x2} {y2}) (width {width}) (layer "{layer}") '
        f'(net {net_id}) (tstamp 0))\n'
    )


def build_visible_routing(
    place: dict[str, tuple[float, float]],
    rotate: dict[str, float],
    fpmap: dict[str, str],
    net_ids: dict[str, int],
) -> str:
    """Return KiCad segment blocks for the first routing pass."""

    def p(ref: str, pad: str) -> tuple[float, float]:
        x, y = place[ref]
        return pad_xy(ref, pad, fpmap[ref], x, y, rotate.get(ref, 0.0))

    def nid(name: str) -> int:
        return net_ids[name]

    lines: list[str] = []
    raw: list[tuple[list[tuple[float, float]], float, str]] = []

    gnd_x = 10.0

    # --- Main power ---
    raw.append(
        ([p("J_MAIN", "1"), (gnd_x + 2, p("J_MAIN", "1")[1]), p("C_MAIN", "1")], TRACK_PWR, "5V_MAIN")
    )
    raw.append(
        ([p("J_MAIN", "2"), (gnd_x, p("J_MAIN", "2")[1])], TRACK_GND, "GND")
    )
    raw.append(
        ([p("C_MAIN", "2"), (gnd_x, p("C_MAIN", "2")[1])], TRACK_GND, "GND")
    )
    raw.append(
        (
            [
                p("C_MAIN", "1"),
                (gnd_x + 2, 22),
                p("SJ_SERVO", "1"),
            ],
            TRACK_PWR,
            "5V_MAIN",
        )
    )

    # 5V_LOGIC branch (U2 VCC + C_AHCT)
    vcc = p("U2", "14")
    raw.append(
        (
            [
                (gnd_x + 2, 22),
                (gnd_x + 2, vcc[1]),
                vcc,
                p("C_AHCT", "1"),
            ],
            TRACK_PWR,
            "5V_LOGIC",
        )
    )
    raw.append(([p("C_AHCT", "2"), (gnd_x, p("C_AHCT", "2")[1])], TRACK_GND, "GND"))

    # U2 GND + ~OE pins to GND rail
    for pin in ("7", "1", "4", "10", "13"):
        raw.append(([p("U2", pin), (gnd_x, p("U2", pin)[1])], TRACK_GND, "GND"))

    # --- Servo power (manual cluster left) ---
    raw.append(([p("SJ_SERVO", "2"), p("C_SERVO", "1")], TRACK_PWR, "5V_SERVO"))
    raw.append(([p("C_SERVO", "2"), (gnd_x, p("C_SERVO", "2")[1])], TRACK_GND, "GND"))
    raw.append(([p("C_SERVO", "1"), p("J_SERVO2", "1")], TRACK_PWR, "5V_SERVO"))
    raw.append(([p("J_SERVO2", "2"), (gnd_x, p("J_SERVO2", "2")[1])], TRACK_GND, "GND"))
    raw.append(
        (
            [
                p("C_SERVO", "1"),
                (gnd_x + 2, 55),
                (65, 55),
                p("J_SERVO1", "1"),
            ],
            TRACK_PWR,
            "5V_SERVO",
        )
    )
    raw.append(([p("J_SERVO1", "2"), (gnd_x, p("J_SERVO1", "2")[1])], TRACK_GND, "GND"))

    # --- LED 5V / GND distribution (right column) ---
    led5v_x = 106.0
    for jref in ("J_LED1", "J_LED2", "J_LED3", "J_LED4"):
        raw.append(
            (
                [
                    (led5v_x, vcc[1]),
                    (led5v_x, p(jref, "1")[1]),
                    p(jref, "1"),
                ],
                TRACK_PWR,
                "5V_LED",
            )
        )
        raw.append(
            (
                [
                    p(jref, "2"),
                    (gnd_x + 55, p(jref, "2")[1]),
                    (gnd_x + 55, 16),
                    (gnd_x, 16),
                ],
                TRACK_GND,
                "GND",
            )
        )
    raw.append(
        (
            [
                (gnd_x + 2, vcc[1]),
                (led5v_x, vcc[1]),
            ],
            TRACK_PWR,
            "5V_LED",
        )
    )

    # --- LED data: ESP -> U2 inputs ---
    bus_x = 68.0
    led_channels = [
        ("LED1_IN", "18", "2", "3", "R_LED1", "J_LED1"),
        ("LED2_IN", "17", "5", "6", "R_LED2", "J_LED2"),
        ("LED3_IN", "21", "9", "8", "R_LED3", "J_LED3"),
        ("LED4_IN", "12", "11", "12", "R_LED4", "J_LED4"),
    ]
    for net_in, esp_pad, u_in, u_out, rref, jref in led_channels:
        esp = p("F_ESP", esp_pad)
        u_i = p("U2", u_in)
        u_o = p("U2", u_out)
        r1 = p(rref, "1")
        r2 = p(rref, "2")
        j3 = p(jref, "3")
        y_bus = u_i[1]
        if esp_pad == "21":
            path_in = [esp, (esp[0], y_bus), (bus_x, y_bus), u_i]
        else:
            path_in = [esp, (bus_x, esp[1]), (bus_x, y_bus), u_i]
        raw.append((path_in, TRACK_SIG, net_in))
        raw.append(([u_o, r1, r2, j3], TRACK_SIG, net_in.replace("_IN", "_DATA")))

    # --- GND backbone (visible) ---
    raw.append(([(gnd_x, 14), (gnd_x, 78)], TRACK_GND, "GND"))

    for paths, width, net in raw:
        for x1, y1, x2, y2 in _ortho_route(paths):
            lines.append(_seg(x1, y1, x2, y2, width, nid(net)))

    return "".join(lines)
