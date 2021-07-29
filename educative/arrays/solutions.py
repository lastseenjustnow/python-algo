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
