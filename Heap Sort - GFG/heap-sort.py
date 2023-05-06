#User function Template for python3
from heapq import heappop,heappush
class Solution:
    def heapify(self,arr, n, i):
        pass
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        heap = []
        for i in arr:
            heappush(heap,i)
        for i in range(len(arr)):
            arr[i] = heappop(heap)
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        
        self.buildHeap(arr,n)
        #code here

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends