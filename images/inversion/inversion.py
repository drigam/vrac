import math
from PIL import Image

width = 5000
height = width
C = width / 2
R = C  # R is the radius of the circle of inversion

echiquier = Image.new('RGB', (width, height), (255, 255, 0))

for x in range(width):
    for y in range(height):
        x0 = x - width / 2
        y0 = y - height / 2
        try:
            f = R ** 2 / (x0 ** 2 + y0 ** 2)  # factor = R**2 / d**2 ;  R**2 / ( d**2 + 0.000001 ) is possible here to avoid division by zero
            x1 = x0 * f
            y1 = y0 * f
            cx = math.floor(x1 / C)
            cy = math.floor(y1 / C)
            color = ((cx + cy) % 2) * 255
            echiquier.putpixel((x, y), (color, color, color))
        except ZeroDivisionError:
            pass

echiquier.show()
echiquier.save("echiquier.png")
