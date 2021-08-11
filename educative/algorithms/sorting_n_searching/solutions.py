# Challenge 1: Find Two Numbers that Add up to "n"

def find_sum_brute_force(lst, n):
    """
    Function to find two number that add up to n

    Time: O(n^2)
    Space: O(1)

    :param lst: A list of integers
    :param n: The integer number n
    """

    for first_i, first in enumerate(lst, 0):
        for second in lst[first_i:]:
            if first + second == n:
                return (first, second)

    return


def find_sum_sorting(lst, n):
    """
    Time: O(n log n)
    Space: O(1)

    :param lst: A list of integers
    :param n: The integer number n
    :return: Possible pair of integers which sums up to n
    """

    lst.sort()
    left, right = 0, len(lst) - 1
    cur_sum = lst[left] + lst[right]

    while left < right:
        if cur_sum == n:
            return lst[left], lst[right]
        elif cur_sum < n:
            cur_sum = cur_sum - lst[left] + lst[left + 1]
            left += 1
        else:
            cur_sum = cur_sum - lst[right] + lst[right - 1]
            right -= 1

    return


def find_sum_dictionary(lst, n):
    """
    Time: O(n)
    Space: O(n)

    :param lst: A list of integers
    :param n: The integer number n
    :return: Possible pair of integers which sums up to n
    """
    d = {}
    for elem in lst:
        if not d.get(n - elem) is None:
            return n - elem, elem
        else:
            d[elem] = "I am here"

    return


def find_sum_set(lst, n):
    """
    Time: O(n)
    Space: O(n)

    :param lst: A list of integers
    :param n: The integer number n
    :return: Possible pair of integers which sums up to n
    """
    d = set()
    for elem in lst:
        if n - elem in d:
            return n - elem, elem
        else:
            d.add(elem)

    return
