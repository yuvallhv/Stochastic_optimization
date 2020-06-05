
import numpy


UNIFORM = "uniform"
ALPHA_ = "alpha_{}"
ALPHA_RANGE = numpy.arange(-2.0, 3.1, 0.1)
WEIGHT_1 = 1
WEIGHT_2 = 2
WEIGHT_4 = 4
WEIGHT_8 = 8
WEIGHT_16 = 16
WEIGHTS_LST = [WEIGHT_1, WEIGHT_2, WEIGHT_4, WEIGHT_8, WEIGHT_16]

ALPHA_VAL = "alpha value"
HEAVIEST_SUBSEQ_WEIGHT = "heaviest sub-sequence weight"
EXPECTED_WEIGHT = "expected weight"
RATIO = "ratio"
X_Y_LST = "[x,y] list"

DEBUG_MODE = True


def print_debug(str):
    if DEBUG_MODE:
        print(str)


def print_dict(dictionary):
    for key, val in zip(dictionary.keys(), dictionary.values()):
        print("{}: {}".format(key, val))
