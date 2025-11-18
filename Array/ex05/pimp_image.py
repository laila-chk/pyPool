from numpy._typing import NDArray
import numpy as np
from PIL import Image


def ft_invert(array : NDArray) -> NDArray:
    """Inverts the colors of the received array of image."""
    im = Image.fromarray(array)
    out = im.point(lambda i: 255 - i)
    out.show()
    return array

def ft_red(array) -> NDArray:
    im = Image.fromarray(array)
    source = im.split()
    R, G, B = 0, 1, 2
    # out = source[R].point(lambda i: 255)
    # source[R].paste(out, None, None)
    out = source[B].point(lambda i: 0)
    source[B].paste(out, None, None)
    out = source[G].point(lambda i: 0)
    source[G].paste(out, None, None)

    img = Image.merge(im.mode, source)
    img.show()
    return array
    

def ft_green(array) -> NDArray:
    im = Image.fromarray(array)
    source = im.split()
    R, B = 0, 2
    out = source[R].point(lambda i: 0)
    source[R].paste(out, None, None)
    out = source[B].point(lambda i: 0)
    source[B].paste(out, None, None)

    img = Image.merge(im.mode, source)
    img.show()
    return array
    
def ft_blue(array) -> NDArray:
    im = Image.fromarray(array)
    source = im.split()
    R, G = 0, 1
    out = source[R].point(lambda i: 0)
    source[R].paste(out, None, None)
    out = source[G].point(lambda i: 0)
    source[G].paste(out, None, None)

    img = Image.merge(im.mode, source)
    img.show()
    return array

def ft_grey(array) -> NDArray:
    im = Image.fromarray(array).convert("L")

    im.show()
    return array
    
# Gray (=(0.299* Red)+(0.587* Green)+(0.114* Blue)).
# def ft_grey(array) -> NDArray:
#     im = Image.fromarray(array)
#     # grey_pixels = np.zeros((im.size[1], im.size[0], 1))
#     grey_pixels = np.copy(array)
#     for r in range(im.size[1] ):
#         for c in range(im.size[0] ):
#             R = array[r, c, 0]
#             G = array[r, c, 1]
#             B = array[r, c, 2]

#             G = 0.299 * R + 0.587 * G + 0.114 * B
#             grey_pixels[r,c] = G

#     img = Image.fromarray(grey_pixels)
#     img.show()
#     return array
    
