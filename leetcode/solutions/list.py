from typing import List, Tuple

import operator
import itertools

class ListSolution:

    # 3. Longest Substring Without Repeating Characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        length, max_length = 0, 0
        for char in s:
            if char in substring:
                max_length = length if length > max_length else max_length
                substring = substring[substring.index(char)+1:] + char
                length = len(substring)
            else:
                substring += char
                length += 1

        return length if length > max_length else max_length

    # Merge Sorted Array
    def mergeSortedArray(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1Copy = nums1[:m].copy()
        i = 0
        for _ in nums1:
            p1 = nums1Copy[0] if nums1Copy else None
            p2 = nums2[0] if nums2 else None
            if p1 is not None and p2 is not None:
                if p1 > p2:
                    nums1[i] = p2
                    nums2 = nums2[1:]
                else:
                    nums1[i] = p1
                    nums1Copy = nums1Copy[1:]
            elif p1 is not None:
                nums1[i] = p1
                nums1Copy = nums1Copy[1:]
            else:
                nums1[i] = p2
                nums2 = nums2[1:]
            i += 1

    # 56. Merge Intervals
    def merge_intervals(self, intervals: List[List[int]]) -> List[List[int]]:
        out: List[List[int]] = []
        for interval in sorted(intervals, key=operator.itemgetter(0)):
            is_updated = False
            for index_new_interval, new_interval in enumerate(out, 0):
                if new_interval[0] <= interval[0] <= new_interval[1]:
                    out[index_new_interval] = [new_interval[0], max(new_interval[1], interval[1])]
                    is_updated = True
                    break
            if is_updated:
                continue
            out.append(interval)

        return out

    # Has attempted to make inplace update of intervals, but it didn't improve memory usage
    def merge_intervals_in_place(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=operator.itemgetter(0))
        i = 0
        for outer_interval in sorted_intervals[i:]:
            is_updated = False
            for inner_index, inner_interval in enumerate(sorted_intervals[:i], 0):
                if inner_interval[0] <= outer_interval[0] <= inner_interval[1]:
                    sorted_intervals[inner_index] = [inner_interval[0], max(inner_interval[1], outer_interval[1])]
                    is_updated = True
                    break
            if is_updated:
                del sorted_intervals[i]
            else:
                i += 1

        return sorted_intervals

    # 200. Number of Islands
    # Must be resolved with graphs!
    def numIslands(self, grid: List[List[str]]) -> int:
        max_x = len(grid[0])
        max_y = len(grid)
        x_coord = [x for x in range(max_x)]
        y_coord = [y for y in range(max_y)]
        existing_coordinates = [x[::-1] for x in itertools.product(y_coord, x_coord)]
        grid_values = [x for y in grid for x in y]
        landmark_coords = {coords for coords, is_land in zip(existing_coordinates, grid_values) if int(is_land)}
        count = 0

        def remove_neighbors(st: set, elem: Tuple):
            if elem in st:
                st.remove(elem)
                remove_neighbors(st, (elem[0] + 1, elem[1]))
                remove_neighbors(st, (elem[0] - 1, elem[1]))
                remove_neighbors(st, (elem[0], elem[1] + 1))
                remove_neighbors(st, (elem[0], elem[1] - 1))
            else:
                return

        while landmark_coords:
            count += 1
            remove_neighbors(landmark_coords, next(iter(landmark_coords)))

        return count
