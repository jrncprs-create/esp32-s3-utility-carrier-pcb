"""Placeholder PCB routing for generate_placeholder.py (v0.9+)."""
from __future__ import annotations

# Pad offsets (mm) from footprint anchor at (0,0).
PAD_OFFSETS: dict[str, dict[str, tuple[float, float]]] = {
    "carrier:ScrewTerm_2p_5.08_Placeholder": {"1": (0, 0), "2": (5.08, 0)},
    "carrier:ScrewTerm_3p_5.08_Placeholder": {"1": (0, 0), "2": (5.08, 0), "3": (10.16, 0)},
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
    "carrier:W5500_SBC_USR_ES1_Placeholder": {str(i): ((i - 1) * 2.5, 0) for i in range(1, 9)},
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
    "carrier:M3_MountingHole": {},
}

TRACK_SIG = 0.25
TRACK_PWR = 0.5  # J_MAIN ↔ C_MAIN only
TRACK_DECO = 0.35  # U2 ↔ C_AHCT and C_MAIN → U2 feed

# South channel below ESP body (y2 ≈ 65.5) — avoids top-edge power bus.
PWR_FEED_X = 38.0
PWR_SOUTH_Y = 67.0

# ESP DevKitC-1 — pin rows 22.86 mm apart; board outline 25.4 × 52.5 mm (verify clone).
ESP_X1, ESP_Y1 = 45.0, 13.0
ESP_ROW_W, ESP_BOARD_H = 22.86, 52.5
ESP_BOARD_W = 25.4
ESP_X2, ESP_Y2 = ESP_X1 + ESP_ROW_W, ESP_Y1 + ESP_BOARD_H
USB_Y1, USB_Y2 = ESP_Y1, ESP_Y1 + 6.0
ANT_Y1, ANT_Y2 = ESP_Y2 - 6.0, ESP_Y2
SPINE_X = 72.0  # routing channel right of ESP pin rows
ESP_ROUTE_X = ESP_X1 - 2.0  # west of left pin row


def pad_xy(
    libfp: str, ox: float, oy: float, pad: str, angle: float = 0.0
) -> tuple[float, float]:
    dx, dy = PAD_OFFSETS[libfp][pad]
    if angle % 360 == 180.0:
        return (ox - dx, oy + dy)
    return (ox + dx, oy + dy)


def _seg(x1: float, y1: float, x2: float, y2: float, width: float, net_id: int) -> str:
    return (
        f'  (segment (start {x1} {y1}) (end {x2} {y2}) (width {width}) (layer "F.Cu") '
        f'(net {net_id}) (tstamp 0))\n'
    )


def _route_45(points: list[tuple[float, float]]) -> list[tuple[float, float, float, float]]:
    """Axis-aligned + 45° corner segments between waypoints."""
    out: list[tuple[float, float, float, float]] = []
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        dx, dy = x2 - x1, y2 - y1
        if abs(dx) < 0.02 or abs(dy) < 0.02:
            out.append((x1, y1, x2, y2))
            continue
        m = min(abs(dx), abs(dy))
        xm = x1 + m * (1.0 if dx > 0 else -1.0)
        ym = y1 + m * (1.0 if dy > 0 else -1.0)
        out.append((x1, y1, xm, ym))
        out.append((xm, ym, x2, y2))
    return out


def _crosses_esp_interior(x1: float, y1: float, x2: float, y2: float) -> bool:
    """True if axis-aligned segment passes through ESP body (not spine channel)."""
    xmin, xmax = min(x1, x2), max(x1, x2)
    ymin, ymax = min(y1, y2), max(y1, y2)
    if abs(y1 - y2) < 0.02:
        return ymin < ESP_Y2 and ymax > ESP_Y1 and xmax > ESP_X1 and xmin < ESP_X2
    if abs(x1 - x2) < 0.02:
        return xmin < ESP_X2 and xmax > ESP_X1 and ymax > ESP_Y1 and ymin < ESP_Y2
    return False


def _esp_bypass_y(esp_y: float) -> float:
    """Route outside ESP USB / ANT keep-outs and below/above pin-row envelope."""
    if esp_y < 40.0:
        return 10.0  # west channel under ESP (below y=13 body, clear USB y≤19)
    return 66.5  # south of antenna keep-out (y≥57.8)


def _path_esp_to_u2(esp: tuple[float, float], u2: tuple[float, float]) -> list[tuple[float, float]]:
    """ESP GPIO pad → spine → U2 input without crossing ESP body."""
    ex, ey = esp
    ux, uy = u2
    if ex >= ESP_X2 - 0.5:
        return [esp, (SPINE_X, ey), (SPINE_X, uy), u2]
    by = _esp_bypass_y(ey)
    return [esp, (ESP_ROUTE_X, ey), (ESP_ROUTE_X, by), (SPINE_X, by), (SPINE_X, uy), u2]


def build_placeholder_routing(
    place: dict[str, tuple[float, float]],
    rotate: dict[str, float],
    fpmap: dict[str, str],
    net_ids: dict[str, int],
) -> str:
    """LED data (×3) + minimal local power — no top bus, no LED 5V/GND pours."""

    def p(ref: str, pad: str) -> tuple[float, float]:
        x, y = place[ref]
        return pad_xy(fpmap[ref], x, y, pad, rotate.get(ref, 0.0))

    def nid(name: str) -> int:
        return net_ids[name]

    raw: list[tuple[list[tuple[float, float]], float, str]] = []

    led_channels = [
        ("LED1_IN", "18", "2", "3", "R_LED1", "J_LED1"),
        ("LED2_IN", "17", "5", "6", "R_LED2", "J_LED2"),
        ("LED3_IN", "21", "9", "8", "R_LED3", "J_LED3"),
    ]
    for net_in, esp_pad, u_in, u_out, rref, jref in led_channels:
        esp = p("F_ESP", esp_pad)
        u_i = p("U2", u_in)
        u_o = p("U2", u_out)
        r1 = p(rref, "1")
        j3 = p(jref, "3")
        net_data = net_in.replace("_IN", "_DATA")

        raw.append((_path_esp_to_u2(esp, u_i), TRACK_SIG, net_in))
        raw.append(([u_o, r1, j3], TRACK_SIG, net_data))

    # Main in → bulk cap (direct, local only)
    j5 = p("J_MAIN", "1")
    jg = p("J_MAIN", "2")
    c5 = p("C_MAIN", "1")
    cg = p("C_MAIN", "2")
    raw.append(([j5, c5], TRACK_PWR, "5V_MAIN"))
    raw.append(([jg, cg], TRACK_PWR, "GND"))

    vcc = p("U2", "14")
    gnd = p("U2", "7")
    c_v = p("C_AHCT", "1")
    c_g = p("C_AHCT", "2")

    # 5V logic: C_MAIN → U2 via west + south channel (no top-edge bus, no LED 5V pours)
    raw.append(
        (
            [c5, (PWR_FEED_X, c5[1]), (PWR_FEED_X, PWR_SOUTH_Y), (vcc[0], PWR_SOUTH_Y), vcc],
            TRACK_DECO,
            "5V_LOGIC",
        )
    )

    # C_AHCT decoupling — short local links at U2 only
    raw.append(([vcc, (vcc[0], c_v[1]), c_v], TRACK_DECO, "5V_LOGIC"))
    raw.append(([gnd, (gnd[0], c_g[1]), c_g], TRACK_DECO, "GND"))

    lines: list[str] = []
    for paths, width, net in raw:
        for x1, y1, x2, y2 in _route_45(paths):
            if _crosses_esp_interior(x1, y1, x2, y2):
                raise RuntimeError(f"Route {net} crosses ESP keep-out")
            lines.append(_seg(x1, y1, x2, y2, width, nid(net)))

    return "".join(lines)


# Back-compat aliases
build_led_data_routing = build_placeholder_routing
build_visible_routing = build_placeholder_routing
