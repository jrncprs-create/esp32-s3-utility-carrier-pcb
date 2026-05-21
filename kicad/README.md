# KiCad project — ESP32-S3 Utility Carrier v1 (placeholder)

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
| `esp32-s3-utility-carrier.kicad_pcb` | Placeholder PCB (130×85 mm, zone layout v0.5) |
| `libraries/carrier.kicad_sym` | F_ESP, SN74AHCT125N, SJ_SERVO |
| `libraries/carrier.pretty/` | Placeholder footprints |

Regenerate (optional): `python3 tools/generate_placeholder.py`

See `../docs/kicad-next-steps.md` and `../hardware/measurements.md`.
