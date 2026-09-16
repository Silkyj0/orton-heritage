from pathlib import Path
from PIL import Image, ImageDraw

ASSETS = Path("assets")
BG = (64, 63, 44, 255)       # #403F2C
FG = (243, 241, 196, 255)    # #F3F1C4


def icon_image(size: int) -> Image.Image:
    scale = 4
    canvas = size * scale
    image = Image.new("RGBA", (canvas, canvas), BG)
    draw = ImageDraw.Draw(image)

    def p(x, y):
        return (round(x / 64 * canvas), round(y / 64 * canvas))

    width = max(1, round(3 / 64 * canvas))

    draw.line([p(10, 29), p(32, 13), p(54, 29)], fill=FG, width=width, joint="curve")
    draw.line([p(15, 29), p(49, 29)], fill=FG, width=width)
    draw.line([p(18, 29), p(18, 48)], fill=FG, width=width)
    draw.line([p(46, 29), p(46, 48)], fill=FG, width=width)
    draw.line([p(18, 40), p(46, 40)], fill=FG, width=width)
    draw.line([p(14, 49), p(50, 49)], fill=FG, width=width)
    draw.line([p(18, 49), p(18, 54)], fill=FG, width=width)
    draw.line([p(46, 49), p(46, 54)], fill=FG, width=width)

    return image.resize((size, size), Image.Resampling.LANCZOS)


favicon = icon_image(32)
favicon.save(ASSETS / "favicon-32.png", "PNG", optimize=True)
print(f"Wrote {ASSETS / 'favicon-32.png'}")

apple = icon_image(180)
apple.save("apple-touch-icon.png", "PNG", optimize=True)
print("Wrote apple-touch-icon.png")
