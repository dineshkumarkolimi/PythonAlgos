"""
    This is to find the first k top elements in the list
"""    
import heapq

def topKElements(arr,k):
    """_summary_

    Args:
        arr (_type_): array of elements
        k (_type_): to find the k top elements
        complexity : O(nlogn)
    """
    heapq.heapify(arr)
    for i in range(1, len(arr)-k+1):
        heapq.heappop(arr)
    print(arr)
    
def topKElementsBetter(arr,k):
    """_summary_

    Args:
         arr (_type_): array of elements
        k (_type_): to find the k top elements
        complexity : O(nlogk)
    """
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