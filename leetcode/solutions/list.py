import operator
from typing import List

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
