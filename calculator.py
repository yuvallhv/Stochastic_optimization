
import math
import constants


def calc_alpha_probabilities(alpha):
    """
    Calculate the normalized probabilities for each weight in the alpha distribution

    :param: alpha: A float between (-2) to 3
    :return: A dictionary with the probability for each weight
    """
    constants.print_debug("\ncalculating alpha probabilities")

    sum_weights = 0
    for weight in [constants.WEIGHT_1, constants.WEIGHT_2, constants.WEIGHT_4, constants.WEIGHT_8, constants.WEIGHT_16]:
        sum_weights += weight ** ((-1) * alpha)
        # constants.print_debug("{} ** ((-1) * {}) = {}".format(weight, alpha, (weight ** ((-1) * alpha))))

    prob_dict = {}
    for weight in [constants.WEIGHT_1, constants.WEIGHT_2, constants.WEIGHT_4, constants.WEIGHT_8, constants.WEIGHT_16]:
        prob_dict[weight] = (weight ** ((-1) * alpha)) / sum_weights

    constants.print_debug("probabilities dictionary:")
    constants.print_dict(prob_dict)
    constants.print_debug("sum of all probabilities is: {}\n".format(sum(prob_dict.values())))
    return prob_dict


def calculate_expected_weight(alpha, alpha_prob_dict=None):
    """
    Calculates the expected weights and store into a dictionary with the keys: UNIFORM/ALPHA_<>

    :param: alpha: A float between (-2) to 3 for an alpha distribution or None for uniform distribution
    :param: prob_dict: A dictionary representing the probabilities for each weight
    :return: The expected weight - 2 * sqrt(the second moment of the distribution)
    """

    if alpha:
        constants.print_debug("calculating expected weight for alpha= {}:".format(alpha))

        sec_moment = 0
        for weight in [constants.WEIGHT_1, constants.WEIGHT_2, constants.WEIGHT_4, constants.WEIGHT_8,
                       constants.WEIGHT_16]:
            sec_moment += (weight ** 2) * alpha_prob_dict[weight]

        constants.print_debug("weight is: {}".format(sec_moment))
        return sec_moment

    else:
        constants.print_debug("calculating expected weight for uniform distribution")
        # the second moment (=E[x^2]) of the uniform[0,1] distribution is 1/3
        constants.print_debug("weight is: {}".format(2 * math.sqrt(1/3)))
        return 2 * math.sqrt(1/3)
