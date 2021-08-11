from typing import List

import math
from collections import deque


# Find Maximum in Sliding Window
def find_max_sliding_window(arr, window_size):
    result = []
    window = deque()

    for index, element in enumerate(arr, 0):
        while window and arr[window[-1]] < element:
            window.pop()
        window.append(index)
        if index - window_size + 1 >= 0:
            while index - window_size + 1 >= window[0]:
                window.popleft()
            result.append(arr[window[0]])
        else:
            continue

    return result


# Search a Rotated Array
# Recursive approach
def binary_search_rotated(arr, key):
    def rec(left_index, right_index):
        middle_index = (right_index - left_index) // 2 + left_index
        if key == arr[left_index] or key == arr[right_index]:
            return left_index if arr[left_index] == key else right_index
        elif arr[left_index] < arr[right_index] and key < arr[middle_index]:
            return rec(left_index, middle_index)
        elif arr[left_index] < arr[right_index] and key > arr[middle_index]:
            return rec(middle_index + 1, right_index)
        elif arr[middle_index] < arr[right_index] and arr[middle_index] < key <= arr[right_index]:
            return rec(middle_index + 1, right_index)
        elif arr[middle_index] > arr[right_index] and not arr[left_index] < key <= arr[middle_index]:
            return rec(middle_index + 1, right_index)
        else:
            return rec(left_index, middle_index)

    return rec(0, len(arr)-1)


# Iterative approach

# Important!
# More efficient than recursive in Python because both algorithms could be executed over the same time,
# but iterative consumes O(1) memory, while recursive consumes O(log n) as it keeps recursive call stack in memory
# JVM implementations may neutralize that effect.
def binary_search_rotated_iter(arr, key):

    left_index, right_index = 0, len(arr)-1

    while arr[left_index] != key and arr[right_index] != key:
        middle_index = (right_index - left_index) // 2 + left_index
        if arr[left_index] < arr[right_index] and key < arr[middle_index]:
            right_index = middle_index
        elif arr[left_index] < arr[right_index] and key > arr[middle_index]:
            left_index = middle_index + 1
        elif arr[middle_index] < arr[right_index] and arr[middle_index] < key <= arr[right_index]:
            left_index = middle_index + 1
        elif arr[middle_index] > arr[right_index] and not arr[left_index] < key <= arr[middle_index]:
            left_index = middle_index + 1
        else:
            right_index = middle_index

    return left_index if arr[left_index] == key else right_index


# Find the Smallest Common Number
def find_least_common_number(a, b, c):

    a_i, b_i, c_i = 0, 0, 0
    current_min = min(a[0], b[0], c[0])

    while not a[a_i] == b[b_i] == c[c_i]:
        while a_i <= len(a) - 1 and a[a_i] < current_min:
            a_i += 1
        if a[a_i] > current_min:
            current_min = a[a_i]
        while b_i <= len(b) - 1 and b[b_i] < current_min:
            b_i += 1
        if b[b_i] > current_min:
            current_min = b[b_i]
        while c_i <= len(c) - 1 and c[c_i] < current_min:
            c_i += 1
        if c[c_i] > current_min:
            current_min = c[c_i]

        if a_i > len(a) - 1 and b_i > len(b) - 1 and c_i > len(c) - 1:
            return -1

    return a[a_i]


# Find Low/High Index of a Key in a Sorted Array
# Recursive approach
def find_low_index(arr, key):
    def rec(left_index, right_index):
        middle_index = (right_index - left_index) // 2 + left_index
        if arr[middle_index] == key and arr[middle_index-1] != key:
            return middle_index
        elif left_index == middle_index == right_index:
            return -1
        elif arr[middle_index] < key:
            return rec(middle_index + 1, right_index)
        else:
            return rec(left_index, middle_index)

    return rec(0, len(arr) - 1)


def find_high_index(arr, key):
    def rec(left_index, right_index):
        middle_index = (right_index - left_index) // 2 + left_index
        if arr[middle_index] == key and (middle_index == right_index or arr[middle_index + 1] != key):
            return middle_index
        elif left_index == middle_index == right_index:
            return -1
        elif arr[middle_index] <= key:
            return rec(middle_index + 1, right_index)
        else:
            return rec(left_index, middle_index)

    return rec(0, len(arr) - 1)


# Iterative approach
def find_low_index_iter(arr, key):
    left_index, middle_index, right_index = 0, (len(arr) - 1) // 2, len(arr) - 1

    while not (arr[middle_index] == key and arr[middle_index-1] != key):
        if left_index == middle_index == right_index:
            return -1
        middle_index = (right_index - left_index) // 2 + left_index
        if arr[middle_index] < key:
            left_index = middle_index + 1
        else:
            right_index = middle_index

    return middle_index


def find_high_index_iter(arr, key):
    left_index, middle_index, right_index = 0, (len(arr) - 1) // 2, len(arr) - 1

    while not (arr[middle_index] == key and (middle_index == right_index or arr[middle_index + 1] != key)):
        if left_index == middle_index == right_index:
            return -1
        middle_index = (right_index - left_index) // 2 + left_index
        if arr[middle_index] <= key:
            left_index = middle_index + 1
        else:
            right_index = middle_index

    return middle_index


# Move All Zeros to the Beginning of the Array
# Insert to a list is inefficient, the solution is naive
def move_zeros_to_left_naive(A):
    for i in range(len(A)):
        if A[i] == 0:
            del A[i]
            A.insert(0, 0)

    return A


def move_zeros_to_left(A):
    read_index, write_index = len(A) - 1, len(A) - 1

    while read_index >= 0:
        if not A[read_index] == 0:
            A[write_index] = A[read_index]
            write_index -= 1
        read_index -= 1

    while write_index >= 0:
        A[write_index] = 0
        write_index -= 1

    return A


# Stock Buy Sell to Maximize Profit
def find_buy_sell_stock_prices(array):

    profit = float('-inf')
    best_min_index = cur_max_index = cur_min_index = first_trough = 0
    while first_trough != len(array) - 1 and array[first_trough + 1] - array[first_trough] < 0:
        if array[first_trough + 1] - array[first_trough] > profit:
            best_min_index, cur_max_index = first_trough, first_trough + 1
            profit = array[first_trough + 1] - array[first_trough]
        first_trough += 1

    for index, elem in enumerate(array[first_trough:], first_trough):
        cur_max_index = index if elem > array[cur_max_index] else cur_max_index
        cur_min_index = index if elem < array[cur_min_index] else cur_min_index
        best_min_index = cur_min_index if cur_min_index < cur_max_index else best_min_index

    return array[best_min_index], array[cur_max_index]


# Merge an Array With Overlapping Intervals
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def merge_intervals(v: List[Pair]):
    result = []

    current_index = 1
    current_pair = Pair(v[0].first, v[0].second)
    while current_index < len(v):
        if current_pair.first <= v[current_index].first <= current_pair.second:
            current_pair.second = max(current_pair.second, v[current_index].second)
        else:
            result.append(current_pair)
            current_pair = Pair(v[current_index].first, v[current_index].second)
        current_index += 1
    result.append(current_pair)

    return result


# Cyclic Sort
def cyclic_sort(nums):
    for index in range(len(nums)):
        elem = nums[index]
        while index != elem - 1:
            nums[elem - 1], nums[index] = nums[index], nums[elem - 1]
            elem = nums[index]

    return nums


# Maximum Sum Subarray of Size K
def max_sub_array_of_size_k(k, arr):
    max_summa = cur_summa = 0
    for index in range(len(arr)):
        cur_summa += arr[index] - (0 if index < k else arr[index - k])
        max_summa = cur_summa if cur_summa > max_summa else max_summa

    return max_summa


# Smallest Subarray with a given sum
def smallest_subarray_with_given_sum(s, arr):
    min_count = current_count = current_sum = subtract_index = 0
    for index in range(len(arr)):
        current_sum += arr[index]
        current_count += 1
        while current_sum >= s:
            if min_count == 0 or min_count > current_count:
                min_count = current_count
            current_sum -= arr[subtract_index]
            current_count -= 1
            subtract_index += 1

    return min_count


# Squaring a Sorted Array
def make_squares(arr):
    left_index, right_index = 0, len(arr) - 1
    squares = deque()
    while left_index <= right_index:
        if abs(arr[left_index]) >= abs(arr[right_index]):
            squares.appendleft(arr[left_index] ** 2)
            left_index += 1
        else:
            squares.appendleft(arr[right_index] ** 2)
            right_index -= 1

    return list(squares)


# Subsets With Duplicates
def find_subsets(nums):
    subsets = []
    sorted_nums = sorted(nums)
    subsets.append([])
    previous_subset_count = 0
    for elem_index in range(len(nums)):
        this_subset_count = 0
        if elem_index == 0 or sorted_nums[elem_index] != sorted_nums[elem_index - 1]:
            subsets_index = 0
        else:
            subsets_index = len(subsets) - previous_subset_count
        for subset_i in range(subsets_index, len(subsets)):
            this_subset_count += 1
            subsets.append(subsets[subset_i] + [sorted_nums[elem_index]])
        previous_subset_count = this_subset_count

    return subsets


# Bitonic Array Maximum
def find_max_in_bitonic_array(arr):
    def rec(left_index, right_index):
        middle_index = ((right_index - left_index) // 2) + left_index
        if left_index == right_index or (arr[middle_index] > arr[middle_index - 1] and arr[middle_index] > arr[middle_index + 1]):
            return arr[middle_index]
        elif arr[middle_index] > arr[middle_index - 1]:
            return rec(middle_index + 1, right_index)
        else:
            return rec(left_index, middle_index)

    return rec(0, len(arr) - 1)


# Permutations
def find_permutations(nums):
    result = []
    result.append([])
    for index, num in enumerate(nums, 0):
        interresult = []
        for subset in result:
            [interresult.append(subset[:i] + [num] + subset[i:]) for i in range(index+1)]
        result = interresult

    return result


# Triplet Sum to Zero
def search_triplets(arr: List):
    triplets = []
    arr.sort()
    left_pointer, right_pointer, triplet_sum = 0, len(arr) - 1, 0
    while arr[left_pointer] <= 0:
        triplet_sum += arr[left_pointer]
        right_pointer = len(arr) - 1
        while arr[right_pointer] >= 0:
            if (right_pointer != len(arr) - 1) and arr[right_pointer] == arr[right_pointer + 1]:
                right_pointer -= 1
                continue
            triplet_sum += arr[right_pointer]
            middle_pointer = right_pointer - 1
            while middle_pointer != left_pointer and arr[middle_pointer] >= triplet_sum * -1:
                if arr[middle_pointer] == triplet_sum * -1:
                    triplets.append([arr[left_pointer], arr[middle_pointer], arr[right_pointer]])
                    break
                middle_pointer -= 1
            triplet_sum -= arr[right_pointer]
            right_pointer -= 1
        triplet_sum -= arr[left_pointer]
        left_pointer += 1

    return triplets


# Triplet Sum Close to Target
def triplet_sum_close_to_target(arr: List, target_sum):
    arr.sort()
    smallest_difference = math.inf
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while (left < right):
            target_diff = target_sum - arr[i] - arr[left] - arr[right]
            if target_diff == 0:  # we've found a triplet with an exact sum
                return target_sum - target_diff  # return sum of all the numbers

            # the second part of the following 'if' is to handle the smallest sum when we have more than one solution
            if abs(target_diff) < abs(smallest_difference) or (
                    abs(target_diff) == abs(smallest_difference) and target_diff > smallest_difference):
                smallest_difference = target_diff  # save the closest and the biggest difference

            if target_diff > 0:
                left += 1  # we need a triplet with a bigger sum
            else:
                right -= 1  # we need a triplet with a smaller sum

    return target_sum - smallest_difference


# Triplet with Smaller Sum
def triplet_with_smaller_sum(arr, target):
    count = 0
    for first_index in range(len(arr) - 2):
        for second_index in range(first_index + 1, len(arr) - 1):
            if arr[first_index] + arr[second_index] >= target:
                continue
            for third_index in range(second_index + 1, len(arr)):
                count += 1 if arr[first_index] + arr[second_index] + arr[third_index] < target else 0

    return count


# Subarrays with Product Less than a Target
def find_subarrays(arr, target):
    result = []
    for right in range(len(arr)):
        left, prod = right, 1
        while left >= 0:
            prod *= arr[left]
            if prod >= target:
                break
            result.append(arr[left:right+1])
            left -= 1

    return result


# Conflicting Appointments
def can_attend_all_appointments(intervals):
    intervals.sort()
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i+1][0]:
            return False
    return True


# Number Range
def find_range(arr, key):
    result = [-1, -1]
    left, right = 0, len(arr) - 1

    while left < right:
        middle = (right - left) // 2 + left
        if arr[middle] == key:
            left_side, right_side = middle, middle
            while arr[left_side] == key:
                result[0] = left_side
                left_side -= 1
            while arr[right_side] == key:
                result[1] = right_side
                right_side += 1
            break
        elif arr[middle] < key:
            left = middle + 1
        else:
            right = middle

    return result


# Minimum Difference Element
def search_min_diff_element(arr, key):
    left, middle, right,  = 0, (len(arr) - 1) // 2, len(arr) - 1
    while left < right and arr[middle] != key:
        middle = (right - left) // 2 + left
        if arr[middle] <= key:
            left = middle + 1
        else:
            right = middle

    if arr[middle] == key:
        oi = middle
    elif abs(arr[right] - key) > abs(arr[middle] - key):
        oi = middle
    else:
        oi = right

    return arr[oi]
