
# lotto 1000 (x,y) between (1,0) without repeat-
import random as rnd
import statistics
import matplotlib.pyplot as plt
import patience_sort_alg


def uniform(n):
    number_set = set()
    while len(number_set) < n:
        item = rnd.random(), rnd.random()
        number_set.add(item)
    l = sorted(number_set, key=lambda x: x[0])

    # get y
    l2 = [x[1] for x in l]

    return patience_sort_alg.patience_sort(l2)


if __name__ == "__main__":
    num_tests = 500
    num_points = 1000
    
    uniform_test = [uniform(num_points) for _ in range(num_tests)]

    mean = statistics.mean(uniform_test)
    variance = statistics.variance(uniform_test)

    plt.plot(range(num_tests), uniform_test, '-bo')
    plt.ylim([min(uniform_test) - 3, max(uniform_test) + 4])
    plt.xlabel("Test no.", fontweight="bold")
    plt.ylabel("Longest subsequence", fontweight="bold")
    plt.title("Uniform Distribution - Longest Subsequences Test", fontweight="bold")
    plt.figtext(.15, .8, "mean = {}".format(mean))
    plt.figtext(.15, .75, "variance = {}".format(variance))
    plt.show()





