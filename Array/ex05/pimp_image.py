from numpy._typing import NDArray
from PIL import Image


def ft_invert(array: NDArray) -> NDArray:
    """Inverts the colors of the received array of image."""
    im = Image.fromarray(array)
    out = im.point(lambda i: 255 - i)
    out.show()
    return array


def ft_red(array) -> NDArray:
    """apply a red filter on the image"""
    im = Image.fromarray(array)
    source = im.split()
    G, B = 1, 2
    out = source[B].point(lambda i: 0)
    source[B].paste(out, None, None)
    out = source[G].point(lambda i: 0)
    source[G].paste(out, None, None)

    img = Image.merge(im.mode, source)
    img.show()
    return array


def ft_green(array) -> NDArray:
    """this function applies a green filter on the image"""
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
    """this function applies a blue filter on the image"""
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
    """this function grayscales the image"""
    im = Image.fromarray(array).convert("L")
    im.show()
    return array
