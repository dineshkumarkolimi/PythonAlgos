'''
    Write a function that takes two inputs n and m 
    and outputs the number of unique paths from the top 
    left corner to bottom right corner of an X m grid.

    Constraints: you can only move down or right 1 unit at a time.
'''

def numOfUniquePathsRecursive(n, m):
    if n == 1 or m == 1:
        return 1
    else:
        return numOfUniquePathsRecursive(n-1,m) + numOfUniquePathsRecursive(n,m-1)
    
def numOfUniquePathsDP(n, m):
    dp=[[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for i in range(n):
        dp[0][i] = 1

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
    
# print(numOfUniquePathsRecursive(4,3))
print(numOfUniquePathsDP(4,3))