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

