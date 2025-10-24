from PIL import Image, ImageDraw

filename = "./batz.jpg"

with Image.open(filename) as source_img:
    source_img.load()


# img.show()

# !!! The source image is supposed to be RGB (not RGBA (see special png files))
# img.getbands()

def transfo_boulanger(img: Image) -> Image:
    new_image = Image.new('RGB', img.size, (255, 255, 255))
    width, height = img.size

    for x in range(width):
        for y in range(height):
            color = img.getpixel((x, y))
            if y == height - 1 and height % 2 == 1:
                new_x, new_y = x, y
            else:
                if y % 2 == 0:
                    new_x = x * 2
                else:
                    new_x = 1 + x * 2

                new_y = y // 2

                if new_x >= width:
                    new_x -= width
                    new_y += height // 2

            # Put the source pixel in the target place (new_x, new_y)
            new_image.putpixel((new_x, new_y), color)

    return new_image


def transfo_photomaton(img: Image) -> Image:
    new_image = Image.new('RGB', img.size, (255, 255, 255))
    width, height = img.size

    for x in range(width):
        for y in range(height):
            color = img.getpixel((x, y))
            if (x == width - 1 and width % 2 == 1) or (y == height - 1 and height % 2 == 1):
                new_x, new_y = x, y
                zone_x, zone_y = 0, 0
            else:
                if x % 2 == 0:
                    new_x = x // 2
                    zone_x = 0
                else:
                    new_x = width // 2 + x // 2
                    zone_x = 1

                if y % 2 == 0:
                    new_y = y // 2
                    zone_y = 0
                else:
                    new_y = height // 2 + y // 2
                    zone_y = 1

            # Put the source pixel in the target place (new_x, new_y)
            color_r, color_g, color_b = color
            new_color = color

            # Change the color according to the zone
            # if zone_x == zone_y == 0:
            #     # NW
            #     pass
            # elif zone_x == 1 and zone_y == 0:
            #     # NE : R <-> G
            #     new_color = (color_g, color_r, color_b)
            # elif zone_x == 0 and zone_y == 1:
            #     # SW : G <-> B
            #     new_color = (color_r, color_b, color_g)
            # elif zone_x == 1 and zone_y == 1:
            #     # SE : R <-> B
            #     new_color = (color_b, color_g, color_r)

            new_image.putpixel((new_x, new_y), new_color)

    return new_image


# target_image = transfo_boulanger(source_img)
target_image = transfo_photomaton(source_img)
target_image.show()
