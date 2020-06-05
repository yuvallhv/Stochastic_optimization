
import numpy.random as rnd
import calculator
import constants


def rand_weights_by_alpha(num_points, alpha):
    """
    Randomize n weights from the alpha distribution.
    Each of the following weight has an alpha-dependent probability:
    weight x - probability (x^(-alpha))/(sum of all probabilities)
    and calculate the expected weight

    :param num_points: number of weights to randomize (n)
    :param alpha: A float between (-2) to 3
    :return: weights list (each item is an int - 1/2/4/8/16), expected weight (with sec moment)
    """

    constants.print_debug("randomizing {} weights from the alpha distribution, alpha= {}".format(num_points, alpha))

    # calculate the probabilities to get each weight (1,2,4,8,16) by the chosen alpha
    prob_dict = calculator.calc_alpha_probabilities(alpha)
    prob_lst = list(prob_dict.values())
    lst = rnd.choice(constants.WEIGHTS_LST, num_points, True, prob_lst)

    expected_weight = calculator.calculate_expected_weight(alpha, prob_dict)
    return list(lst), expected_weight


def rand_weights_uniformly(num_points):
    """
    Randomize n weights from uniform distribution.

    :param num_points: number of weights to randomize (n)
    :return: weights list (each item is an int - 1/2/4/8/16)
    """

    constants.print_debug("randomizing {} weights from uniform distribution".format(num_points))

    lst = rnd.choice(constants.WEIGHTS_LST, num_points, True)
    return list(lst)


def rand_points_uniform_distribution(num_points):
    """
    1. Randomize n points (x, y) from a uniform distribution[0,1].
    2. Sorts the y of each point in a list by their x value

    :param num_points: number of points to randomize (n)
    :return: A tuple - The points tuples list [(X1,Y1),...,(Xn,Yn)], The sorted list of y values
    """

    constants.print_debug("randomizing {} points (x, y) from a uniform distribution[0,1]".format(num_points))
    constants.print_debug("randomizing {} points (x, y) from a uniform distribution[0,1]".format(num_points))

    number_set = set()
    while len(number_set) < num_points:
        item = rnd.random(), rnd.random()   # A tuple - (x,y)
        number_set.add(item)
    x_y_lst = sorted(number_set, key=lambda x: x[0])

    # get a list of y only, ordered by x
    y_lst = [x[1] for x in x_y_lst]

    return x_y_lst, y_lst



