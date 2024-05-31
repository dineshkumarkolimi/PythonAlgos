'''This code calculates some of all the elements in a list using recursion techniques'''

def sum(A, n):
    if n == 0:
        return 0
    else:
        return A[n-1] + sum(A,n-1)
    
def sumTailRecur(A,n,sum=0):
    if n == 0:
        return sum
    else:
        return sumTailRecur(A,n-1,sum+A[n-1])
    
def sumDP(A):
    n = len(A)
    if n == 0:
        return 0
    dp = [0]*n
    dp[0] = A[0]
    for i in range(1, n):
        dp[i] = A[i] + dp[i-1]
    return dp[n-1]

A = [1,2,3,4,5,6,7,8,9,10,11]
print(sum(A,len(A)))
print(sumTailRecur(A,len(A), 0))
print(sumTailRecur(A,len(A)))
print(sumDP(A))