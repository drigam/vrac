from PIL import Image

WIDTH, HEIGHT = 1500, 1500
UNITE = 300
NB_ITERATIONS = 20
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
# COLORS = [(254, 231, 240), (254, 254, 224), (244, 254, 254)]

image_wada = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 255))

def newton():
    """
    Search for the cubic roots of 2 ( zeros of function f )
    Iteration : x = x - f(x)/f'(x)
    """
    for x in range(WIDTH):
        for y in range(HEIGHT):
            z = complex((x-WIDTH/2)/UNITE, (y-HEIGHT/2)/UNITE)
            for k in range(NB_ITERATIONS):
                if z != 0:
                    z = z - (z**3-2) / (3*z**2)
            if z.real > 0:
                image_wada.putpixel((x, y), COLORS[0])
            elif z.imag > 0:
                image_wada.putpixel((x, y), COLORS[1])
            elif z.imag < 0:
                image_wada.putpixel((x, y), COLORS[2])


newton()

image_wada.show()
image_wada.save("img_wada_1.png")
