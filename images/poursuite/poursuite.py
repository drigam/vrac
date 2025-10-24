""" Voir Points de Brocard """

import math
from PIL import Image, ImageDraw


WIDTH, HEIGHT = 1748, 1240

poursuite = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 255))
draw = ImageDraw.Draw(poursuite)

def avance(p, q, v):
    dist = math.dist(p, q)
    if dist == 0:
        coeff = 1
    else:
        coeff = v / dist
    return [p[0] + coeff * (q[0]-p[0]), p[1] + coeff * (q[1]-p[1])]

def trace(my_poly):
    for ni in range(NB_POLY):
        draw.line((my_poly[ni], my_poly[(ni+1) % NB_POLY]), fill=(0, 0, 0), width=1)


for nx in range(3):
    for ny in range(2):
        A = [100+500*nx, 100+500*ny]
        B = [100+500*nx, 600+500*ny]
        C = [600+500*nx, 600+500*ny]
        D = [600+500*nx, 100+500*ny]
        poly = [A, B, C, D]
        if (nx+ny) % 2 == 0:
            poly.reverse()
        NB_POLY = len(poly)

        for nk in range(200):
            trace(poly)
            p0 = poly[0]
            for i in range(NB_POLY - 1):
                poly[i] = avance(poly[i], poly[i+1], math.dist(poly[i], poly[i+1])/15)
            poly[NB_POLY - 1] = avance(poly[NB_POLY - 1], p0, math.dist(poly[NB_POLY - 1], p0)/15)

poursuite.show()

poursuite.save("poursuite.png")
