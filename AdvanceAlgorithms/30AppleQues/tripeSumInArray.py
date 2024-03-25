"""
    Problem: Given an array arr[] of size n and an integer X. 
        Find if there's a triplet in the array which sums up to the given integer X.
"""

def find3Numbers(A, n, sum):
    arr = set(A)
    result = set()
    for i in range(len(A) - 2):
        target_sum = sum - A[i]
        for j in range(i+1, len(A)):
            target_sum = target_sum - A[j]
            if target_sum in arr and target_sum != A[i] and target_sum != A[j]:
                result.add((A[i], A[j], target_sum))
    print(len(result))



if __name__ == '__main__':
    A = [1, 4, 45, 6, 10, 8]
    sum = 22
    arr_size = len(A)
    find3Numbers(A, arr_size, sum)