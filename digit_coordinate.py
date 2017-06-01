import numpy as np
from img_util import Point


def is_validate_coordinate(coordinate_list, threshold=1.2):
    '''
    This function is to check whether
    '''
    p1 = np.array(coordinate_list[0])
    p2 = np.array(coordinate_list[1])
    p3 = np.array(coordinate_list[2])
    a = np.sqrt(np.linalg.norm(p1 - p2))
    b = np.sqrt(np.linalg.norm(p2 - p3))
    c = np.sqrt(np.linalg.norm(p3 - p1))

    if min(a, b, c) == 0:
        return False
    if max(a, b, c) / min(a, b, c) > threshold:
        return False
    else:
        return True


def three_sides(points):
    '''

    Parameters
    ----------
    points: list of Points

    Returns:
    Three length of sides of the points
    -------

    '''
    p1 = np.array(points[0])
    p2 = np.array(points[1])
    p3 = np.array(points[2])
    a = np.sqrt(np.linalg.norm(p1 - p2))
    b = np.sqrt(np.linalg.norm(p2 - p3))
    c = np.sqrt(np.linalg.norm(p3 - p1))
    return a, b, c


def digit_coordinate_list(num):
    count = 0
    qualified_tris = []
    while count < num:
        c = np.array([[0, 0], [1, 0], [0.5, 1]])*50
        if True:
            count += 1
            # c = c / np.max(three_sides(c))*4
            # c = c / np.max(three_sides(c)) * (np.random.randn() * 0.5 + 4)
            qualified_tris.append([Point(x=point[0], y=point[1]) for point in list(c.astype(np.int))])

    return qualified_tris
