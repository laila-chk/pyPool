from PIL import Image
import numpy as np
from numpy._typing import NDArray

def ft_load(path: str) -> NDArray:
    """this function loads an image, prints its format, and its pixels
    content and RGB format. """
    try:
        img = Image.open(path)
    except Exception :
        exit("Error while trying to read the image! make sure the path is correct.")
    data = np.asarray(img)
    print(f"The shape of image is: ({img.size[1]}, {img.size[0]}, {len(img.mode)})")
    print(f":{data}")
    return data

