# Challenge 2: Find the Peak Element

def find_peak(lst):
    """
    Finds a peak element

    Time: O(log n)

    :param lst: List of integers
    :return: Returns a peak element in a given list
    """

    l, r = 0, len(lst) - 1

    def divide(left, right):
        if left == right:
            return -1
        middle = (right - left) // 2 + left
        if lst[middle] >= lst[max(middle - 1, l)] and lst[middle] >= lst[min(middle + 1, r)]:
            return lst[middle]
        return max(divide(left, middle), divide(middle + 1, right))

    return divide(l, r)


# Challenge 3: Maximum Sum Sublist of Size K
def max_sub_list_of_size_k(lst, k):
    """
    Finds a maximum sum of a sub-list of given window size k

    Time: O(n)

    :param lst: List of integers
    :param k: Window size of the list
    :return: Returns the maximum sum of a sub-list of given window size k
    """

    glob_max = 0
    for i in range(k):
        glob_max += lst[i]

    cur_max = glob_max

    for i in range(k, len(lst)):
        cur_max = cur_max - lst[i - k] + lst[i]
        glob_max = cur_max if cur_max > glob_max else glob_max

    return glob_max

