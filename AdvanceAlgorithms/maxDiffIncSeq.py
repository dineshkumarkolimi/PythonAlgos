import sys

def maxDiff(arr,n):
    max_diff = -sys.maxsize - 1
    prev = arr[0]
    min_ele = arr[0]
    for i in range(1, n):
        if arr[i] > prev:
            prev = arr[i]
            if prev - min_ele > max_diff:
                max_diff = prev-min_ele
        else:
            min_ele = arr[i]
            prev = arr[i]

    return max_diff if max_diff != -sys.maxsize-1 else 0

print(maxDiff([2,3,10,6,4,8,1], 7))
print(maxDiff([7,9,5,6,3,2], 6))
print(maxDiff([5,4,3], 3))
print(maxDiff([-2,-1], 2))
print(maxDiff([2,3,10,6,4,8,1,13], 8))
