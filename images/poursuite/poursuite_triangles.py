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


delta = 500 * math.sqrt(3) / 2

for nx in range(6):
    for ny in range(5):
        for np in range(2):
            nnx = nx - 2
            nny = ny - 1
            A = [100+500*nnx + 250 * (nny % 2), 100 + delta*nny]
            B = [600+500*nnx + 250 * (nny % 2), 100 + delta*nny]
            C = [350+500*nnx + 250 * (nny % 2), 100 + delta*(np*2 - 1) + delta*nny]
            if np == 0:
                poly = [A, C, B]
            else:
                poly = [A, B, C]
            # if (nx+ny) % 2 == 0:
            #     poly.reverse()
            NB_POLY = len(poly)

            for nk in range(200):
                trace(poly)
                p0 = poly[0]
                for i in range(NB_POLY - 1):
                    poly[i] = avance(poly[i], poly[i+1], math.dist(poly[i], poly[i+1])/15)
                poly[NB_POLY - 1] = avance(poly[NB_POLY - 1], p0, math.dist(poly[NB_POLY - 1], p0)/15)

poursuite.show()

poursuite.save("poursuite_triangle.png")
