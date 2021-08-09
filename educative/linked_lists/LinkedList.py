import heapq

from educative.linked_lists.Node import Node, ArbitraryPointerNode
from typing import List

class LinkedList:
    def __init__(self):
        self.head_node = None

    def __eq__(self, other):

        self_head = self.get_head() if self else None
        other_head = other.get_head() if other else None

        while self_head or other_head:
            if not self_head or not other_head:
                return False
            if self_head.data != other_head.data:
                return False
            self_head = self_head.next_element
            other_head = other_head.next_element

        return True

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is None:  # Check whether the head is None
            return True
        else:
            return False

    # Supplementary print function
    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

    # Challenge 1: Insertion at Tail
    def insert_at_tail(self, value):
        if self.is_empty():
            self.head_node = Node(value)
        else:
            temp = self.get_head()
            while temp.next_element is not None:
                temp = temp.next_element
            temp.next_element = Node(value)

    # Auxiliary method to create a linked list from a list
    def from_list(self, lst):
        [self.insert_at_tail(x) for x in lst]
        return self

    # Challenge 2: Search in a Singly Linked List
    def search(self, value):
        # Write your code here
        if self.is_empty():
            return None
        else:
            head = self.get_head()

        while head:
            if head.data == value:
                return True
            head = head.next_element
        return False

    def delete_at_head(self):
        # Get Head and firstElement of List
        first_element = self.get_head()
        # If List is not empty then link head to the
        # nextElement of firstElement.
        if first_element is not None:
            self.head_node = first_element.next_element
            first_element.next_element = None
        return

    # Challenge 3: Deletion by Value
    def delete(self, value):
        first = self.get_head()

        if not first:
            return False

        if first.data == value:
            self.delete_at_head()
            self.delete(value)
            return True

        second = first.next_element
        d = False

        while second:
            if second.data == value:
                first.next_element = second.next_element
                d = True
            first = first.next_element
            second = second.next_element

        return d

    # Challenge 4: Find the Length of a Linked List
    def length(self):
        length = 0
        if self.is_empty():
            return length
        else:
            h = self.get_head()
            length += 1

        while h.next_element:
            h = h.next_element
            length += 1

        return length

    def insert_at_head(self, dt):
        temp_node = Node(dt)
        if self.is_empty():
            self.head_node = temp_node
            return self.head_node

        temp_node.next_element = self.head_node
        self.head_node.previous_element = temp_node  # what?
        self.head_node = temp_node
        return self.head_node

    # Challenge 5: Reverse a Linked List
    def reverse(self):
        rl = LinkedList()
        h = self.get_head()
        while h:
            rl.insert_at_head(h.data)
            h = h.next_element
        return rl

    # Challenge 6: Detect Loop in a Linked List
    def detect_loop(self):
        i1 = self.get_head()
        i2 = self.get_head()

        while i1 and i2 and i2.next_element:
            i1 = i1.next_element
            i2 = i2.next_element.next_element
            if i1 == i2:
                return True

        return False

    # Challenge 7: Find Middle Node of Linked List
    def find_mid(self):
        length = self.length()
        r = int(length / 2) + length % 2
        if self.is_empty():
            return None
        else:
            h = self.get_head()
        for _ in range(0, r - 1):
            h = h.next_element
        return h.data

    # Challenge 8: Remove Duplicates from Linked List
    def remove_duplicates(self):
        head = self.get_head()
        while head:
            first = head
            second = head.next_element
            while second:
                if second.data == head.data:
                    first.next_element = second.next_element
                    second = second.next_element
                    continue
                first = first.next_element
                second = second.next_element
            head = head.next_element
        return

    # Challenge 10: Return the Nth node from End
    def find_nth(self, n):
        # Write your code here
        length = self.length()
        if n > length:
            return -1
        h = self.get_head()
        for _ in range(0, length - n):
            h = h.next_element
        return h.data


# Challenge 9: Union & Intersection of Linked Lists
def union(list1, list2):
    # Write your code here
    l3 = LinkedList()

    h1 = list1.get_head() if list1 else None
    h2 = list2.get_head() if list2 else None

    while h1:
        l3.insert_at_tail(h1.data)
        h1 = h1.next_element

    while h2:
        l3.insert_at_tail(h2.data)
        h2 = h2.next_element

    l3.remove_duplicates()

    return l3


# Returns a list containing the intersection of list1 and list2


def intersection(list1, list2):
    # Write your code here
    l3 = LinkedList()

    l2 = list2.get_head()

    while l2:
        is_present = False
        l1 = list1.get_head()

        while l1:
            if l1.data == l2.data:
                is_present = True
                break
            l1 = l1.next_element

        if is_present:
            l3.insert_at_tail(l2.data)
        l2 = l2.next_element

    return l3


def find_happy_number(num):
    m = []
    c = 0
    while not c == 1:
        c = 0
        for i in str(num):
            c += int(i) ** 2
        if c in m:
            return False
        m.append(c)
        num = c

    return True


# Reverse every K-element Sub-list (medium)


# Using Linked List empty instance
def __reverse_every_k_elements_using_linked_list(head, k):
    out = None
    current_node = head
    last_node = None
    i = 1
    inner_linked_list = LinkedList()
    while current_node:
        inner_linked_list.insert_at_head(current_node.data)
        last_node = inner_linked_list.get_head() if last_node is None else last_node
        if i == k or not current_node.next_element:
            if not out:
                out = inner_linked_list
            else:
                while last_node.next_element:
                    last_node = last_node.next_element
                last_node.next_element = inner_linked_list.get_head()
            inner_linked_list = LinkedList()
            i = 0
        i += 1
        current_node = current_node.next_element

    return out if head else None


# Without Linked List empty instance
def reverse_every_k_elements(head, k):
    if k <= 1 or not head or not head.next_element:
        return head

    previous, current, following = None, head, head.next_element
    previous_sublist_last, current_sublist_last = None, None
    i = 1

    while True:
        if i == 1:
            current_sublist_last = current
        if i == k:
            if previous_sublist_last:
                previous_sublist_last.next_element = current
            else:
                head = current
            previous_sublist_last = current_sublist_last
            current_sublist_last.next_element = None
            i = 0
        if not following:
            current.next_element = previous
            if previous_sublist_last:
                previous_sublist_last.next_element = current
            current_sublist_last.next_element = None
            return head

        current.next_element = previous
        previous = current
        current = following
        following = following.next_element
        i += 1


# Rotate a Linked list
def rotate_list(head, n):
    i = 0
    if head:
        old_head = head
    else:
        return head

    length = 0
    while head:
        head = head.next_element
        length += 1

    head = old_head
    previous, current = None, head
    nth = length - n + int(n / length) * length - (length if n < 0 else 0)

    while i != nth:
        previous = current
        current = current.next_element
        i += 1

    result = current
    previous.next_element = None

    if current.next_element:
        while current.next_element:
            current = current.next_element

    current.next_element = old_head

    return result


# Add Two Integers Represented by Linked Lists
def add_integers(integer1: LinkedList, integer2: LinkedList) -> LinkedList:
    head1 = integer1.get_head()
    head2 = integer2.get_head()
    is_residual = 0

    head1_previous, head1_current = None, head1

    while head1_current or head2 or is_residual > 0:
        head_value1 = head1_current.data if head1_current else 0
        head_value2 = head2.data if head2 else 0
        nodes_sum = head_value1 + head_value2 + is_residual
        is_residual = int(nodes_sum > 9)
        if head1_current:
            head1_current.data = nodes_sum % 10
        else:
            head1_previous.next_element = Node(nodes_sum % 10)
            head1_current = head1_previous.next_element
        head1_previous = head1_current
        head1_current = head1_current.next_element if head1_current else None
        head2 = head2.next_element if head2 else None

    return head1


# Copy Linked List with Arbitrary Pointer
def deep_copy_arbitrary_pointer(head: ArbitraryPointerNode):

    ht = {}
    new_head = new_current = None

    while head:
        if new_head is None:
            new_head = ArbitraryPointerNode(head.data)
            new_head.arbitrary = head.arbitrary
            new_current = new_head
            ht[head] = new_current
        else:
            new_current.next_element = ArbitraryPointerNode(head.data)
            new_current = new_current.next_element
            new_current.arbitrary = head.arbitrary
            ht[head] = new_current
        head = head.next_element

    new_current = new_head

    while new_current:
        new_current.arbitrary = ht.get(new_current.arbitrary)
        new_current = new_current.next_element

    return new_head


# Merge K Sorted Lists (medium)
# Solution with list, no heap
def merge_lists_no_heap(lists: List[Node]):
    resultHead = None
    heads = [x for x in lists]
    while heads:
        values = list(map(lambda x: x.data, heads))
        min_value = min(values)
        min_value_index = values.index(min_value)
        if resultHead is None:
            resultHead = Node(min_value)
            current_node = resultHead
        else:
            current_node.next_element = Node(min_value)
            current_node = current_node.next_element
        heads[min_value_index] = heads[min_value_index].next_element
        heads = [x for x in heads if x]

    return resultHead


# Solution with heap
def merge_lists(lists: List[Node]):
    h = []
    [heapq.heappush(h, head.data) for head in lists]
    new_head = current = None
    heads = [x for x in lists]

    while h:
        next_min = heapq.heappop(h)
        if not new_head:
            new_head = Node(next_min)
            current = new_head
        else:
            current.next_element = Node(next_min)
            current = current.next_element
        for i in range(len(heads)):
            if heads[i].data == next_min:
                heads[i] = heads[i].next_element
                if heads[i]:
                    heapq.heappush(h, heads[i].data)
                else:
                    del heads[i]
                break

    return new_head