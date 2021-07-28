from collections import deque


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
