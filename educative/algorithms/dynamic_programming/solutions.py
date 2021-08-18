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

