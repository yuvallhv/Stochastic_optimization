
import statistics
import math
import matplotlib.pyplot as plt
import numpy


import heaviest_subsequence_alg
import rand_weights_and_points
import constants
import calculator


# TODO: Haim should call this function
def randomize(num_points, expected_weights, alpha=None):
    """
    1. Randomize n points and weights from the specified distribution (x, y are randomized uniformly)
    2. Calculate the heaviest sub-sequence
    3. Calculate the ratio between the expected weight (2 * sqrt(the second moment of the distribution))

    :param: num_points: number of points and weights to randomize (n)
    :param: expected_weights: A dictionary representing the expected weights
    :param: alpha: A float between (-2) to 3 for an alpha distribution or None for uniform distribution
    :return: A tuple - (The points tuples list [(X1,Y1),...,(Xn,Yn)], The weight of the heaviest sub-sequence, the ration)
    """

    x_y_lst, y_lst = rand_weights_and_points.rand_points_uniform_distribution(num_points)

    if alpha:
        weights_lst = rand_weights_and_points.rand_weights_by_alpha(num_points, alpha)
    else:
        weights_lst = rand_weights_and_points.rand_weights_uniformly(num_points)

    heaviest_subseq = heaviest_subsequence_alg.algorithm(y_lst, weights_lst)
    exp_weight = expected_weights[constants.ALPHA + str(alpha)] if alpha else expected_weights[constants.UNIFORM]
    ratio = abs(heaviest_subseq - exp_weight)

    return x_y_lst, heaviest_subseq, ratio


def handle_results(alpha, heaviest_subsequence, x_y_lst, graph_name, csv_name):
    """
    Display the results in a graph, save the graph and export to excel

    :param alpha: A float between (-2) to 3 for an alpha distribution or None for uniform distribution
    :param heaviest_subsequence: The weight of the heaviest subsequence (int)
    :param x_y_lst: The points tuples list [(X1,Y1),...,(Xn,Yn)]
    :param graph_name: The name of the graph (to save)
    :param csv_name: The name of the excel file (to save)
    """

    # TODO: Yaniv
    pass


def run_chosen_alpha():
    # try to reach 1000 runs for several chosen alpha

    # TODO: Haim
    pass


def run_many_points():
    # try to test how far we can get with the number of points (try to reach 1,000,000,000)

    # TODO: Haim
    pass


if __name__ == "__main__":

    expected_alpha_weight_list = {}

    # calculate the expected weight of the heaviest sub-sequence for uniform distribution
    expected_alpha_weight_list[constants.UNIFORM] = calculator.calculate_expected_weight(None)

    for alpha in constants.ALPHA_RANGE:

        # calculate the probabilities to get each weight (1,2,4,8,16) by the chosen alpha
        alpha_prob_list = calculator.calc_alpha_probabilities(alpha)

        # calculate the expected weight of the heaviest sub-sequence for the chosen alpha
        expected_alpha_weight_list[constants.ALPHA + str(alpha)] = calculator.calculate_expected_weight(alpha, alpha_prob_list)

        # res_tuple = randomize(10000, alpha_weight_list, alpha)
        # constants.print_debug("res_tuple: {}".format(res_tuple))
        # constants.print_debug("x: {}".format(alpha))



    # for each point: x=place in line, y=row in the plane

    # TODO: Haim
    pass

    # for the uniform distribution and for each alpha distribution call the randomize function
    # save the results from the function (a tuple - The weight of the heaviest sub-sequence, the ration)
    # display the results in a graph and export to excel (alpha, the weight of the heaviest subsequence, ratio,
    #   the points, the weight of each point)
    # use 10 million points

    # try to reach 1000 runs for several chosen alpha - func: run_chosen_alpha
    # try to test how far we can get with the number of points (try to reach 1,000,000,000) - func: run_many_points

    # write the results for each test in a separate execl (and a separate function :)








