from typing import Deque, Tuple, Optional

from collections import deque


# Challenge 1: The 0/1 Knapsack Problem
def knap_sack_brute_force_iterative(profits, profits_length, weights, capacity):
    """
    Finds the maximum value that can be put in a knapsack

    Time: O(n^2)

    :param profits: The profit that can be gained by each item
    :param profits_length: The number of pieces of jewelry
    :param weights: The weight of each piece of jewelry
    :param capacity: The maximum weight that the knapsack can hold
    :return: Maximum value that can be put in a knapsack
    """

    cum_profits, cum_weights = [], []
    max_profit = 0

    for i in range(profits_length):
        cum_profits.append(profits[i])
        cum_weights.append(weights[i])
        if profits[i] > max_profit and weights[i] <= capacity:
            max_profit = profits[i]
        this_len = len(cum_profits) - 1
        for j in range(this_len):
            new_profit = cum_profits[j] + profits[i]
            new_weight = cum_weights[j] + weights[i]
            cum_profits.append(new_profit)
            cum_weights.append(new_weight)
            if new_profit > max_profit and new_weight <= capacity:
                max_profit = new_profit

    return max_profit


def knap_sack_brute_force_recursive(profits, profits_length, weights, capacity):

    def rec(i, cum_profit, cum_weight):
        if cum_weight > capacity:
            return 0
        if i == profits_length:
            return cum_profit
        put = rec(i + 1, cum_profit + profits[i], cum_weight + weights[i])
        not_put = rec(i + 1, cum_profit, cum_weight)
        return max(put, not_put)

    return rec(0, 0, 0)


def knap_sack_memoization(profits, profits_length, weights, capacity):

    memo = dict()

    def rec(i, cum_profit, cum_weight):
        if cum_weight > capacity:
            return 0
        if i == profits_length:
            key = ' '.join(map(str, [i, cum_weight]))
            if memo.get(key) is None:
                memo[key] = cum_profit
            return cum_profit

        key = ' '.join(map(str, [i + 1, cum_weight + weights[i]]))
        put = rec(i + 1, cum_profit + profits[i], cum_weight + weights[i]) if memo.get(key) is None else memo[key]

        key = ' '.join(map(str, [i + 1, cum_weight]))
        not_put = rec(i + 1, cum_profit, cum_weight) if memo.get(key) is None else memo[key]

        return max(put, not_put)

    return rec(0, 0, 0)


def knap_sack_tabularization(profits, profits_length, weights, capacity):
    """

    Time: O(N * C)
    Space: O(N * C)

    N - items count
    C - capacity

    Finds the maximum value that can be put in a knapsack
    :param profits: The profit that can be gained by each
    :param profits_length: The number of pieces of jewelry
    :param weights: The weight of each piece of jewelry
    :param capacity: The maximum weight that the knapsack can hold
    :return: Maximum value that can be put in a knapsack
    """

    # Basic checks
    if capacity <= 0 or profits_length == 0:
        return 0

    lookup_table = [[0 for x in range(capacity + 1)] for x in range(profits_length + 1)]

    # Building the lookup table in bottom up manner
    for i in range(profits_length + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                lookup_table[i][j] = 0
            elif weights[i - 1] <= j:
                lookup_table[i][j] = max(profits[i - 1] + lookup_table[i - 1][j - weights[i - 1]],
                                         lookup_table[i - 1][j])
            else:
                lookup_table[i][j] = lookup_table[i - 1][j]

    return lookup_table[profits_length][capacity]


def knap_sack_tabularization_optimized(profits, profits_length, weights, capacity):
    """
    Finds the maximum value that can be put in a knapsack

    Time: O(N * C)
    Space: O(C)

    N - items count
    C - capacity

    :param profits: The profit that can be gained by each
    :param profits_length: The number of pieces of jewelry
    :param weights: The weight of each piece of jewelry
    :param capacity: The maximum weight that the knapsack can hold
    :return: Maximum value that can be put in a knapsack
    """

    # basic checks
    if capacity <= 0 or profits_length == 0:
        return 0

    lookup_table = [0 for x in range(capacity + 1)]
    # if we have only one weight, we will take it if it is not more than the
    # capacity
    for i in range(capacity + 1):
        if weights[0] <= i:
            lookup_table[i] = profits[0]

    # process all sub-lists for all the capacities
    for i in range(1, profits_length):
        for j in reversed(range(capacity + 1)):

            profit1 = 0

            # include the item, if it is not more than the capacity
            if weights[i] <= j:
                profit1 = profits[i] + lookup_table[j - weights[i]]
            # exclude the item
            profit2 = lookup_table[j]
            # take maximum
            lookup_table[j] = max(profit1, profit2)

    return lookup_table[capacity]


# Challenge 2: Staircase Problem
def count_ways_brute_force(n):
    """
    Calculates the number of ways a stair can be climbed

    Amount of maximum stairs that can be jumped: 3

    Time: O(3^n)

    :param n: Number of stairs
    :return: Number of ways to climb a stair
    """
    const = {0: 1, 1: 1, 2: 2, 3: 4}
    if n <= 3:
        return const[n]

    count = 0

    stack = deque([x for x in range(1, 4)])

    while stack:
        cum_stairs = stack.popleft()
        if cum_stairs == n:
            count += 1
        else:
            for stairs in range(1, 4):
                if cum_stairs + stairs <= n:
                    stack.append(cum_stairs + stairs)

    return count


def count_ways_memoization(n):
    """
    Time: O(n ^ 2)
    Space: O(n ^ 2)
    """

    const = {0: 1, 1: 1, 2: 2, 3: 4}
    if n <= 3:
        return const[n]

    lookup_table = [[0 for _ in range(n)] for _ in range(n)]

    def fill_lookup_table(i, j):
        if i < 0 or j < 0:
            return 0

        if i == 0 and 0 <= j <= 2:
            lookup_table[i][j] = 1
            return 1

        if lookup_table[i][j] > 0:
            return lookup_table[i][j]
        else:
            result = sum([fill_lookup_table(i-1, j-x) for x in range(1, 4)])
            lookup_table[i][j] = result
            return result

    return sum([fill_lookup_table(y, n-1) for y in range(n)])


def count_ways_tabularization(n):
    """
    Time: O(n ^ 2)
    Space: O(n ^ 2)
    """

    if n <= 2:
        return max(1, n)

    lookup_table = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(3):
        lookup_table[0][i] = 1

    for i in range(1, n):
        for j in range(n):
            subarray = lookup_table[i-1][max(j - 3, 0):max(j, 0)]
            lookup_table[i][j] = sum(subarray)

    result = sum([x[n - 1] for x in lookup_table])
    return result


def count_ways_tabularization_optimized(n):
    """
    Time: O(n ^ 2)
    Space: O(n)
    """

    const = {0: 1, 1: 1, 2: 2, 3: 4}
    if n <= 3:
        return const[n]

    array, i, result = [1, 1, 1] + [0] * (n - 4), 1, 0

    while i <= n:
        result += array[n-i] if i > 1 else 0
        i += 1
        array = [sum(array[max(0, j - 2):max(0, j + 1)]) for j in range(n-1)]

    return result


# Challenge 3: The Partition Problem
def can_partition_brute_force(st):
    """
    Checks if two sub-lists has equal sum or not

    Time: O(2^n)

    :param st: Integer list having positive numbers only
    :return: returns True if two sub-lists have equal sum, otherwise False
    """

    stack: Deque[Optional[Tuple[int, int]]] = deque()
    stack.append((0, sum(st)))
    stack.append(None)
    i = 0

    while i != len(st):
        current_tuple = stack.popleft()
        if not current_tuple:
            i += 1
            stack.append(None)
            continue
        if current_tuple[0] + st[i] == current_tuple[1] - st[i]:
            return True
        stack.append((current_tuple[0], current_tuple[1]))
        stack.append((current_tuple[0] + st[i], current_tuple[1] - st[i]))

    return False


def can_partition_tabularization_optimized(st):
    """
    Checks if two sub-lists has equal sum or not

    Time: O(s * l)
    Space: O(s)

    l - length of a set
    s - sum of a set

    :param st: Integer list having positive numbers only
    :return: returns True if two sub-lists have equal sum, otherwise False
    """

    set_sum = sum(st)
    if set_sum % 2 == 1:
        return False

    lookup_table = [0] * (int(set_sum / 2))
    lookup_table[int(set_sum / 2) - 1] = 1
    i = 0

    while i != len(st):
        new_lookup_table = lookup_table
        for j in range(int(set_sum / 2)):
            if lookup_table[j] == 1 and j - st[i] == 0:
                return True
            new_lookup_table[abs(j - st[i])] = 1
        lookup_table = new_lookup_table

    return False


# Challenge 6: Longest Palindromic Subsequence
def longest_palindromic_subsequence_recursive_brute_force(s):
    """
    Finds the longest palindromic subsequence length

    Time: O(n!)

    :param s: Input string
    :return: Length of shortest common superstring
    """
    def rec(subsec):
        for i in range(len(subsec) // 2):
            if subsec[i] != subsec[len(subsec) - i - 1]:
                subseq_max = max([rec(subsec[:j] + subsec[(j+1):]) for j in range(len(subsec))])
                return subseq_max

        return len(subsec)

    return rec(s)


def longest_palindromic_subsequence_memoization(s):
    """
    Finds the longest palindromic subsequence length

    Time: O(n!)

    :param s: Input string
    :return: Length of shortest common superstring
    """
    lookup_table = dict()

    def rec(subsec):

        if lookup_table.get(subsec):
            return lookup_table[subsec]

        for i in range(len(subsec) // 2):
            if subsec[i] != subsec[len(subsec) - i - 1]:
                subseq_max = max([rec(subsec[:j] + subsec[(j+1):]) for j in range(len(subsec))])
                lookup_table[subsec] = subseq_max
                return subseq_max

        return len(subsec)

    return rec(s)


# Challenge 7: The Coin Change Problem
def count_change_brute_force_recursive(denoms, denoms_length, amount):
    """
    Finds the number of ways that the given number of cents can be represented.

    Time: O(2^n)
    Space: O(1)

    :param denoms: Values of the coins available
    :param denoms_length: Number of denoms
    :param amount: Given cent
    :return: The number of ways that the given number of cents can be represented.
    """

    def rec(available_denoms, available_denoms_length, cur_amount):
        if cur_amount < 0 or available_denoms_length == 0:
            return 0
        if cur_amount == 0:
            return 1
        put_coin = rec(available_denoms, available_denoms_length, cur_amount - available_denoms[0])
        not_put_coin = rec(available_denoms[1:], available_denoms_length - 1, cur_amount)
        return put_coin + not_put_coin

    return rec(denoms, denoms_length, amount)


def count_change_memoization(denoms, denoms_length, amount):
    """
    Finds the number of ways that the given number of cents can be represented.

    Time: O(n * m)
    Space: O(n * m)

    n - length of denoms
    m - amount

    :param denoms: Values of the coins available
    :param denoms_length: Number of denoms
    :param amount: Given cent
    :return: The number of ways that the given number of cents can be represented.
    """
    lookup_table = [[-1 for _ in range(denoms_length)] for _ in range(amount)]

    def rec(i, current_amount):
        if current_amount < 0 or i < 0:
            return 0
        if current_amount == 0:
            return 1
        if lookup_table[current_amount - 1][i] != -1:
            return lookup_table[current_amount - 1][i]
        put_coin = rec(i, current_amount - denoms[i])
        not_put_coin = rec(i - 1, current_amount)
        lookup_table[current_amount - 1][i] = put_coin + not_put_coin
        return put_coin + not_put_coin

    return rec(denoms_length - 1, amount)


def count_change_tabularization(denoms, denoms_length, amount):
    """
    Finds the number of ways that the given number of cents can be represented.

    Time: O(n * m)
    Space: O(n * m)


    n - length of denoms
    m - amount

    :param denoms: Values of the coins available
    :param denoms_length: Number of denoms
    :param amount: Given cent
    :return: The number of ways that the given number of cents can be represented.
    """
    lookup_table = [[-1 for _ in range(amount + 1)] for _ in range(denoms_length)]

    for x in range(denoms_length):
        lookup_table[x][0] = 1

    for x in range(denoms_length):
        for y in range(1, amount + 1):
            first_term = lookup_table[x-1][y] if x > 0 else 0
            second_term = lookup_table[x][y - denoms[x]] if y - denoms[x] >= 0 else 0
            lookup_table[x][y] = first_term + second_term

    return lookup_table[denoms_length - 1][amount]


def count_change_tabularization_optimized(denoms, denoms_length, amount):
    """
    Finds the number of ways that the given number of cents can be represented.

    Time: O(n * m)
    Space: O(m)

    n - length of denoms
    m - amount

    :param denoms: Values of the coins available
    :param denoms_length: Number of denoms
    :param amount: Given cent
    :return: The number of ways that the given number of cents can be represented.
    """
    lookup_table = [1] + [0] * amount

    for x in range(denoms_length):
        new_lookup_table = [1] + [0] * amount
        for y in range(1, amount + 1):
            first_term = lookup_table[y] if x > 0 else 0
            second_term = new_lookup_table[y - denoms[x]] if y - denoms[x] >= 0 else 0
            new_lookup_table[y] = first_term + second_term
        lookup_table = new_lookup_table

    return lookup_table[amount]
