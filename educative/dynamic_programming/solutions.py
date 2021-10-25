from typing import List


# Largest Sum Subarray
def find_max_sum_sub_array(A):
    """Find a contiguous subarray with the largest sum."""
    best_sum = float('-inf')
    current_sum = 0
    for x in A:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum


# MaxSum Subsequence - Nonadjacent Elements
def find_max_sum_nonadjacent(a):
    first_sum = second_sum = max_sum = is_odd = 0
    for i in a:
        if i > 0:
            if not is_odd:
                first_sum += i
            else:
                second_sum += i
            is_odd = 1 - is_odd
        else:
            max_sum += max(first_sum, second_sum)
            first_sum = second_sum = 0

    return max_sum + max(first_sum, second_sum)


# Find Combinations for Game Scoring
def scoring_options(n):

    memo = [[None for _ in range(3)] for _ in range(n)]
    runs = [1, 2, 4]

    def rec(residual, pointer):
        if pointer > len(runs) - 1:
            return 0

        if residual < runs[pointer]:
            memo[residual - 1][pointer] = 0
            return 0

        if memo[residual - 1][pointer] is not None:
            return memo[residual - 1][pointer]

        if residual == runs[pointer]:
            memo[residual - 1][pointer] = 1
            return 1

        first_term = rec(residual - runs[pointer], 0)
        second_term = rec(residual, pointer + 1)
        memo[residual - 1][pointer] = first_term + second_term
        return memo[residual - 1][pointer]

    return rec(n, 0)


# Equal Subset Sum Partition
def can_partition(num: List[int]):
    summa = sum(num)
    if summa % 2 != 0:
        return False

    half_sum = int(summa / 2)
    lookup = [0] * half_sum
    lookup[0] = 1

    for elem in num:
        if lookup[half_sum - elem] == 1:
            return True

        for i in range(elem, half_sum):
            lookup[i] = lookup[i - elem]

    return False


# Subset Sum
def can_partition_subset_sum(num, sum):
    """
    Time: O(sum * l)
    Space: O(sum)

    l - length of array given

    """
    lookup = [0] * (sum + 1)
    lookup[0] = 1

    for elem in num:
        if lookup[sum] == 1:
            return True

        for i in range(sum, elem - 1, -1):
            lookup[i] = lookup[i - elem]

    return False


# Minimum Subset Sum Difference
def can_partition_minimum_subset_sum_difference(num):
    """
    Time: O(sum * l)
    Space: O(sum)

    l - length of array given

    """
    half_sum = int(sum(num) / 2)
    is_odd = sum(num) % 2
    lookup = [0] * (half_sum + 1)
    lookup[0] = 1

    for elem in num:
        if lookup[half_sum] == 1:
            return is_odd

        for i in range(half_sum, elem - 1, -1):
            lookup[i] = lookup[i - elem]

    for i in range(half_sum, -1, -1):
        if lookup[i] == 1:
            return (half_sum - i) * 2 + is_odd


# Longest Subarray with Ones after Replacement
def length_of_longest_substring_naive(arr, k):
    summa = sum(arr) + k

    while True:
        for i in range(summa, len(arr) + 1):
            if sum(arr[i - summa:i]) + k == summa:
                return summa
        summa -= 1


# Correct solution
def length_of_longest_substring(arr, k):

    window_start, window_end, current_ones, max_contiguous_ones = 0, 0, 0, 0

    while window_end < len(arr):
        if arr[window_end] == 1:
            current_ones += 1
        while window_end - window_start + 1 - current_ones > k:
            if arr[window_start] == 1:
                current_ones -= 1
            window_start += 1
        if current_ones > max_contiguous_ones:
            max_contiguous_ones = current_ones
        window_end += 1

    return max_contiguous_ones + k
