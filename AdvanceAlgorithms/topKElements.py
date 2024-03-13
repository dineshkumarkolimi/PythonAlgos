"""
    This is to find the first k top elements in the list
"""    
import heapq

"""_summary_

    Args:
        arr (_type_): array of elements
        k (_type_): to find the k top elements
        complexity : O(nlogn)
"""
def topKElements(arr,k):
    heapq.heapify(arr)
    for i in range(0, len(arr)-k):
        heapq.heappop(arr)
    print(arr)

"""_summary_

    Args:
         arr (_type_): array of elements
        k (_type_): to find the k top elements
        complexity : O(nlogk)
"""
def topKElementsBetter(arr,k):
    L=[]
    heapq.heapify(L)
    for i in range(k):
        heapq.heappush(L, arr[i])
    for i in range(k+1,len(arr)):
        heapq.heappush(L, arr[i])
        heapq.heappop()
    print(L)
    
    
if __name__ == "__main__":
    arr = [1,23,12,9,30,2,50]
    k = 3
    topKElements(arr, k)
    topKElementsBetter(arr,k)
