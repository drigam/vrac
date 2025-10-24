from math import cos, sin, pi

from PIL import Image, ImageDraw


WIDTH, HEIGHT = 2000, 1500
COLORS = [(255, 0, 0, 125), (0, 255, 0, 125), (0, 0, 255, 125)]
L = 150
ALPHA = pi/180 * 45
A0 = WIDTH/2 - L, HEIGHT - 100
B0 = WIDTH/2 + L, HEIGHT - 100


def square_length(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

def sim(a, b, alpha, mu):
    """
    Apply a similitude (rotation and homothetie) on a point

    :param a: center of rotation
    :param b: point to transform
    :param alpha: rotation angle
    :param mu: multiplication factor
    :return: new point
    """
    calpha, salpha = cos(alpha), sin(alpha)
    c = [b[0] - a[0], b[1] - a[1]]
    d = [mu*(c[0]*calpha + c[1]*salpha), mu*(-c[0]*salpha + c[1]*calpha)]

    return a[0] + d[0], a[1] + d[1]

def tree(a, b, n, alpha):
    if n < 0:
        return

    if square_length(a, b) < 1:
        return

    c = sim(b, a, -pi/2, 1)
    d = sim(a, b, pi/2, 1)
    fill_color = COLORS[n % 3]
    draw.polygon([a, b, c, d], fill=fill_color)  # outline=(50, 50, 50, 255)

    e = sim(d, c, alpha, cos(alpha))
    tree(d, e, n-1, alpha)
    tree(e, c, n-1, alpha)


image = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 255))

for num_alpha in range(45, 46):
    image = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(image, 'RGBA')
    alpha_new = pi/180 * num_alpha
    tree(A0, B0, 150, alpha_new)
    image.save(f"pytha_{num_alpha}.png")

# Show last image
image.show()
