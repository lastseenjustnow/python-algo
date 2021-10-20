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
