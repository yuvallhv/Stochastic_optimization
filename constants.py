
import numpy

# TODO: Yuval Geva use this :)
# TODO: Haim use this :)
UNIFORM = "UNIFORM"
ALPHA = "ALPHA_"
ALPHA_RANGE = numpy.arange(-2.0, 3.1, 0.1)
WEIGHT_1 = 1
WEIGHT_2 = 2
WEIGHT_4 = 4
WEIGHT_8 = 8
WEIGHT_16 = 16

DEBUG_MODE = True


def print_debug(str):
    if DEBUG_MODE:
        print(str)


def print_dict(dictionary):
    for key, val in zip(dictionary.keys(), dictionary.values()):
        print("{}: {}".format(key, val))
