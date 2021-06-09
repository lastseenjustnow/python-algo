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
