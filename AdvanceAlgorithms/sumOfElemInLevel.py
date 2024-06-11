'''

           1
        2     4
    5      7      9
10    13    15      16

Given a list of integers return the sum of each level of the pyramid.
For example: in the above example L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
and sum of 2nd level is 9

'''

L = 3

def levelSum(L, level):
    start = ((level-1)*(level))//2
    sum = 0
    for i in range(start,start + level):
        sum += L[i]   
    return sum

L =[ 1,2,4,5,7,9,10,13,15,16]
print(levelSum(L,4))