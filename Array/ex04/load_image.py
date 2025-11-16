from PIL import Image, ImageDraw, ImageFont
import numpy as np

def ft_load(path: str, crop: bool) :
    """if crop is true, the function crops the image, grayscales it, adds a XY axis and write pixels vals
    then renders the new image, and print to the standar output the size, the mode and the pixels of the image"""
    try:
        img = Image.open(path)
    except Exception :
        exit("Error while trying to read the image! make sure the path is correct.")
    data = []
    if crop is True:
        box = (400, 100, 800, 500)
        img = img.crop(box)
        img = img.convert("L")
        data = np.asarray(img)
        data = np.transpose(data)
        img = Image.fromarray(data)

        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        width, height = img.size
        draw.rectangle([(0, 0), (399, 399)], outline="black")

        for x in range(0, width, 50):
            draw.line([(x, height - 10), (x, height)], fill="black")  # x-axis tick
            draw.text((x + 2, height - 15), str(x), fill="black", font=font)

        for y in range(0, height, 50):
            draw.line([(0, y), (10, y)], fill="black")  # y-axis tick
            draw.text((12, y - 5), str(y), fill="black", font=font)
        img.show()

    if crop is False:
        data = np.asarray(img)
    if len(img.mode) == 1:
        print(f"New shape after transpose:({img.size[1]}, {img.size[0]}, {len(img.mode)}) or: ({img.size[1]}, {img.size[0]})")
    else:
        print(f"The shape of image is:({img.size[1]}, {img.size[0]}, {len(img.mode)})")
    print(data) 

