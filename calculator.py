
import math
import numpy


# TODO: Yuval Geva use this :)
# TODO: Haim use this :)
UNIFORM = "UNIFORM"
ALPHA = "ALPHA_"
ALPHA_RANGE = numpy.arange(-2.0, 3.0, 0.1)
WEIGHT_1 = 1
WEIGHT_2 = 2
WEIGHT_4 = 4
WEIGHT_8 = 8
WEIGHT_16 = 16


# TODO: Haim should call this function and pass the value to the randomize function
# TODO: Yuval Geva should call this function to give rand weights
def calc_alpha_probabilities(alpha):
    """
    Calculate the normalized probabilities for each weight in the alpha distribution

    :param: alpha: A float between (-2) to 3
    :return: A dictionary with the probability for each weight
    """

    sum = 0
    for weight in [WEIGHT_1, WEIGHT_2, WEIGHT_4, WEIGHT_8, WEIGHT_16]:
        sum += weight ** ((-1) * alpha)

    prob_dict = {}
    for weight in [WEIGHT_1, WEIGHT_2, WEIGHT_4, WEIGHT_8, WEIGHT_16]:
        prob_dict[weight] = (weight ** ((-1) * alpha)) / sum

    return prob_dict


def expect_weight(alpha, alpha_prob_dict=None):
    """
    Calculate the expected weight

    :param: alpha: A float between (-2) to 3 for an alpha distribution or None for uniform distribution
    :param: prob_dict: If this is an alpha distribution, this is a dictionary representing the probabilities for each weight
    :return: The expected weight - 2 * sqrt(the second moment of the distribution)
    """

    if alpha:
        sec_moment = 0
        for weight in [WEIGHT_1, WEIGHT_2, WEIGHT_4, WEIGHT_8, WEIGHT_16]:
            sec_moment += (weight ** 2) * alpha_prob_dict[weight]
        return sec_moment

    else:
        # the second moment (=E[x^2]) of the uniform[0,1] distribution is 1/3
        return 2 * math.sqrt(1/3)


# TODO: Haim should call this function and pass the value to the randomize function
def calculate_expected_weights(alpha_prob_dict):
    """
    Calculates the expected weights and store into a dictionary with the keys: UNIFORM/ALPHA_<>

    :param: prob_dict: A dictionary representing the probabilities for each weight
    :return: A dictionary of weights
    """

    weights_dict = {}

    # uniform distribution
    weights_dict[UNIFORM] = expect_weight(None)

    # alpha distribution
    for alpha in ALPHA_RANGE:
        weights_dict[ALPHA + str(alpha)] = expect_weight(alpha, alpha_prob_dict)

    return weights_dict