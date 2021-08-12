from typing import Dict, Set

import heapq

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


# Challenge 2: Search in a Rotated List
def pivoted_binary_search(lst, n, key):
    """
    It's implied that a list is sorted and then rotated
    Time: O(log n)
    Space: O(1)

    Function to search key in a list
    :param lst: A list of integers
    :param n: The size of the list
    :param key: A key to be searched in the list
    """

    left, right = 0, n - 1
    while left < right:
        middle = (right - left) // 2 + left
        if lst[middle] == key:
            return middle
        elif lst[middle] <= lst[right]:
            if lst[middle] < key < lst[right]:
                left = middle + 1
            else:
                right = middle
        else:
            if lst[left] < key < lst[middle]:
                right = middle
            else:
                left = middle + 1

    return


# Challenge 3: Group Anagrams
def anagrams(lst):
    """
    Function to find anagram pairs

    Time: O(n) (?)
    Space: O(n)

    :param lst: A lst of strings
    :return: Group of anagrams
    """

    groups = []
    decomposed_anagrams: Dict[str, Set[str]] = {}

    for anagram in lst:
        # 26 letters of alphabet + space. Other symbols of english words also should be included
        alphabet_dict = [0] * 27
        for letter in anagram:
            alphabet_dict[min(abs(ord(letter)-97), 26)] += 1

        alphabet_key = ' '.join(map(str, alphabet_dict))
        if decomposed_anagrams.get(alphabet_key):
            for word in decomposed_anagrams.get(alphabet_key):
                groups.append([word, anagram])
            decomposed_anagrams.get(alphabet_key).add(anagram)
        else:
            decomposed_anagrams[alphabet_key] = {anagram}

    return groups


# Challenge 4: Arrange a Binary List
def sort_binary_list(lst):

    """
    A function to sort binary list

    Time: O(n)
    Space: O(1)

    :param lst: A list containing binary numbers
    :return: A sorted binary list
    """

    binary_dict = {0: 0, 1: 0}
    for elem in lst:
        binary_dict[elem] += 1

    return [0] * binary_dict[0] + [1] * binary_dict[1]


# Challenge 5: Find the Maximum Product of Two Integers in a List
def find_max_prod(lst):
    """

    Time: O(n)
    Space: O(1)

    Finds the pair having maximum product in a given list
    :param lst: A list of integers
    :return: A pair of integer
    """
    min_heap, max_heap = [], []
    for elem in lst[:2]:
        heapq.heappush(min_heap, elem)
        heapq.heappush(max_heap, elem * -1)

    for elem in lst[2:]:
        if elem > heapq.nsmallest(1, min_heap)[0]:
            heapq.heappushpop(min_heap, elem)
        if elem < abs(heapq.nsmallest(1, max_heap)[0]):
            heapq.heappushpop(max_heap, elem * -1)

    return min_heap if min_heap[0] * min_heap[1] > max_heap[0] * max_heap[1] else list(map(lambda x: x * -1, max_heap))
