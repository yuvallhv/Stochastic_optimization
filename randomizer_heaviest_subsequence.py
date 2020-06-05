import json
import statistics
import math
import matplotlib.pyplot as plt
import numpy
import constants, calculator, rand_weights_and_points, heaviest_subsequence_alg
import pandas as pd


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
        weights_lst, expected_weight = rand_weights_and_points.rand_weights_by_alpha(num_points, alpha)
        # TODO: check the expected weights are ok - Yaniv
        expected_weights_dict[constants.ALPHA_.format(str(alpha))] = expected_weight
    else:
        weights_lst = rand_weights_and_points.rand_weights_uniformly(num_points)
        constants.print_debug(weights_lst)

    heaviest_subseq_weight = heaviest_subsequence_alg.algorithm(y_lst, weights_lst)

    if alpha:
        exp_weight = expected_weights_dict[constants.ALPHA_.format(str(alpha))]
    else:
        exp_weight = expected_weights_dict[constants.UNIFORM]

    ratio = abs(heaviest_subseq_weight - exp_weight)

    return x_y_lst, weights_lst, heaviest_subseq_weight, ratio


def handle_results(alpha, heaviest_subseq_weight, expected_weight, ratio, x_y_lst, file_name):
    """
    Save the results to json file

    :param alpha: A float between (-2) to 3 for an alpha distribution or None for uniform distribution (float)
    :param heaviest_subseq_weight: The weight of the heaviest subsequence (int)
    :param expected_weight: The expected weight of the heaviest subsequence (int)
    :param ratio: The ratio between the expected an the acual weight of the heaviest sub-sequence
    :param x_y_lst: The points tuples list [(X1,Y1),...,(Xn,Yn)]
    :param file_name: The name of the file (to save)
    """

    if alpha:
        directory_name = constants.ALPHA_.format(str(alpha))
    else:
        directory_name = constants.UNIFORM

    constants.print_debug("saving the results in: json name={}, at directory={}".format(file_name, directory_name))

    # the x_y list is a list of tuples and should be turned to a list of lists in order to be saved in a json
    x_y_list_of_lists = [list(x_y) for x_y in x_y_lst]

    json_dict = {
        constants.ALPHA_VAL: alpha,
        constants.HEAVIEST_SUBSEQ_WEIGHT: heaviest_subseq_weight,
        constants.EXPECTED_WEIGHT: expected_weight,
        constants.RATIO: ratio,
        constants.X_Y_LST: x_y_list_of_lists
    }

    # dump dictionary to json file
    file_name = f"{directory_name}/{file_name}.json"
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(json_dict, f, ensure_ascii=False, indent=4)


def make_graph(name, results, alpha=None):
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

    # TODO: Yaniv


def run_uniform_distribution(expected_weight_dict, num_points, repeats):
    constants.print_debug("\n*** running uniform distribution, {} times with {} points each time ***"
                          .format(repeats, num_points))
    graph_name = "uniform_distribution_graph"
    file_name = "uniform_distribution_no._{}"
    results = []

    for idx in range(repeats):
        constants.print_debug("\nrun no. {}".format((idx+1)))
        x_y_lst, weight_lst, heaviest_subseq_weight, ratio = randomize(num_points, expected_weight_dict)

        # x_lst, y_lst = [i[0] for i in x_y_lst], [i[1] for i in x_y_lst]
        # df = pd.DataFrame(data={"x_list": x_lst, "y_list": y_lst, "weights": weight_lst})
        # df.to_csv("csv\\" + graph_name + str(idx) + '.csv')

        handle_results(None, heaviest_subseq_weight, expected_weight_dict[constants.UNIFORM], ratio, x_y_lst,
                       file_name.format(str(idx)))

        results.append([idx, heaviest_subseq_weight])

        constants.print_debug("heaviest sub-sequence is: {}, ratio between the expected and actual weight: {}\n"
                              .format(heaviest_subseq_weight, ratio))
    make_graph(graph_name, results)


def run_chosen_alpha(alpha, expected_weight_dict, num_points, repeats):
    constants.print_debug("\n*** running alpha= {} distribution, {} times with {} points each time ***"
                          .format(alpha, repeats, num_points))
    graph_name = "alpha_{}_distribution_graph".format(alpha)
    file_name = "alpha_{}_distribution_no._".format(alpha)
    results = []

    for idx in range(repeats):
        constants.print_debug("\nrun no. {}".format((idx + 1)))
        x_y_lst, weights_lst, heaviest_subseq_weight, ratio = randomize(num_points, expected_weight_dict, alpha)

        # def handle_results(alpha, heaviest_subseq_weight, expected_weight, ratio, x_y_lst, file_name):
        handle_results(alpha, heaviest_subseq_weight, expected_weight_dict[constants.ALPHA_.format(str(alpha))], ratio,
                       x_y_lst, file_name + str(idx))

        results.append([idx, heaviest_subseq_weight])

        constants.print_debug("heaviest sub-sequence is: {}, ratio between the expected and actual weight: {}\n"
                              .format(heaviest_subseq_weight, ratio))

    make_graph(graph_name, results)


if __name__ == "__main__":

    # TODO: try to reach 1000 runs

    #TODO: Yuval G

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








