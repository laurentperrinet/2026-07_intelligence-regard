"""Compose the six retino panels into a 2 x 3 grid for the article.

The script resolves its input and output paths from its own location, so it
can be run from any directory::

    python content/images/compose_retino.py

It reads ``2026-08-28_retino.jpg`` (an 8811 x 2200 px strip of six panels)
and writes ``2026-11-18_retino_v2.png`` next to it. Re-running it regenerates
the same pixels: the crops are fixed coordinates, not detected ones.

Args (none): the script takes no command-line arguments.
Output: a 16.18 cm x 10.00 cm RGBA PNG at 200 px/cm (about 508 dpi).
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SRC = HERE / "2026-08-28_retino.jpg"
DST = HERE / "2026-11-18_retino_v2.png"
FONT = Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf")

# Canvas: the golden ratio (16.18 / 10.00 ~ 1.618) in centimetres, rendered at
# a fixed pixel density so that the sizes stay consistent across exports.
PX_PER_CM = 200
INCH_PER_CM = 1 / 2.54  # conversion constant for the PNG dpi metadata only
W = round(16.18 * PX_PER_CM)  # 3236 px
H = round(10.00 * PX_PER_CM)  # 2000 px

MARGIN = 60  # outer margin around the grid (px)
GAP = 50  # gap between cells, horizontal and vertical (px)
LABEL_BAND = 82  # height reserved at the top of each cell for its label (px)
ROW_H = (1150, 680)  # cell heights of the two rows (px); 1150 + 680 = H - 2 * MARGIN - GAP
LABEL_SIZE = 64  # font size of the panel labels (px)
LABEL_COLOUR = (20, 20, 20, 255)

# Factor from the preview coordinates used to choose the crops to the original
# 8811 px wide source. The crops were measured on the preview, so this constant
# must stay as it is for the output to match.
K = 4.41


def scaled_box(x0, y0, x1, y1):
    """Convert a box read on the preview into original pixel coordinates.

    Args:
        x0 (float): left edge on the preview (px).
        y0 (float): top edge on the preview (px).
        x1 (float): right edge on the preview (px).
        y1 (float): bottom edge on the preview (px).

    Returns:
        tuple[int, int, int, int]: the box (left, top, right, bottom) in
        original source pixels.
    """
    return tuple(int(round(v * K)) for v in (x0, y0, x1, y1))


def load_panels(src):
    """Crop the six panels from the source strip, in reading order.

    Args:
        src (Path): path to the 8811 x 2200 px source JPEG.

    Returns:
        list[PIL.Image.Image]: the panels (a) to (f), as RGB images.
    """
    im = Image.open(src).convert("RGB")
    cat = im.crop(scaled_box(0, 0, 385, 499))
    eye = im.crop(scaled_box(435, 115, 655, 283))
    # The fundus is cropped to its disc: the thin frame stays as an annotation,
    # and the tight crop removes the dark corner and grey shadow at bottom right.
    fundus = im.crop(scaled_box(675, 22, 1108, 455))
    fundus = fundus.crop((80, 75, 1840, 1835))
    brain = im.crop(scaled_box(1135, 90, 1450, 355))
    zoom_top = im.crop(scaled_box(1537, 22, 1987, 247))
    zoom_bottom = im.crop(scaled_box(1535, 260, 1985, 478))
    return [cat, eye, fundus, brain, zoom_top, zoom_bottom]


def fit(img, box_w, box_h):
    """Scale an image to fit inside a box, keeping its aspect ratio.

    Args:
        img (PIL.Image.Image): the image to scale.
        box_w (int): maximum width (px).
        box_h (int): maximum height (px).

    Returns:
        PIL.Image.Image: the resized image, using LANCZOS resampling.
    """
    scale = min(box_w / img.width, box_h / img.height)
    size = (round(img.width * scale), round(img.height * scale))
    return img.resize(size, Image.LANCZOS)


def main():
    """Build the grid and write the PNG next to this script."""
    panels = load_panels(SRC)
    labels = ["(a)", "(b)", "(c)", "(d)", "(e)", "(f)"]

    cell_w = (W - 2 * MARGIN - 2 * GAP) // 3
    row_y = [MARGIN, MARGIN + ROW_H[0] + GAP]

    # A transparent canvas keeps the figure usable on any page background.
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(str(FONT), LABEL_SIZE)

    for i, (panel, label) in enumerate(zip(panels, labels)):
        row, col = divmod(i, 3)
        x0 = MARGIN + col * (cell_w + GAP)
        y0 = row_y[row]
        cell_h = ROW_H[row]

        # Labels sit at the top-left of each cell, so they align along each row.
        draw.text((x0, y0), label, font=font, fill=LABEL_COLOUR)

        # The image fits below the label band, top-aligned and horizontally centred.
        box_h = cell_h - LABEL_BAND
        scaled = fit(panel, cell_w, box_h).convert("RGBA")
        px = x0 + (cell_w - scaled.width) // 2
        py = y0 + LABEL_BAND
        canvas.alpha_composite(scaled, (px, py))

        print(f"{label}: source {panel.size} -> placed {scaled.size} at ({px}, {py})")

    dpi = PX_PER_CM / INCH_PER_CM
    canvas.save(DST, dpi=(dpi, dpi), optimize=True)
    print("saved", DST, canvas.size)


if __name__ == "__main__":
    main()
