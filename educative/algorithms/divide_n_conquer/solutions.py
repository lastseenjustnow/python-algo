import math

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


# Challenge 4: Collect Coins in Minimum Steps
def minimum_steps(lst):
    """
    Function which calculates the minimum steps to collect coins from the list
    :param lst: List of coins stack
    :return: Returns minimum steps to collect coins from the list, otherwise 0
    """
    if len(lst) == 1:
        return 1
    if len(lst) == 0:
        return 0

    max_elem = max(lst)
    if len(lst) > max_elem:
        lists, new_list = [], []
        for elem in lst:
            if elem - 1 == 0:
                lists.append(new_list)
                new_list = []
            else:
                new_list.append(elem - 1)
        return sum([minimum_steps(x) for x in lists]) + 1

    return minimum_steps(lst[:lst.index(max_elem)]) \
           + minimum_steps(lst[lst.index(max_elem)+1:]) \
           + 1


# Challenge 5: Find the Floor and Ceil of a Number in a Sorted List
def find_floor(lst, low, high, x):
    """
    Modified binary search function to find the floor of given number x
    :param lst: List of integers
    :param low: Starting index of the list
    :param high: Ending index of the list
    :return: Returns the floor of an integer x if exists, otherwise -1
    """
    middle = (high - low) // 2 + low
    if middle + 1 == len(lst):
        return lst[middle]
    if x > lst[middle]:
        if x <= lst[middle+1]:
            return lst[middle]
        return find_floor(lst, middle + 1, high, x)
    return find_floor(lst, low, middle, x)


def find_ceiling(lst, low, high, x):
    """
    Modified binary search function to find the floor of given number x

    Time: O(log n)

    :param lst: List of integers
    :param low: Starting index of the list
    :param high: Ending index of the list
    :return: Returns the ceiling of an integer x if exists, otherwise -1
    """

    middle = (high - low) // 2 + low
    if middle + 1 == len(lst):
        return -1
    if x >= lst[middle]:
        if x <= lst[middle+1]:
            return lst[middle+1]
        return find_ceiling(lst, middle + 1, high, x)
    return find_ceiling(lst, low, middle, x)


def find_floor_ceiling(lst, x):
    # DO NOT MODIFY THIS FUNCTION #

    """
    Calls the find_floor and find_ceiling functions and returns their results
    :param lst: List of integers
    :param x: An integer
    :return: Returns the floor of an integer x, otherwise -1
    """
    return find_floor(lst, 0, len(lst) - 1, x), find_ceiling(lst, 0, len(lst) - 1, x)


# Challenge 7: Find the Closest Number
def find_closest(lst, target):
    """
    Finds the closest number to the target in the list
    :param lst: Sorted list of integers
    :param target: Left sided index of the list
    :return: Closest element from the list to the target
    """

    def rec(start, end):
        mid = (end - start) // 2 + start
        if mid == len(lst) - 1:
            return lst[mid]
        if abs(lst[mid] - target) > abs(lst[mid+1] - target):
            return rec(mid + 1, end)
        if abs(lst[mid] - target) > abs(lst[mid-1] - target):
            return rec(start, mid)
        return lst[mid]

    return rec(0, len(lst) - 1)


# Challenge 8: Shuffle Integers
def shuffle_list_naive(lst):
    """
    Shuffles the list
    :param lst: List of integers
    """
    log_base = math.log2(len(lst))
    if not log_base.is_integer():
        return lst

    swap_count = math.pow(2, log_base - 1) - 1
    while swap_count > 0:
        this_swap_count = swap_count
        i, j = int(len(lst) / 2) - 1, int(len(lst) / 2)
        while this_swap_count > 0:
            if this_swap_count == swap_count:
                lst[i], lst[j] = lst[j], lst[i]
            else:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                i -= 1
                j += 1
            this_swap_count -= 1
        swap_count -= 2

    return lst


def shuffle_list_recursive(lst):

    """
    Shuffles the list

    Time: O(n log n)

    :param lst: List of integers
    """

    log_base = math.log2(len(lst))
    if not log_base.is_integer():
        return lst

    def rec(left, right):
        if right - left == 1:
            return

        swap_step = int(((right - left) + 1) / 4)
        middle = (right - left) // 2 + left
        step = middle
        for _ in range(swap_step):
            lst[step], lst[step + swap_step] = lst[step + swap_step], lst[step]
            step -= 1
        rec(left, middle)
        rec(middle + 1, right)

    rec(0, len(lst)-1)
    return lst


# Challenge 9: Inversion Count in a List
def inversion_count(lst):
    """
    Function to find Inversion Count
    :param lst: List of integers
    :return: The inversion count of the list
    """

    def rec(left, right):
        if right - left == 1:
            if lst[left] > lst[right]:
                lst[left], lst[right] = lst[right], lst[left]
                return 1
            return 0
        elif right - left == 0:
            return 0

        mid = (right - left) // 2 + left
        left_count = rec(left, mid)
        right_count = rec(mid+1, right)
        merge_count = 0
        while mid + 1 < len(lst) and lst[mid+1] < lst[mid]:
            i = mid + 1
            while i > 0 and lst[i] < lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
                merge_count += 1
                i -= 1
            mid += 1
        return left_count + right_count + merge_count

    return rec(0, len(lst) - 1)
