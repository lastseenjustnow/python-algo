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

