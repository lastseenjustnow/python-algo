from Node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def __eq__(self, other):

        self_head = self.get_head()
        other_head = other.get_head()

        while self_head or other_head:
            if not self_head or not other_head:
                print("1")
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
