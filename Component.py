import numpy as np
from img_util import crop_edge, ComponentSetting, Point
from dataset import DataSet
from matplotlib import pyplot as plt


def generate_component(component_setting):
    """

    :type component_setting: ComponentSetting
    """
    digit_list = component_setting.numbers
    coordinate = component_setting.coordinate
    variance = component_setting.variance

    coordinate_system = np.zeros((200, 200))
    digit_list = list(digit_list)
    for index, tdigit in enumerate(digit_list):
        digit = DataSet.get_one_digit(tdigit)
        x = int(coordinate[index].x + np.random.randn() * variance)
        y = int(coordinate[index].y + np.random.randn() * variance)
        coordinate_system[(x - 14 + 20):(x + 14 + 20), (y - 14 + 20):(y + 14 + 20)] = np.maximum(digit.reshape(28, 28),
                                                                                                 coordinate_system[
                                                                                                 (x - 14 + 20):(
                                                                                                     x + 14 + 20),
                                                                                                 (y - 14 + 20):(
                                                                                                     y + 14 + 20)])
    return crop_edge(coordinate_system)


if __name__ == '__main__':
    set = ComponentSetting(coordinate=[Point(10, 15), Point(20, 9), Point(11, 30)], numbers=[3, 4, 5], variance=1)
