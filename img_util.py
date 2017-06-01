import numpy as np
from collections import namedtuple


# crop the black part of the image at the edge
# can refer to draft ipython notebook
# noinspection PyTypeChecker
def crop_edge(img):
    h, w = img.shape
    nd = img
    ul = 0
    ur = 0
    dl = 0
    dr = 0
    for i in range(h):
        if np.any(nd[0:i, :] != 0):
            ul = i - 1
            break
    for j in range(w):
        if np.any(nd[:, 0:j] != 0):
            ur = j - 1
            break
    for i in range(h - 1, -1, -1):
        if np.any(nd[i:h, :] != 0):
            dl = i + 1
            break
    for j in range(w - 1, -1, -1):
        if np.any(nd[:, j:w] != 0):
            dr = j + 1
            break
    return img[ul:dl, ur:dr]


class ComponentSetting(namedtuple("Component", ["coordinate", "numbers", "variance"])):
    pass


class Point(namedtuple("Point", ["x", "y"])):
    pass
