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

    print(max_profit)
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