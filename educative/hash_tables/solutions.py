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
