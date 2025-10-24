from PIL import Image

WIDTH, HEIGHT = 1500, 1500
UNITE = 300
NB_ITERATIONS = 20
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

image_wada = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 255))

def newton():
    """
    Search for the zeros of function f  -  x -> x**4 - 2
    Iteration : x = x - f(x)/f'(x)
    """
    for x in range(WIDTH):
        for y in range(HEIGHT):
            z = complex((x-WIDTH/2)/UNITE, (y-HEIGHT/2)/UNITE)
            for k in range(NB_ITERATIONS):
                if z != 0:
                    z = z - (z**4-2) / (4*z**3)
            z = z * complex(1, 1)  # Rotation by 90° for the following tests (by quadrants)
            if z.real > 0 and z.imag > 0:
                image_wada.putpixel((x, y), COLORS[0])
            elif z.real > 0 and z.imag <= 0:
                image_wada.putpixel((x, y), COLORS[1])
            elif z.real <= 0 and z.imag > 0:
                image_wada.putpixel((x, y), COLORS[2])
            elif z.real <= 0 and z.imag <= 0:
                image_wada.putpixel((x, y), COLORS[3])


newton()

image_wada.show()
image_wada.save("img_wada_2.png")
