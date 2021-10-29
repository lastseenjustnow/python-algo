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


# Unbounded Knapsack
def solve_knapsack(profits, weights, capacity):
    lookup_table = [0] * capacity
    for i in range(len(profits)):
        for j in range(weights[i] - 1, capacity):
            current_profit = 0 if j == weights[i] - 1 else lookup_table[j - weights[i]]
            if current_profit + profits[i] > lookup_table[j]:
                current_profit += profits[i]
                lookup_table[j] = current_profit

    return max(lookup_table)


# Maximum Ribbon Cut
def count_ribbon_pieces(ribbonLengths, total):
    """
    Time: O(total * l)
    Space: O(total)

    t - total length of ribbons needed
    l - possible variations of ribbons lengths

    """
    lookup_table = [-1] * total
    for ribbon in ribbonLengths:
        if lookup_table[ribbon - 1] == -1:
            lookup_table[ribbon - 1] = 1
        for ribbons_count in range(ribbon + 1, total + 1):
            if lookup_table[ribbons_count - ribbon - 1] != -1 and lookup_table[ribbons_count - 1] < lookup_table[ribbons_count - ribbon - 1] + 1:
                lookup_table[ribbons_count - 1] = lookup_table[ribbons_count - ribbon - 1] + 1

    return lookup_table[total - 1]


# House thief
def find_max_steal(wealth):
    """
    Time: O(n)
    Space: O(1)

    t - total length of ribbons needed
    l - possible variations of ribbons lengths

    """
    lookup = [wealth[0], max(wealth[0], wealth[1])]
    for w in wealth[2:]:
        cur_wealth = max(w + lookup[0], lookup[1])
        lookup[0], lookup[1] = lookup[1], cur_wealth

    return lookup[1]


# Minimum Deletions to Make a Sequence Sorted
def find_minimum_deletions(nums):
    """
    Time: O((max(n) - min(n))^2)
    Space: O(max(n) - min(n))
    """
    global_max, global_min = max(nums), min(nums)
    lookup = [0] * (global_max - global_min + 1)
    for n in nums[::-1]:
        if lookup[n - global_min] == 0:
            lookup[n - global_min] = 1
        counter = 1
        for i in range(n - global_min + 1, global_max - global_min + 1):
            if lookup[i] >= counter:
                counter += 1
            if 0 < lookup[i] < counter:
                lookup[i] = counter

    return len(nums)-max(lookup)


# Palindromic Partitioning
def palindromic_partitioning(s):
    """
    Time: O(n^2)
    Space: O(1)
    """
    unique_ids = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            continue
        unique_ids += 1
        j = i
        while j > 1:
            if s[j - 2] != s[i]:
                break
            unique_ids -= 2
            j -= 2
        if j != i and j > 0 and s[j] == s[j-1]:
            unique_ids += 1

    return unique_ids - 1


# Longest Bitonic Subsequence
def find_LBS_length(nums):
    """
    Time: O(n^2)
    Space: O(n)
    """

    l = len(nums)
    lis, lds = [0] * l, [0] * l
    lis[0], lds[-1] = 1, 1

    for i in range(1, l):
        lis[i] = 1
        lds[l - i - 1] = 1
        for j in range(i):
            if nums[i] > nums[j]:
                lis[i] = lis[j] + 1
            if nums[l - i - 1] > nums[l - j - 1]:
                lds[l - i - 1] = lds[l - j - 1] + 1

    maxLength = 0
    for i in range(l):
        maxLength = max(maxLength, lis[i] + lds[i] - 1)

    return maxLength


# Edit Distance
def find_min_operations(s1, s2):
    """
    Time: O(max(s1, s2))
    Space: O(n)
    """

    max_l, min_l = max(len(s1), len(s2)), min(len(s1), len(s2))
    long_s, short_s = (s1, s2) if len(s1) > len(s2) else (s2, s1)
    insertions_left = diff = max_l - min_l
    i = j = 0

    while i < max_l:
        if long_s[i] != short_s[j]:
            if short_s[j] == long_s[i+1] and insertions_left > 0:
                insertions_left -= 1
                i += 1
            else:
                diff += 1
                i += 1
                j += 1
        else:
            i += 1
            j += 1

    return diff
