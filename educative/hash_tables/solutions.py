from HashTable import HashTable
from educative.linked_lists.LinkedList import LinkedList
from educative.linked_lists.Node import Node


# Challenge 1. A List as a Subset of Another List
def is_subset(list1, list2):
    # Write your code here
    set1 = set(list1)
    set2 = set(list2)

    return set2.issubset(set1)


# Challenge 2: Check if Lists are Disjoint
def is_disjoint(list1, list2):
    for el in list2:
        if el in set(list1):
            return False

    return True


# Challenge 3: Check if Lists are Disjoint
def find_symmetric(my_list):
    dct = dict(my_list)
    out = []

    for val in dct.values():
        if dct.get(val) is not None:
            out.append([dct[val], val])

    return out


# Challenge 4: Trace the Complete Path of a Journey
def trace_path(my_dict: dict):
    set_dests = set(my_dict.values())
    out = []
    for k in my_dict.keys():
        if k not in set_dests:
            break

    while my_dict.get(k):
        pair = [k, my_dict[k]]
        out.append(pair)
        k = pair[1]

    return out


# Challenge 5: Find Two Pairs in List such that a+b = c+d
def find_pair(my_list):
    dct = {}
    for index1, elem1 in enumerate(my_list, 0):
        for elem2 in my_list[index1+1:]:
            if dct.get(elem1 + elem2) is None:
                dct[elem1 + elem2] = [elem1, elem2]
            else:
                pair = dct.get(elem1 + elem2)
                if elem1 in pair or elem2 in pair:
                    continue
                else:
                    return [pair, [elem1, elem2]]
    return None


# Challenge 6: A Sublist with a Sum of 0
def find_sub_zero(my_list):
    st = set()
    s = 0
    for elem in my_list:
        s += elem
        if elem == 0 or s == 0 or s in st:
            return True
        else:
            st.add(elem)
    return False


# Challenge 7: Word Formation Using a Hash Table
def is_formation_possible(lst, word):
    ht = HashTable()
    for elem in lst:
        ht.insert(elem, elem)

    for index1, elem1 in enumerate(word, 0):
        v1, v2 = tuple([ht.search(x) for x in [word[:index1], word[index1:]]])
        if v1 and v2:
            return True

    return False


# Challenge 8: Find Two Numbers that Add up to "k"

# HashTable solution
def findSum_HashTable(lst, k):
    ht = HashTable()
    for elem in lst:
        ht.insert(elem, elem)

    for elem in lst:
        v = ht.search(k - elem)
        if v is not None:
            return [elem, v]

    return None


# Set solution
def findSum(lst, k):
    st = set()

    for elem in lst:
        v = k - elem
        if v in st:
            return [elem, v]
        else:
            st.add(elem)

    return None


# Challenge 9: First Non-Repeating Integer in a List
def findFirstUnique(lst):
    dct = dict()
    for elem in lst:
        if dct.get(elem) is None:
            dct[elem] = 1
        else:
            dct[elem] += 1

    for elem in lst:
        if dct.get(elem) == 1:
            return elem

    return None


# Challenge 10: Detect Loop in a Linked List
def detect_loop(lst: LinkedList):
    st = set()

    head = lst.get_head()
    while head:
        if head.data in st:
            return True
        st.add(head.data)
        head = head.next_element

    return False


# Challenge 11: Remove Duplicates from Linked List
def remove_duplicates(lst: LinkedList):

    if not lst.get_head().next_element:
        return

    previous = lst.get_head()
    head = lst.get_head().next_element
    st = {previous.data}

    while head:
        if head.data in st:
            previous.next_element = head.next_element
            head = head.next_element
            continue
        st.add(head.data)
        previous, head = tuple([x.next_element for x in [previous, head]])


# Challenge 12: Union & Intersection of Linked Lists
def union(list1: LinkedList, list2: LinkedList):
    head = list1.get_head()

    while head.next_element:
        head = head.next_element

    head.next_element = list2.get_head()
    remove_duplicates(list1)

    return list1

# Returns a list containing the intersection of list1 and list2


def intersection(list1, list2):
    head = list1.get_head()
    st = set()

    while head:
        st.add(head.data)
        head = head.next_element

    head = list2.get_head()
    list3 = LinkedList()

    while head:
        if head.data in st:
            list3.insert_at_tail(head.data)
        head = head.next_element

    return list3

