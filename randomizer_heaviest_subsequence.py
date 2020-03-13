
import statistics
import math
import matplotlib.pyplot as plt
import numpy
import constants, calculator, rand_weights_and_points, heaviest_subsequence_alg
import pandas as pd

# TODO: Haim should call this function
def randomize(num_points, expected_weights_dict, alpha=None):
    """
    1. Randomize n points and weights from the specified distribution (x, y are randomized uniformly)
    2. Calculate the heaviest sub-sequence
    3. Calculate the ratio between the expected weight (2 * sqrt(the second moment of the distribution))

    :param: num_points: number of points and weights to randomize (n)
    :param: expected_weights: A dictionary representing the expected weights
    :param: alpha: A float between (-2) to 3 for an alpha distribution or None for uniform distribution
    :return: A tuple - (The points tuples list [(X1,Y1),...,(Xn,Yn)], weight of the heaviest sub-sequence, the ration)
    """

    x_y_lst, y_lst = rand_weights_and_points.rand_points_uniform_distribution(num_points)

    if alpha:
        weights_lst = rand_weights_and_points.rand_weights_by_alpha(num_points, alpha)
        # constants.print_debug(weights_lst)
    else:
        weights_lst = rand_weights_and_points.rand_weights_uniformly(num_points)
        constants.print_debug(weights_lst)

    heaviest_subseq = heaviest_subsequence_alg.algorithm(y_lst, weights_lst)

    if alpha:
        exp_weight = expected_weights_dict[constants.ALPHA + str(alpha)]
    else:
        exp_weight = expected_weights_dict[constants.UNIFORM]

    ratio = abs(heaviest_subseq - exp_weight)

    return x_y_lst, weights_lst, heaviest_subseq, ratio


def handle_results(alpha, heaviest_subsequence, x_y_lst, graph_name, csv_name):
    """
    Display the results in a graph, save the graph and export to excel

    :param alpha: A float between (-2) to 3 for an alpha distribution or None for uniform distribution
    :param heaviest_subsequence: The weight of the heaviest subsequence (int)
    :param x_y_lst: The points tuples list [(X1,Y1),...,(Xn,Yn)]
    :param graph_name: The name of the graph (to save)
    :param csv_name: The name of the excel file (to save)
    """

    constants.print_debug("creating graph and saving the results in: graph name={}, csv name={}"
                          .format(graph_name, csv_name))


    constants.print_debug("TODO")
    # TODO: Yaniv
    pass

def make_graph(name, results):
    ids = [i[0] for i in results]
    seqs = [i[1] for i in results]
    mean = statistics.mean(seqs)
    variance = statistics.variance(seqs)
    plt.plot(ids, seqs, '-bo')
    plt.ylim([min(seqs) - 3.0, max(seqs) + 4.0])
    plt.xlabel("Test no.", fontweight="bold")
    plt.ylabel("Heaviest subsequence", fontweight="bold")
    plt.title(name + " - Heaviest Subsequences Test", fontweight="bold")
    plt.figtext(.15, .8, "mean = {}".format(mean))
    plt.figtext(.15, .75, "variance = {}".format(variance))
    plt.show()

def run_uniform_distribution(expected_weight_dict, num_points, repeats):
    constants.print_debug("\n*** running uniform distribution, {} times with {} points each time ***"
                          .format(repeats, num_points))
    graph_name = "uniform_distribution_graph_no._"
    csv_name = "uniform_distribution_csv_no._"
    results = []
    for idx in range(repeats):
        constants.print_debug("\nrun no. {}".format((idx+1)))
        x_y_lst, weight_lst, heaviest_subseq, ratio = randomize(num_points, expected_weight_dict)

        x_lst, y_lst = [i[0] for i in x_y_lst], [i[1] for i in x_y_lst]
        df = pd.DataFrame(data={"x_list": x_lst, "y_list": y_lst, "weights": weight_lst})
        df.to_csv("csv\\" + graph_name + str(idx) + '.csv')

        handle_results(None, heaviest_subseq, x_y_lst, graph_name + str(idx), csv_name + str(idx))
        results.append([idx, heaviest_subseq])
        constants.print_debug("heaviest sub-sequence is: {}, ratio between the expected and actual weight: {}\n"
                              .format(heaviest_subseq, ratio))
    make_graph("Unifrom Distribution", results)


def run_chosen_alpha(alpha, expected_weight_dict, num_points, repeats):
    constants.print_debug("\n*** running alpha= {} distribution, {} times with {} points each time ***"
                          .format(alpha, repeats, num_points))
    graph_name = "alpha_{}_distribution_graph_no._".format(alpha)
    csv_name = "alpha_{}_distribution_csv_no._".format(alpha)

    for idx in range(repeats):
        constants.print_debug("\nrun no. {}".format((idx + 1)))
        x_y_lst, heaviest_subseq, ratio = randomize(num_points, expected_weight_dict, alpha)
        handle_results(alpha, heaviest_subseq, x_y_lst, graph_name + str(idx), csv_name + str(idx))
        constants.print_debug("heaviest sub-sequence is: {}, ratio between the expected and actual weight: {}\n"
                              .format(heaviest_subseq, ratio))

    # TODO: Haim - make sure I did this correct, didnt have time to check
    pass


if __name__ == "__main__":

    # TODO: Haim
    # TODO: weird results, talk to Yaniv
    # TODO: try to reach 1000 runs
    expected_weight_dict = {}
    num_points = 1000
    repeats = 100

    # calculate the expected weight of the heaviest sub-sequence and ration for uniform distribution
    expected_weight_dict[constants.UNIFORM] = calculator.calculate_expected_weight(None)
    run_uniform_distribution(expected_weight_dict, num_points, repeats)
    #
    # # calculate the expected weight of the heaviest sub-sequence and ration for alpha distribution
    # for alpha in constants.ALPHA_RANGE:
    #
    #     # calculate the probabilities to get each weight (1,2,4,8,16) by the chosen alpha
    #     alpha_prob_list = calculator.calc_alpha_probabilities(alpha)
    #
    #     # calculate the expected weight of the heaviest sub-sequence for the chosen alpha
    #     expected_weight_dict[constants.ALPHA + str(alpha)] = calculator.calculate_expected_weight(alpha, alpha_prob_list)
    #
    #     # run
    #     run_chosen_alpha(alpha, expected_weight_dict, num_points, repeats)


    # for each point: x=place in line, y=row in the plane


    # for the uniform distribution and for each alpha distribution call the randomize function
    # save the results from the function (a tuple - The weight of the heaviest sub-sequence, the ration)
    # display the results in a graph and export to excel (alpha, the weight of the heaviest subsequence, ratio,
    #   the points, the weight of each point)
    # use 10 million points

    # try to reach 1000 runs for several chosen alpha - func: run_chosen_alpha

    # write the results for each test in a separate execl (and a separate function :)








