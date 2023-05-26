import heapq
from heapq import heappush

def heapify_up(heap,index):
    par = (index - 1)//2
    if heap[par] > heap[index]:
        heap[par],heap[index] = heap[index],heap[par]
        index = par
        heapify_up(heap,index)
    return heap

def heappush(heap,value):
        heap.append(value)
        current = len(heap) - 1
        heap = heapify_up(heap,current)
        heappush(heap, 3)
def test():
    heap = [2, 4, 7, 9, 10, 5]
    assert heap == [2, 4, 3, 7, 9, 10, 5], f"Error: expected [2, 4, 3, 7, 9, 10, 5], but got {heap}"

    heap = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    heappush(heap, 0)
    assert heap == [0, 1, 3, 4, 2, 6, 7, 8, 9, 5], f"Error: expected [0, 2, 1, 4, 5, 6, 7, 8, 9, 3], but got {heap}"
   
    print("Great Job !!!")
test()


