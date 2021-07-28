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
