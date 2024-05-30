''' Writing the code for the longest increasing subsequence in a list of Integers

For example:
1. L = [2,5,3,10,1]
    Solution: LIS = [2,5,10]
              length = 3
              
2. L = [5,2,8,6,3,6,9,5]
    Solution: LIS = [2,3,6,9]
              length = 4'''


def LISLen(A):
    L = [1]*len(A)
    for i in range(len(L)):
        subProblems = [L[k] for k in range(i) if A[k] < A[i]]
        L[i] = 1 +max(subProblems, default=0)
    return max(L)

def LIS(A):
    n = len(A)
    L = [1]*n
    result  = []
    prev = [-1]*n
    for i in range(n):
        for j in range(i):
            if A[i] > A[j] and L[i] < L[j]+1:
                L[i] = L[j]+1
                prev[i] = j
    max_index = L.index(max(L))
    print(L)
    while max_index != -1:
        result.insert(0,A[max_index])
        max_index = prev[max_index]
    return result

nums = [10,9,2,5,3,7,101,18]
print(LIS(nums))
print(LISLen(nums))


