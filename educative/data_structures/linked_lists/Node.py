from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next_element
        print()

    def to_list(self):
        lst = []
        while self:
            lst.append(self.data)
            self = self.next_element

        return lst


class ArbitraryPointerNode:
    def __init__(self, data):
        self.data = data
        self.next_element: Optional[ArbitraryPointerNode] = None
        self.arbitrary: Optional[ArbitraryPointerNode] = None
