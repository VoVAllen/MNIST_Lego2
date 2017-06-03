from Component import generate_component
import numpy as np
from img_util import ComponentSetting, crop_edge
from digit_coordinate import digit_coordinate_list
import itertools
import matplotlib.pyplot as plt
from scipy import misc

# bg_imgs = np.load("cllutter_bg_150.npy").astype(np.float)
# bg_imgs /= 256
# print(bg_imgs.max())


def generate_component_settings(coordinates):
    clist = []
    ns = [(i,j,k) for i in range(10) for j in range(10) for k in range(10)]
    print len(ns)
    # ns2 = np.random.permutation(ns)[:len(coordinates)]
    ns2=ns
    for index in range(len(nsm)):
        clist.append(
            ComponentSetting(coordinate=coordinates[0], variance=1, numbers=ns2[index]))
    return clist


def patch_on_background(cp, bg_size=150):
    '''
    This function is to patch the component onto the background

    Parameters
    ----------
    cp: np.array
    The component to be placed on the background

    bg_size: Int
    Background Size, default is 150

    Returns

    bg: np.array with shape (bg_size,bg_size)
    -------

    '''
    # may use cluttered background later
    # bg_imgs = np.zeros((bg_size, bg_size))
    size = bg_size
    bg=np.zeros((bg_size,bg_size))
    # bg = bg_imgs[np.random.randint(0, bg_imgs.shape[0])][:size, :size].copy()
    height, width = cp.shape
    x = np.random.randint(size - width)
    y = np.random.randint(size - height)
    bg[y:y + height, x:x + width] = np.maximum(cp, bg[y:y + height, x:x + width])
    return bg


def lego_generator(num, num_class, component_num=1, settings=None):
    """

    Parameters
    ----------
    num: Int
    Number of picture per class

    num_class: Int
    Number of classes

    component_num: Int
    Number of component in one picture

    Returns

    dataset: np.array
    The dataset

    label: np.array
    The label, with shape (component_num,

    -------

    """
    if component_num == 1:
        if settings is None:
            coordinates = digit_coordinate_list(num_class)
            settings = generate_component_settings(coordinates)
        dataset = []
        label = []
        for index in range(num_class):
            for i in range(num):
                if i % 100 == 0: print index, ' ', i
                dataset.append(patch_on_background(generate_component(settings[index]), 100))
                label.append(index)

        return dataset, label, settings
    if component_num == 2:
        if settings is None:
            print 'yes'
            coordinates = digit_coordinate_list(num_class)
            settings = generate_component_settings(coordinates)
        dataset = []
        label = []
        components = []
        for index in range(num_class):
            for i in range(2 * num):
                if i % 100 == 0: print index, ' ', i
                components.append(generate_component(settings[index]))
                label.append(index)
        components = np.array(components)
        permutated_indices = np.random.permutation(range(len(components)))
        permutated_components = components[permutated_indices]
        permutated_label = np.array(label)[permutated_indices]
        plt.imsave('0.jpg', permutated_components[0])
        plt.imsave('1.jpg', permutated_components[1])
        plt.imsave('2.jpg', permutated_components[2])
        final_label = []
        for i in range(num * num_class):
            component1, component2 = permutated_components[2 * i:2 * i + 2]
            label1, label2 = permutated_label[2 * i:2 * i + 2]
            h1, w1 = component1.shape
            h2, w2 = component2.shape
            x, y = np.random.randint(0, 20, size=2)
            bg = np.pad(component1, pad_width=((0, 150 - h1), (0, 150 - w1)), mode="constant")
            bg[h1 + x:h1 + x + h2, w1 + y:w1 + y + w2] = component2
            combined_component = bg.copy()
            dataset.append(patch_on_background(crop_edge(combined_component)))
            final_label.append((label1, label2))
            if i % 100 == 0: print i
        print final_label
        return dataset, final_label, settings
