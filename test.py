import patience_sort_alg

if __name__ == "__main__":

	lst = [float(7), float(3), float(8), float(1), float(3), float(4), float(10), float(6), float(9), float(5),];
	print("The longest increasing subsequence length is: {}".format(patience_sort_alg.patience_sort(lst)))