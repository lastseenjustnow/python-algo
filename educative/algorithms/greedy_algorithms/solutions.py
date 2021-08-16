# Challenge 1: Counting Money!

def find_min_coins(v, coins_available):
    """
    This function finds the minimum number of coins

    Time: O(n^2)

    :param v: Total amount
    :param coins_available: Coins available in the machine
    :return: A list of total coins
    """

    stack, coins_stack, sum = [], sorted(coins_available), 0

    while sum != v and coins_stack:
        coin = coins_stack.pop()
        while sum < v:
            sum += coin
            stack.append(coin)
        if sum > v:
            sum -= coin
            stack.pop()
        elif sum == v:
            return stack

    return []
