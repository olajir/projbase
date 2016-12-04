

import numpy as np
import skimage
import skimage.morphology as morph
import skimage.filters as filt
import skimage.exposure as expo


def get_corrected_image(iimage, gamma=0.25):
    """Return filtered image to detect spots."""
    image = skimage.util.img_as_float(iimage)
    image **= gamma

    return image
