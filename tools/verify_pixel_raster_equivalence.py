#!/usr/bin/env python3
"""Verify current raster-bound pixel assets against Kotlin PixelSprite masters.

This tool is intentionally narrow and deterministic. It parses the literal PixelSprite
forms currently used by PixelAssetCatalog.kt and PixelSceneCatalog.kt, decodes PNG files
with the Python standard library, and compares native RGBA pixels.

It does not attempt to parse arbitrary Kotlin or act as a production art exporter.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import struct
import zlib
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
TRANSPARENT = (0, 0, 0, 0)

ASSET_SOURCE = Path(
    "android/app/src/main/java/com/thegame/rpg/ui/PixelAssetCatalog.kt"
)
SCENE_SOURCE = Path(
    "android/app/src/main/java/com/thegame/rpg/ui/PixelSceneCatalog.kt"
)
THEME_SOURCE = Path(
    "android/app/src/main/java/com/thegame/rpg/ui/PixelTheme.kt"
)
BINDING_EVIDENCE = Path("docs/evidence/raster_bindings_2026-10-02.json")
LINEAGE_EVIDENCE = Path("docs/evidence/raster_export_lineage_2026-10-03.json")


@dataclass(frozen=True)
class PixelSpriteMaster:
    declaration: str
    constant_name: str
    asset_id: str
    width: int
    height: int
    palette: dict[str, tuple[int, int, int, int]]
    rows: tuple[str, ...]

    def rgba_pixels(self) -> list[tuple[int, int, int, int]]:
        pixels: list[tuple[int, int, int, int]] = []
        for row in self.rows:
            for key in row:
                if key == ".":
                    pixels.append(TRANSPARENT)
                else:
                    pixels.append(self.palette[key])
        return pixels


def git_blob_sha1(content: bytes) -> str:
    header = f"blob {len(content)}\0".encode("ascii")
    return hashlib.sha1(header + content).hexdigest()


def _extract_parenthesized(text: str, open_index: int) -> tuple[str, int]:
    if open_index >= len(text) or text[open_index] != "(":
        raise ValueError(f"Expected '(' at index {open_index}")

    depth = 0
    quote: str | None = None
    escaped = False

    for index in range(open_index, len(text)):
        char = text[index]

        if quote is not None:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            continue

        if char in {'"', "'"}:
            quote = char
            continue

        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return text[open_index + 1 : index], index

    raise ValueError(f"Unclosed parenthesized expression at index {open_index}")


def _extract_named_call_body(body: str, name_pattern: str) -> str:
    match = re.search(name_pattern + r"\s*\(", body)
    if not match:
        raise ValueError(f"Missing call matching {name_pattern!r}")
    open_index = match.end() - 1
    call_body, _ = _extract_parenthesized(body, open_index)
    return call_body


def _argb_hex_to_rgba(value: str) -> tuple[int, int, int, int]:
    if len(value) != 8:
        raise ValueError(f"Expected 8-digit AARRGGBB value, found {value!r}")
    number = int(value, 16)
    alpha = (number >> 24) & 0xFF
    red = (number >> 16) & 0xFF
    green = (number >> 8) & 0xFF
    blue = number & 0xFF
    return red, green, blue, alpha


def parse_pixel_colors(theme_text: str) -> dict[str, tuple[int, int, int, int]]:
    colors: dict[str, tuple[int, int, int, int]] = {}
    for name, value in re.findall(
        r"\bval\s+([A-Za-z0-9_]+)\s*=\s*Color\(0x([0-9A-Fa-f]{8})\)",
        theme_text,
    ):
        colors[name] = _argb_hex_to_rgba(value)

    if not colors:
        raise ValueError("No PixelColors Color(0xAARRGGBB) values found")
    return colors


def _resolve_color(
    expression: str,
    pixel_colors: dict[str, tuple[int, int, int, int]],
) -> tuple[int, int, int, int]:
    expression = expression.strip()

    direct = re.fullmatch(r"Color\(0x([0-9A-Fa-f]{8})\)", expression)
    if direct:
        return _argb_hex_to_rgba(direct.group(1))

    named = re.fullmatch(r"PixelColors\.([A-Za-z0-9_]+)", expression)
    if named:
        name = named.group(1)
        try:
            return pixel_colors[name]
        except KeyError as exc:
            raise ValueError(f"Unknown PixelColors.{name}") from exc

    raise ValueError(f"Unsupported palette expression: {expression!r}")


def parse_pixel_sprite_masters(
    source_text: str,
    pixel_colors: dict[str, tuple[int, int, int, int]],
) -> dict[str, PixelSpriteMaster]:
    constants = dict(
        re.findall(
            r"\bconst\s+val\s+([A-Za-z0-9_]+)\s*=\s*\"([^\"]+)\"",
            source_text,
        )
    )

    declaration_pattern = re.compile(
        r"\b(?:private\s+)?val\s+([A-Za-z0-9_]+)\s*=\s*PixelSprite\s*\("
    )
    masters: dict[str, PixelSpriteMaster] = {}

    for declaration_match in declaration_pattern.finditer(source_text):
        declaration = declaration_match.group(1)
        body, _ = _extract_parenthesized(source_text, declaration_match.end() - 1)

        asset_match = re.search(r"\bassetId\s*=\s*([^,\n]+)", body)
        width_match = re.search(r"\bwidth\s*=\s*(\d+)", body)
        height_match = re.search(r"\bheight\s*=\s*(\d+)", body)
        if not asset_match or not width_match or not height_match:
            raise ValueError(f"Incomplete PixelSprite declaration {declaration}")

        asset_expression = asset_match.group(1).strip()
        if re.fullmatch(r'"[^"]+"', asset_expression):
            constant_name = ""
            asset_id = asset_expression[1:-1]
        else:
            constant_name = asset_expression
            if constant_name not in constants:
                raise ValueError(
                    f"{declaration} references unknown asset constant {constant_name!r}"
                )
            asset_id = constants[constant_name]

        palette_body = _extract_named_call_body(body, r"\bpalette\s*=\s*mapOf")
        palette: dict[str, tuple[int, int, int, int]] = {}
        palette_pattern = re.compile(
            r"'((?:\\.|[^'])+)'\s+to\s+([^,\n]+)"
        )
        for key_text, expression in palette_pattern.findall(palette_body):
            if key_text.startswith("\\") and len(key_text) == 2:
                key = key_text[1]
            else:
                key = key_text
            if len(key) != 1:
                raise ValueError(
                    f"{declaration} has unsupported palette key {key_text!r}"
                )
            palette[key] = _resolve_color(expression, pixel_colors)

        rows_body = _extract_named_call_body(body, r"\brows\s*=\s*listOf")
        rows = tuple(re.findall(r'"([^"]*)"', rows_body))

        width = int(width_match.group(1))
        height = int(height_match.group(1))
        if len(rows) != height:
            raise ValueError(
                f"{asset_id}: expected {height} rows, parsed {len(rows)}"
            )
        if any(len(row) != width for row in rows):
            bad = [index for index, row in enumerate(rows) if len(row) != width]
            raise ValueError(f"{asset_id}: row width mismatch at {bad[:8]}")

        used = {char for row in rows for char in row if char != "."}
        missing = sorted(used - palette.keys())
        if missing:
            raise ValueError(f"{asset_id}: missing palette keys {missing}")

        if constant_name:
            masters[constant_name] = PixelSpriteMaster(
                declaration=declaration,
                constant_name=constant_name,
                asset_id=asset_id,
                width=width,
                height=height,
                palette=palette,
                rows=rows,
            )

    if not masters:
        raise ValueError("No constant-backed PixelSprite declarations parsed")
    return masters


def _paeth_predictor(left: int, up: int, upper_left: int) -> int:
    estimate = left + up - upper_left
    left_distance = abs(estimate - left)
    up_distance = abs(estimate - up)
    upper_left_distance = abs(estimate - upper_left)
    if left_distance <= up_distance and left_distance <= upper_left_distance:
        return left
    if up_distance <= upper_left_distance:
        return up
    return upper_left


def decode_png_rgba(
    content: bytes,
) -> tuple[int, int, list[tuple[int, int, int, int]]]:
    if not content.startswith(PNG_SIGNATURE):
        raise ValueError("Invalid PNG signature")

    position = len(PNG_SIGNATURE)
    ihdr: tuple[int, int, int, int, int, int, int] | None = None
    palette: list[tuple[int, int, int]] | None = None
    transparency: bytes | None = None
    idat = bytearray()

    while position < len(content):
        if position + 12 > len(content):
            raise ValueError("Truncated PNG chunk")

        length = struct.unpack(">I", content[position : position + 4])[0]
        chunk_type = content[position + 4 : position + 8]
        data_start = position + 8
        data_end = data_start + length
        crc_end = data_end + 4
        if crc_end > len(content):
            raise ValueError("Truncated PNG chunk payload")

        data = content[data_start:data_end]
        stored_crc = struct.unpack(">I", content[data_end:crc_end])[0]
        actual_crc = zlib.crc32(chunk_type)
        actual_crc = zlib.crc32(data, actual_crc) & 0xFFFFFFFF
        if stored_crc != actual_crc:
            raise ValueError(
                f"PNG CRC mismatch in {chunk_type.decode('ascii', errors='replace')}"
            )

        if chunk_type == b"IHDR":
            if length != 13:
                raise ValueError("Invalid IHDR length")
            ihdr = struct.unpack(">IIBBBBB", data)
        elif chunk_type == b"PLTE":
            if len(data) % 3:
                raise ValueError("Invalid PLTE length")
            palette = [
                tuple(data[index : index + 3])
                for index in range(0, len(data), 3)
            ]
        elif chunk_type == b"tRNS":
            transparency = data
        elif chunk_type == b"IDAT":
            idat.extend(data)
        elif chunk_type == b"IEND":
            break

        position = crc_end

    if ihdr is None:
        raise ValueError("PNG has no IHDR")
    if not idat:
        raise ValueError("PNG has no IDAT")

    width, height, bit_depth, color_type, compression, filter_method, interlace = ihdr
    if bit_depth != 8:
        raise ValueError(f"Only 8-bit PNGs are supported, found {bit_depth}")
    if compression != 0 or filter_method != 0:
        raise ValueError("Unsupported PNG compression/filter method")
    if interlace != 0:
        raise ValueError("Interlaced PNGs are not supported")

    channels_by_type = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}
    try:
        bytes_per_pixel = channels_by_type[color_type]
    except KeyError as exc:
        raise ValueError(f"Unsupported PNG color type {color_type}") from exc

    row_size = width * bytes_per_pixel
    raw = zlib.decompress(bytes(idat))
    expected_length = height * (row_size + 1)
    if len(raw) != expected_length:
        raise ValueError(
            f"Unexpected decompressed PNG size: {len(raw)} != {expected_length}"
        )

    rows: list[bytes] = []
    previous = bytearray(row_size)
    cursor = 0

    for _ in range(height):
        filter_type = raw[cursor]
        cursor += 1
        filtered = raw[cursor : cursor + row_size]
        cursor += row_size
        reconstructed = bytearray(row_size)

        for index, value in enumerate(filtered):
            left = reconstructed[index - bytes_per_pixel] if index >= bytes_per_pixel else 0
            up = previous[index]
            upper_left = previous[index - bytes_per_pixel] if index >= bytes_per_pixel else 0

            if filter_type == 0:
                decoded = value
            elif filter_type == 1:
                decoded = (value + left) & 0xFF
            elif filter_type == 2:
                decoded = (value + up) & 0xFF
            elif filter_type == 3:
                decoded = (value + ((left + up) // 2)) & 0xFF
            elif filter_type == 4:
                decoded = (
                    value + _paeth_predictor(left, up, upper_left)
                ) & 0xFF
            else:
                raise ValueError(f"Unsupported PNG row filter {filter_type}")

            reconstructed[index] = decoded

        rows.append(bytes(reconstructed))
        previous = reconstructed

    rgba: list[tuple[int, int, int, int]] = []

    for row in rows:
        for offset in range(0, len(row), bytes_per_pixel):
            if color_type == 6:
                red, green, blue, alpha = row[offset : offset + 4]
            elif color_type == 2:
                red, green, blue = row[offset : offset + 3]
                alpha = 255
            elif color_type == 0:
                gray = row[offset]
                red = green = blue = gray
                alpha = 255
            elif color_type == 4:
                gray, alpha = row[offset : offset + 2]
                red = green = blue = gray
            else:
                if palette is None:
                    raise ValueError("Indexed PNG has no PLTE")
                palette_index = row[offset]
                if palette_index >= len(palette):
                    raise ValueError(f"PLTE index out of range: {palette_index}")
                red, green, blue = palette[palette_index]
                alpha = (
                    transparency[palette_index]
                    if transparency is not None and palette_index < len(transparency)
                    else 255
                )

            if alpha == 0:
                rgba.append(TRANSPARENT)
            else:
                rgba.append((red, green, blue, alpha))

    return width, height, rgba


def _png_chunk(chunk_type: bytes, data: bytes) -> bytes:
    crc = zlib.crc32(chunk_type)
    crc = zlib.crc32(data, crc) & 0xFFFFFFFF
    return (
        struct.pack(">I", len(data))
        + chunk_type
        + data
        + struct.pack(">I", crc)
    )


def encode_png_rgba(
    width: int,
    height: int,
    pixels: list[tuple[int, int, int, int]],
) -> bytes:
    if width <= 0 or height <= 0:
        raise ValueError("PNG dimensions must be positive")
    if len(pixels) != width * height:
        raise ValueError(
            f"Pixel count mismatch: {len(pixels)} != {width * height}"
        )

    scanlines = bytearray()
    for y in range(height):
        scanlines.append(0)  # PNG filter type 0: None
        start = y * width
        for red, green, blue, alpha in pixels[start : start + width]:
            scanlines.extend((red, green, blue, alpha))

    ihdr = struct.pack(
        ">IIBBBBB",
        width,
        height,
        8,  # bit depth
        6,  # RGBA
        0,  # compression
        0,  # filter method
        0,  # no interlace
    )
    compressed = zlib.compress(bytes(scanlines), level=9)
    return (
        PNG_SIGNATURE
        + _png_chunk(b"IHDR", ihdr)
        + _png_chunk(b"IDAT", compressed)
        + _png_chunk(b"IEND", b"")
    )


def _load_source_masters(
    root: Path,
) -> tuple[dict[Path, dict[str, PixelSpriteMaster]], dict]:
    theme_text = (root / THEME_SOURCE).read_text(encoding="utf-8")
    pixel_colors = parse_pixel_colors(theme_text)
    source_masters = {
        ASSET_SOURCE: parse_pixel_sprite_masters(
            (root / ASSET_SOURCE).read_text(encoding="utf-8"),
            pixel_colors,
        ),
        SCENE_SOURCE: parse_pixel_sprite_masters(
            (root / SCENE_SOURCE).read_text(encoding="utf-8"),
            pixel_colors,
        ),
    }
    bindings = json.loads((root / BINDING_EVIDENCE).read_text(encoding="utf-8"))
    return source_masters, bindings


def export_repository_rasters(root: Path, destination: Path) -> dict:
    root = root.resolve()
    destination = destination.resolve()
    if destination == root:
        raise ValueError(
            "Refusing to export directly onto the repository root; "
            "use a separate --export-dir."
        )

    source_masters, bindings = _load_source_masters(root)
    exported: list[dict] = []

    for binding in bindings["assets"]:
        asset_symbol = binding["asset_symbol"]
        source_path = _asset_source_path(asset_symbol)
        constant_name = asset_symbol.split(".", 1)[1]
        try:
            master = source_masters[source_path][constant_name]
        except KeyError as exc:
            raise ValueError(
                f"{binding['path']}: no parsed source master for {asset_symbol}"
            ) from exc

        relative_path = Path(binding["path"])
        output_path = destination / relative_path
        output_path.parent.mkdir(parents=True, exist_ok=True)

        payload = encode_png_rgba(
            master.width,
            master.height,
            master.rgba_pixels(),
        )
        output_path.write_bytes(payload)

        exported.append(
            {
                "path": relative_path.as_posix(),
                "asset_symbol": asset_symbol,
                "asset_id": master.asset_id,
                "width": master.width,
                "height": master.height,
                "sha256": hashlib.sha256(payload).hexdigest(),
                "bytes": len(payload),
            }
        )

    return {
        "status": "PASS",
        "root": str(root),
        "destination": str(destination),
        "asset_count": len(exported),
        "assets": exported,
        "notes": [
            "Exports are deterministic 8-bit RGBA PNGs with filter type 0 and zlib level 9.",
            "Export bytes need not match historical PNG compression/chunk layout; decoded source pixels are authoritative.",
            "The exporter writes only under the explicit destination tree and refuses the repository root.",
        ],
    }


def _asset_source_path(asset_symbol: str) -> Path:
    if asset_symbol.startswith("PixelAssetCatalog."):
        return ASSET_SOURCE
    if asset_symbol.startswith("PixelSceneCatalog."):
        return SCENE_SOURCE
    raise ValueError(f"Unsupported asset symbol owner: {asset_symbol}")


def verify_repository(root: Path) -> dict:
    root = root.resolve()

    source_masters, bindings = _load_source_masters(root)
    lineage = json.loads((root / LINEAGE_EVIDENCE).read_text(encoding="utf-8"))
    lineage_by_path = {entry["path"]: entry for entry in lineage["assets"]}

    results: list[dict] = []
    total_pixel_mismatches = 0

    for binding in bindings["assets"]:
        path = Path(binding["path"])
        asset_symbol = binding["asset_symbol"]
        source_path = _asset_source_path(asset_symbol)
        constant_name = asset_symbol.split(".", 1)[1]

        try:
            master = source_masters[source_path][constant_name]
        except KeyError as exc:
            raise ValueError(
                f"{path}: no parsed source master for {asset_symbol}"
            ) from exc

        raster_bytes = (root / path).read_bytes()
        png_width, png_height, actual_pixels = decode_png_rgba(raster_bytes)
        expected_pixels = master.rgba_pixels()

        if (png_width, png_height) != (master.width, master.height):
            dimension_match = False
            pixel_mismatches = max(len(actual_pixels), len(expected_pixels))
            first_mismatches: list[dict] = []
        else:
            dimension_match = True
            first_mismatches = []
            pixel_mismatches = 0
            for index, (expected, actual) in enumerate(
                zip(expected_pixels, actual_pixels)
            ):
                if expected == actual:
                    continue
                pixel_mismatches += 1
                if len(first_mismatches) < 8:
                    first_mismatches.append(
                        {
                            "x": index % master.width,
                            "y": index // master.width,
                            "expected": list(expected),
                            "actual": list(actual),
                        }
                    )

        total_pixel_mismatches += pixel_mismatches

        sha256 = hashlib.sha256(raster_bytes).hexdigest()
        blob_sha = git_blob_sha1(raster_bytes)
        lineage_entry = lineage_by_path.get(path.as_posix())

        source_bytes = (root / source_path).read_bytes()
        source_blob = git_blob_sha1(source_bytes)

        results.append(
            {
                "path": path.as_posix(),
                "asset_symbol": asset_symbol,
                "asset_id": master.asset_id,
                "source_file": source_path.as_posix(),
                "source_blob": source_blob,
                "dimensions": [png_width, png_height],
                "dimension_match": dimension_match,
                "sha256": sha256,
                "sha256_matches_evidence": sha256 == binding["sha256"],
                "git_blob": blob_sha,
                "git_blob_matches_evidence": blob_sha == binding["git_blob"],
                "lineage_source_blob_matches": (
                    lineage_entry is not None
                    and source_blob == lineage_entry["current_source_blob"]
                ),
                "pixel_mismatches": pixel_mismatches,
                "first_mismatches": first_mismatches,
                "pixel_match": dimension_match and pixel_mismatches == 0,
            }
        )

    expected_count = 24
    checks = {
        "asset_count_is_24": len(results) == expected_count,
        "all_dimensions_match": all(item["dimension_match"] for item in results),
        "all_sha256_match_evidence": all(
            item["sha256_matches_evidence"] for item in results
        ),
        "all_git_blobs_match_evidence": all(
            item["git_blob_matches_evidence"] for item in results
        ),
        "all_lineage_source_blobs_match": all(
            item["lineage_source_blob_matches"] for item in results
        ),
        "all_pixels_match_source": all(item["pixel_match"] for item in results),
    }

    status = "PASS" if all(checks.values()) else "FAIL"

    return {
        "status": status,
        "root": str(root),
        "asset_count": len(results),
        "matched_assets": sum(1 for item in results if item["pixel_match"]),
        "total_pixel_mismatches": total_pixel_mismatches,
        "checks": checks,
        "assets": results,
        "notes": [
            "Transparent PNG pixels are canonicalized to RGBA 0,0,0,0 before comparison.",
            "The parser supports only the literal PixelSprite/Color forms used by the audited catalogs.",
            "This verifies current raster/source equivalence; it is not a general Kotlin parser or authoring exporter.",
        ],
    }


def _summarize_failures(report: dict) -> Iterable[str]:
    for asset in report["assets"]:
        if (
            asset["pixel_match"]
            and asset["sha256_matches_evidence"]
            and asset["git_blob_matches_evidence"]
            and asset["lineage_source_blob_matches"]
        ):
            continue
        yield (
            f"{asset['path']}: pixel_match={asset['pixel_match']} "
            f"pixel_mismatches={asset['pixel_mismatches']} "
            f"sha256_evidence={asset['sha256_matches_evidence']} "
            f"git_blob_evidence={asset['git_blob_matches_evidence']} "
            f"source_blob_lineage={asset['lineage_source_blob_matches']}"
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--output", help="Optional JSON verification output path")
    parser.add_argument(
        "--export-dir",
        help=(
            "Optional separate directory where deterministic source-native PNG "
            "reconstructions are written."
        ),
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress PASS output; failures still print",
    )
    args = parser.parse_args()

    root = Path(args.root)
    report = verify_repository(root)
    payload = json.dumps(report, indent=2, sort_keys=True)

    if args.output:
        Path(args.output).write_text(payload + "\n", encoding="utf-8")

    export_report = None
    if args.export_dir:
        export_report = export_repository_rasters(root, Path(args.export_dir))

    if report["status"] == "PASS":
        if not args.quiet:
            print(
                f"PASS: {report['matched_assets']}/{report['asset_count']} "
                "raster assets match current source pixels and evidence."
            )
            if export_report is not None:
                print(
                    f"EXPORTED: {export_report['asset_count']} deterministic "
                    f"source-native PNGs to {export_report['destination']}."
                )
        return 0

    print("FAIL: pixel raster equivalence verification failed.")
    for line in _summarize_failures(report):
        print(line)
    if not args.output and not args.quiet:
        print(payload)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
