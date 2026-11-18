"""Translate the English labels of the What-Where figure into French.

The source is the publication figure ``jeremie-25-ccn/featured.jpg``, saved
in this folder as ``2026-11-18_modele.jpg`` (3344 x 1930 px, white background).
The script erases its English labels and redraws the French ones in a larger,
bolder font, so that they stay legible at article size. Its arrows are redrawn
in one style (same dash pattern, shaft width and arrowhead), since the originals
differed in weight and dash length. The photos and dashed frames are not modified.

The script resolves its paths from its own location, so it can be run from
any directory::

    python content/images/compose_modele_fr.py

Args (none): the script takes no command-line arguments.
Output: ``2026-11-18_modele_fr.png``, same size as the source, white background.
"""

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SRC = HERE / "2026-11-18_modele.jpg"
DST = HERE / "2026-11-18_modele_fr.png"
FONT_REG = Path("/System/Library/Fonts/Supplemental/Arial.ttf")
FONT_BOLD = Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf")

# Label sizes in original pixels. The source labels are about 22 px tall on the
# 2000 px preview, so 40 px here is a visible increase.
LABEL_SIZE = 40
TITLE_SIZE = 46
LINE_SPACING = 1.25  # line height, as a multiple of the label size
TEXT_COLOUR = (0, 0, 0)
PREVIEW_W = 2000  # width of the preview on which the coordinates were read

# Panels in preview coordinates: letter centre, label lines, first line centre,
# and the erase box that covers the English label (x0, y0, x1, y1).
PANELS = [
    dict(letter="A", lx=275, ly=800, lines=["Scène naturelle"], ty=835,
         erase=(120, 785, 430, 852)),
    dict(letter="B", lx=676, ly=158, lines=["Entrée rétinotopique", "dorsale"], ty=184,
         erase=(520, 150, 830, 236)),
    dict(letter="C", lx=1058, ly=158, lines=["Carte de saillance", "polaire"], ty=184,
         erase=(918, 150, 1198, 236)),
    dict(letter="D", lx=1436, ly=158, lines=["Traitement", "de la saillance"], ty=184,
         erase=(1296, 150, 1576, 236)),
    dict(letter="E", lx=1780, ly=800, lines=["Système saccadique"], ty=835,
         erase=(1640, 785, 1925, 848)),
    dict(letter="F", lx=1436, ly=640, lines=["Nouvelle position", "ventrale"], ty=664,
         erase=(1296, 630, 1574, 712)),
    dict(letter="G", lx=1062, ly=640, lines=["Entrée rétinotopique", "fovéale"], ty=664,
         erase=(898, 628, 1228, 712)),
    dict(letter="H", lx=676, ly=640, lines=["Classification", "de l’image"], ty=664,
         erase=(536, 630, 816, 712)),
]

# Titles of the two pathways, in preview coordinates.
TITLES = [
    dict(text="Voie « où »", cx=1058, cy=80, erase=(930, 40, 1190, 120)),
    dict(text="Voie « quoi »", cx=1050, cy=1088, erase=(940, 1050, 1180, 1130)),
]


def to_original(x, y, k):
    """Convert a point read on the preview into original pixel coordinates.

    Args:
        x (float): horizontal position on the preview (px).
        y (float): vertical position on the preview (px).
        k (float): preview-to-original factor (original width / preview width).

    Returns:
        tuple[float, float]: the point in original pixels.
    """
    return x * k, y * k


def erase(draw, box, k):
    """Paint a preview-space box white, to remove the English label beneath it.

    Args:
        draw (PIL.ImageDraw.ImageDraw): drawing context of the canvas.
        box (tuple[int, int, int, int]): box (x0, y0, x1, y1) on the preview.
        k (float): preview-to-original factor.
    """
    x0, y0, x1, y1 = box
    draw.rectangle([x0 * k, y0 * k, x1 * k, y1 * k], fill=(255, 255, 255))


# Arrows, in preview coordinates. Each entry is a polyline, or a quadratic
# Bezier curve given by its start, control and end points; the last point is
# the tip of the arrowhead. The boxes in ARROW_ERASE remove the old arrows,
# which lie on white background, before the new ones are drawn.
ARROW_ERASE = [
    (280, 236, 516, 347),    # A to B, curved
    (812, 366, 918, 390),    # B to C
    (1199, 364, 1298, 388),  # C to D
    (1603, 236, 1795, 412),  # E, curve down onto the saccade panel
    (1586, 848, 1795, 964),  # E to F, lower curve
    (1206, 860, 1300, 884),  # F to G
    (738, 860, 918, 884),    # G to H
]
ARROWS = [
    [(290, 342), (330, 236), (512, 252)],    # A to B (quadratic Bezier)
    [(818, 378), (912, 378)],                # B to C
    [(1199, 375), (1294, 375)],              # C to D
    [(1612, 268), (1745, 236), (1780, 410)], # E, down onto the saccade panel
    [(1782, 860), (1775, 950), (1590, 936)], # E to F
    [(1300, 872), (1208, 872)],              # F to G
    [(920, 872), (742, 872)],                # G to H
]

ARROW_WIDTH = 6  # shaft width (px, original scale)
HEAD_LEN = 26  # arrowhead length (px)
HEAD_HALF = 12  # arrowhead half-width (px)
DASH_ON = 24  # dash length (px)
DASH_OFF = 14  # gap length (px)
SUPERSAMPLE = 4  # arrows are drawn at 4x and reduced, for smooth edges
ARROW_COLOUR = (0, 0, 0, 255)


def bezier(p0, p1, p2, n=80):
    """Sample a quadratic Bezier curve.

    Args:
        p0 (tuple[float, float]): start point (preview px).
        p1 (tuple[float, float]): control point (preview px).
        p2 (tuple[float, float]): end point (preview px).
        n (int): number of segments in the sampled polyline.

    Returns:
        list[tuple[float, float]]: n + 1 points along the curve.
    """
    pts = []
    for i in range(n + 1):
        t = i / n
        a, b, c = (1 - t) ** 2, 2 * (1 - t) * t, t * t
        pts.append((a * p0[0] + b * p1[0] + c * p2[0], a * p0[1] + b * p1[1] + c * p2[1]))
    return pts


def dash_segments(points, on, off):
    """Split a polyline into dashes of a given on/off length.

    Args:
        points (list[tuple[float, float]]): polyline, in pixels.
        on (float): length of each dash (px).
        off (float): length of each gap (px).

    Returns:
        list[list[tuple[float, float]]]: the dashes, each with at least two points.
    """
    segs = []
    drawing = True
    remaining = on
    cur = [points[0]]
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        seg_len = math.hypot(x1 - x0, y1 - y0)
        pos = 0.0
        while seg_len - pos > 1e-9:
            step = min(remaining, seg_len - pos)
            pos += step
            remaining -= step
            t = pos / seg_len
            p = (x0 + (x1 - x0) * t, y0 + (y1 - y0) * t)
            if drawing:
                cur.append(p)
            if remaining <= 1e-9:
                if drawing:
                    segs.append(cur)
                    cur = []
                    drawing = False
                    remaining = off
                else:
                    drawing = True
                    remaining = on
                    cur = [p]
    if drawing and len(cur) > 1:
        segs.append(cur)
    return segs


def draw_arrow(im, points, k):
    """Draw one dashed arrow with a filled head onto the image, in place.

    The arrow is rendered on a supersampled transparent layer, then reduced,
    so its edges are smooth. The layer covers only the arrow's bounding box.

    Args:
        im (PIL.Image.Image): RGB canvas, modified in place.
        points (list[tuple[float, float]]): polyline on the preview; the last
            point is the arrowhead tip.
        k (float): preview-to-original factor.
    """
    if len(points) == 3:  # start, control, end: a curved arrow
        points = bezier(*points)
    pts = [(x * k, y * k) for x, y in points]
    (tx, ty), (qx, qy) = pts[-1], pts[-2]
    length = math.hypot(tx - qx, ty - qy)
    ux, uy = (tx - qx) / length, (ty - qy) / length  # unit vector towards the tip
    bx, by = tx - ux * HEAD_LEN, ty - uy * HEAD_LEN  # base of the arrowhead
    shaft = pts[:-1] + [(bx, by)]
    head = [
        (tx, ty),
        (bx - uy * HEAD_HALF, by + ux * HEAD_HALF),
        (bx + uy * HEAD_HALF, by - ux * HEAD_HALF),
    ]

    margin = 40
    x0 = int(min(p[0] for p in pts)) - margin
    y0 = int(min(p[1] for p in pts)) - margin
    x1 = int(max(p[0] for p in pts)) + margin
    y1 = int(max(p[1] for p in pts)) + margin
    w, h = x1 - x0, y1 - y0

    def to_layer(p):
        return ((p[0] - x0) * SUPERSAMPLE, (p[1] - y0) * SUPERSAMPLE)

    layer = Image.new("RGBA", (w * SUPERSAMPLE, h * SUPERSAMPLE), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    r = ARROW_WIDTH * SUPERSAMPLE / 2
    for dash in dash_segments(shaft, DASH_ON, DASH_OFF):
        d.line([to_layer(p) for p in dash], fill=ARROW_COLOUR, width=int(2 * r), joint="curve")
        for ex, ey in (to_layer(dash[0]), to_layer(dash[-1])):
            d.ellipse([ex - r, ey - r, ex + r, ey + r], fill=ARROW_COLOUR)  # round caps
    d.polygon([to_layer(p) for p in head], fill=ARROW_COLOUR)

    layer = layer.resize((w, h), Image.LANCZOS)
    region = im.crop((x0, y0, x1, y1)).convert("RGBA")
    region.alpha_composite(layer)
    im.paste(region.convert("RGB"), (x0, y0))


def apply_arrows(im, k):
    """Erase the original arrows and draw the new ones.

    Args:
        im (PIL.Image.Image): RGB canvas, modified in place.
        k (float): preview-to-original factor.
    """
    draw = ImageDraw.Draw(im)
    for box in ARROW_ERASE:
        erase(draw, box, k)
    for points in ARROWS:
        draw_arrow(im, points, k)


def main():
    """Erase the English labels and draw the French ones, then save the PNG."""
    im = Image.open(SRC).convert("RGB")
    k = im.width / PREVIEW_W
    draw = ImageDraw.Draw(im)

    reg = ImageFont.truetype(str(FONT_REG), LABEL_SIZE)
    bold = ImageFont.truetype(str(FONT_BOLD), TITLE_SIZE)
    line_h = LINE_SPACING * LABEL_SIZE

    for title in TITLES:
        erase(draw, title["erase"], k)
        x, y = to_original(title["cx"], title["cy"], k)
        draw.text((x, y), title["text"], font=bold, fill=TEXT_COLOUR, anchor="mm")

    for p in PANELS:
        erase(draw, p["erase"], k)
        x, y = to_original(p["lx"], p["ly"], k)
        draw.text((x, y), p["letter"], font=bold, fill=TEXT_COLOUR, anchor="mm")
        cx, _ = to_original(p["lx"], 0, k)
        _, ty = to_original(0, p["ty"], k)
        for i, line in enumerate(p["lines"]):
            draw.text((cx, ty + i * line_h), line, font=reg, fill=TEXT_COLOUR, anchor="mm")

    apply_arrows(im, k)
    im.save(DST, optimize=True)
    print("saved", DST, im.size)


if __name__ == "__main__":
    main()
