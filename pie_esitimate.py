from random import random
from PIL import Image, ImageDraw

IMAGE_SIZE = 500
img = Image.new("RGBA", (IMAGE_SIZE, IMAGE_SIZE))
img_draw = ImageDraw.Draw(img)
img_draw.arc((-500, -500, 500, 500), start=0, end=360, fill=(255, 0, 0), width=12)
img.save("base.png")

N = 100
N_in = 0
for i in range(N):
    x, y = random(), random()
    if x**2 + y**2 <= 1:
        img_draw.arc(
            (
                x * IMAGE_SIZE - 3,
                y * IMAGE_SIZE - 3,
                x * IMAGE_SIZE + 3,
                y * IMAGE_SIZE + 3,
            ),
            start=0,
            end=360,
            fill=(0, 255, 0),
            width=6,
        )
        N_in += 1
    else:
        img_draw.arc(
            (
                x * IMAGE_SIZE - 3,
                y * IMAGE_SIZE - 3,
                x * IMAGE_SIZE + 3,
                y * IMAGE_SIZE + 3,
            ),
            start=0,
            end=360,
            fill=(0, 0, 255),
            width=6,
        )

print(N_in, N)
print((N_in / N) * 4)

img.save("plot.png")
