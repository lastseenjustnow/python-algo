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
        secont_term = rec(residual, pointer + 1)
        memo[residual - 1][pointer] = first_term + secont_term
        return memo[residual - 1][pointer]

    return rec(n, 0)
