# Challenge 1: The 0/1 Knapsack Problem
def knap_sack(profits, profits_length, weights, capacity):
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
