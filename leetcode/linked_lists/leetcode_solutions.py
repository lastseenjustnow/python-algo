class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def from_list(self, lst: list):
        return ListNode(lst[0], self.from_list(lst[1:])) if len(lst) > 0 else None

    def to_list(self):
        lst = []
        while self:
            lst.append(self.val)
            self = self.next

        return lst


class Solution:
    # 2. Add Two Numbers
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def addTwoNumbersRec(l1: ListNode, l2: ListNode, is_incr: int = 0):
            out = None
            if l1 or l2 or is_incr > 0:
                v1 = l1.val if l1 else 0
                v2 = l2.val if l2 else 0
                this_val = (v1 + v2 + is_incr) % 10
                this_residual = int((v1 + v2 + is_incr) / 10)
                l1_incr = l1.next if l1 else None
                l2_incr = l2.next if l2 else None
                out = ListNode(this_val, addTwoNumbersRec(l1_incr, l2_incr, this_residual))
                l1 = l1_incr
                l2 = l2_incr
            return out

        return addTwoNumbersRec(l1, l2)

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
