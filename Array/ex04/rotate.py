from load_image import ft_load


def rotate():
    """
    this function loads an image, prints its format, and its pixels
    content in RGB format.
    then it crops the image to 400x400 px, grayscales it,
    prints again the new values then renders the new image.
    """
    try:
        ft_load("animal.jpeg", False)
        ft_load("animal.jpeg", True)
    except Exception:
        exit()


def main():
    rotate()


if __name__ == "__main__":
    main()
