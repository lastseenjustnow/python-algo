from MinHeap import MinHeap
from MaxHeap import MaxHeap


# Challenge 1: Convert Max-Heap to Min-Heap
def convertMax(maxHeap):
    len_max_heap = len(maxHeap)

    def rec(heap_array, i):
        if i > len_max_heap - 1:
            return heap_array
        min_i, stack = i, {i}
        while stack:
            current_i = stack.pop()
            if current_i > len_max_heap - 1:
                continue
            if heap_array[current_i] < heap_array[min_i]:
                min_i = current_i
            stack.add((current_i + 1) * 2 - 1)
            stack.add((current_i + 1) * 2)
        heap_array[min_i], heap_array[i] = heap_array[i], heap_array[min_i]
        rec(heap_array, (i + 1) * 2 - 1)
        rec(heap_array, (i + 1) * 2)
        return heap_array

    return rec(maxHeap, 0)


# Challenge 2: Find k smallest elements in a List
def findKSmallest(lst, k):

    heap = MinHeap()
    heap.buildHeap(lst)
    res = []
    for _ in range(k):
        res.append(heap.getMin())
        heap.removeMin()

    return res


# Challenge 3: Find k largest elements in the List
def findKLargest(lst, k):
    heap = MaxHeap()
    heap.buildHeap(lst)
    return [heap.removeMax() for _ in range(k)]
