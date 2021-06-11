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


class LinkedListSolution:
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

    # 1041. Robot Bounded In Circle
    def isRobotBounded(self, instructions: str) -> bool:
        """
        On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

        "G": go straight 1 unit;
        "L": turn 90 degrees to the left;
        "R": turn 90 degrees to the right.
        The robot performs the instructions given in order, and repeats them forever.

        Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
        :param instructions:
        :return:
        """
        k = 0
        current_position = (0, 0)
        x_incr, y_incr = (0, 1)
        for i in instructions * 4:
            if i == 'G':
                current_position = (current_position[0] + x_incr, current_position[1] + y_incr)

            else:
                k = k + 1 if i == 'R' else k - 1
                x_incr = (1 - abs(x_incr)) * (-1) ** int(abs((k + 3)/2))
                y_incr = (1 - abs(y_incr)) * (-1) ** int(abs((k + 4)/2))

        return current_position == (0, 0)
