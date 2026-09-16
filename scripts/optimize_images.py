from pathlib import Path
from PIL import Image

IMAGE_DIR = Path("assets/images")
WIDTHS = (900, 1500, 2200)
QUALITY = 84

for source in sorted(IMAGE_DIR.glob("place-*.jpg")):
    stem = source.stem
    with Image.open(source) as image:
        image = image.convert("RGB")
        source_width, source_height = image.size

        for width in WIDTHS:
            target_width = min(width, source_width)
            target_height = round(source_height * target_width / source_width)
            output = IMAGE_DIR / f"{stem}-{width}.webp"

            if target_width == source_width:
                resized = image
            else:
                resized = image.resize((target_width, target_height), Image.Resampling.LANCZOS)

            resized.save(
                output,
                "WEBP",
                quality=QUALITY,
                method=6,
                optimize=True,
            )
            print(f"Wrote {output} ({target_width}x{target_height})")
