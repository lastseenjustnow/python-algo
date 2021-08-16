import heapq
import math

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


# Challenge 2: Connecting n Pipes with Minimum Cost
def min_cost(pipes):
    """
    Calculates the minimum cost of connecting pipes

    Time: O(n log n)

    :param pipes: A list where its length is the number of pipes and indexes are the specific lengths of the pipes.
    :return: The minimum cost
    """
    result = 0
    heapq.heapify(pipes)

    while len(pipes) != 1:
        mins = heapq.nsmallest(2, pipes)
        result += sum(mins)
        heapq.heappop(pipes)
        heapq.heappushpop(pipes, sum(mins))

    return result


# Challenge 3: Find the Egyptian Fraction's Denominators
def egyptian_fraction(numerator, denominator):
    """
    Finds the egyptian fraction denominators
    :param numerator: Numerator of the fraction
    :param denominator: Denominator of the fraction
    :return: A list of denominators of the egyptian fraction
    """

    gcd = math.gcd(numerator, denominator)
    numerator = int(numerator / gcd)
    denominator = int(denominator / gcd)

    result, fr = [], 1

    while numerator != 1:
        if 1 / fr < numerator / denominator:
            result.append(fr)
            greatest_common_factor: int = int(fr * denominator / math.gcd(fr, denominator))
            new_numerator: int = numerator * greatest_common_factor / denominator - greatest_common_factor / fr
            new_denominator: int = greatest_common_factor
            numerator, denominator = new_numerator, new_denominator
        fr += 1
    result.append(denominator)

    return result
