import math
from PIL import Image

WIDTH = 1000
HEIGHT = WIDTH
C = WIDTH / 2
R = C  # R : radius of the circle of inversion
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

echiquier = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 0))

for x in range(WIDTH):
    for y in range(HEIGHT):
        x0 = x - WIDTH / 2
        y0 = y - HEIGHT / 2
        try:
            f = R ** 2 / (x0 ** 2 + y0 ** 2)
            x1 = x0 * f
            y1 = y0 * f
            cx = math.floor(x1 / C)
            cy = math.floor(y1 / C)
            num_color = (cx + cy) % 3
            color = COLORS[num_color]
            echiquier.putpixel((x, y), color)
        except ZeroDivisionError:
            pass

echiquier.show()
echiquier.save("echiquier_rgb.png")
