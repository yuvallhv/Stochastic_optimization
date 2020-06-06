import bisect
import constants


def heaviest_subseq(in_list):
    """How does this work?
    best_subseq: list of tuples - (biggest number in seq so far, sum of seq).
    We delete seq from the list when it's no longer relevant - there's another seq with a equal/bigger sum but ending on a smaller number.
    For every num: find where it fits in the list (using bisect), calculate new seq weight (weight of previous seq + new weight),
    and check for sequences to delete.

    Example run on this list: [7,5,8,2,4,6,9].
    Starting state = [(0,0)] (best list is in weight 0)
    Element: 7. best_subseq = [(0,0), (7,7)].
    Element: 5. best_subseq = [(0,0), (5,5), (7,7)].
    Element: 8. best_subseq = [(0,0), (5,5), (7,7), (8,15)]. Since 8 is after 7, the weight of the seq is 15.
    Element: 2. best_subseq = [(0,0), (2,2), (5,5), (7,7), (8,15)]
    Element: 4. 4 fits after 2, and the weight of the [2,4] seq is 6.
    At this point, (5,5) becomes irrelevant* - as the new sequence ends on a smaller number (4) and weights more (6).
    So the new list after deleting (5,5): [(0,0), (2,2), (4,6), (7,7), (8,15)].
    Element: 6. best_subseq = [(0,0), (2,2), (4,6), (6, 12), (7,7), (8,15)].
    Element: 9. best_subseq = [(0,0), (2,2), (4,6), (6, 12), (7,7), (8,15), (9,24)].
    Final answer = 24 [7,8,9].

    *NOTE: deleting isn't just for fun. We MUST delete - otherwise the algorithm is wrong!! Why?
    What if we didn't delete (5,5)?
    Next number is 6, which would have been added after (5,5). Weight is calculated by previous weight + new, so 5+6=11.
    So the list will be: ...(4,6),(5,5),(6,11).
    This is wrong! [2,4,6]=12 is an heavier subseq than [5,6]=11, so the list shoud have (6,12), not (6,11)!!
    So we delete 5 to avoid those cases.
    """
    best_subseq = [(0, 0, 0)] ##tuples of (last number in seq, seq max)
    for new_elem in in_list:
        insert_loc = bisect.bisect_left(best_subseq, (new_elem[0], 0)) #find where to insert current value in best_subseq
        best_pred_subseq_val = best_subseq[insert_loc - 1][1] #find y-sum of previous seq
        new_subseq_val = new_elem[0] + best_pred_subseq_val #calculate y-sum of current seq
        best_pred_subseq_weight = best_subseq[insert_loc - 1][2] #find weight of previous seq
        new_subseq_weight = new_elem[1] + best_pred_subseq_weight #calculate weight of current seq
        list_len = len(best_subseq)
        num_deleted = 0
        while (num_deleted + insert_loc < list_len
               and best_subseq[insert_loc][1] <= new_subseq_val):
            del best_subseq[insert_loc] ##if sequence is no longer relevant, delete it
            num_deleted += 1
        best_subseq.insert(insert_loc, (new_elem[0], new_subseq_val, new_subseq_weight))
    #return max(val for key, val in best_subseq)
    sorted_by_val = sorted(best_subseq, key=lambda tup: tup[1], reverse=True)
    return sorted_by_val[0][2]


def algorithm(y_lst, weight_lst):
    """
    Implements the heaviest sub-sequence algorithm

    :param y_lst: a list of y - represents the row in the plane, the list is ordered by their randomized x
    :param weight_lst: a list of weights for the points
    note: y_lst[i] matches weight_lst[i]
    :return: The weight of the heaviest sub-sequence of this list

    Note: this algorithm sorts the weights by their y_list values. I'm (Yaniv) not sure if this is really necessary.
    If we need to sort by the x_values, it means both lists are already sorted and we can directly call heaviest_subseq
    In this case, y_lst isn't needed at all.
    """

    constants.print_debug("running the heaviest sub-sequence algorithm")
    if len(weight_lst) != len(y_lst):
        return "list lenghts do not match"
    pairs = [(y_lst[i], weight_lst[i]) for i in range(0, len(weight_lst))]
 #   pairs = sorted(pairs, key=lambda tup: tup[0])
 #   weights = [x[1] for x in pairs]
    return heaviest_subseq(pairs)