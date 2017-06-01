import cPickle as pickle
import gzip
import numpy as np
import matplotlib.pyplot as plt


class DataSet:
    # digit_image = None

    digit_image = None

    @classmethod
    def __init__(cls):
        filename = "mnist.pkl.gz"
        f = gzip.open(filename, 'rb')
        train_set, valid_set, test_set = pickle.load(f)
        f.close()
        image, label = train_set
        cls.digit_image = [[] for i in range(10)]
        for index, image in enumerate(image):
            cls.digit_image[label[index]].append(image)

    @classmethod
    def get_one_digit(cls, digit=np.random.randint(0, 9), index=None):
        if index is None:
            index = np.random.randint(0, 100)
        return cls.digit_image[digit][index].reshape(28, 28)

    @staticmethod
    def show_image(image_array, is_gray=True, is_reshape=True):
        arr = np.array(image_array)
        if is_reshape:
            arr = arr.reshape(28, 28)
        if is_gray:
            plt.imshow(arr, cmap='gray')
        else:
            plt.imshow(arr)
        plt.show()


DataSet()
