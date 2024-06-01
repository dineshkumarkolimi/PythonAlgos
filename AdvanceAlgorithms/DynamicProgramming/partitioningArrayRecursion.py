''' Write a program that counts the number of ways you can n objects using 
    partitions upto m assuming m>=0'''

def numPartitionsRecursive(n,m):
    if n == 0:
        return 1
    if m == 0:
        return 0
    if n<0 or m<0:
        return 0
    return (numPartitionsRecursive(n-m,m) + numPartitionsRecursive(n,m-1))

def numPartitionsDP(n,m):
    if n == 0:
        return 1
    if m == 0:
        return 0
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
        dp[i][1] = 1
    for j in range(1, n+1):
        for k in range(1, m+1):
            if j-k >=0:
                print(j, k-1, j-k, k)
                dp[j][k] += dp[j][k-1] + dp[j-k][k]
            # print(dp)
    return dp[n][m]

n=9
m=5
print(numPartitionsRecursive(n,m))
# print(numPartitionsDP(n,m))