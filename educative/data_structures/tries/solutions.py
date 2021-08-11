from TrieNode import TrieNode
from Trie import Trie

# Challenge 1: Total Number of Words in a Trie


def total_words(root: TrieNode) -> int:

    def total_words_rec(node: TrieNode, total: int) -> int:
        if node.children.count(None) == len(node.children):
            return total + 1 if node.is_end_word else total
        else:
            children_total = sum([total_words_rec(n, total) for n in node.children if n])
            return children_total + 1 if node.is_end_word else children_total

    return total_words_rec(root, 0)


# Challenge 2: Find All Words Stored in Trie
def find_words(root):
    words = []

    def find_words_rec(node: TrieNode, substr: str):
        if node.is_end_word:
            words.append(substr + node.char)
        [find_words_rec(child, substr + node.char) for child in node.children if child]

    find_words_rec(root, "")
    return words


# Challenge 3: List Sort Using Trie
def sort_list(arr):
    t = Trie()
    for w in arr:
        t.insert(w)

    return find_words(t.root)


# Challenge 4: Word Formation From a Dictionary Using Trie
def is_formation_possible(dictionary, word) -> bool:
    t = Trie()

    for w in dictionary:
        t.insert(w)

    current = t.root

    for outer_index, outer_ch in enumerate(word[:-1], 0):
        index = t.get_index(outer_ch)
        if current.children[index]:
            current = current.children[index]
        if current.is_end_word:
            nxt = t.root
            for inner_ch in word[outer_index+1:]:
                nxt = nxt.children[t.get_index(inner_ch)]
                if not nxt:
                    break
            if nxt and nxt.is_end_word:
                return True

    return False
