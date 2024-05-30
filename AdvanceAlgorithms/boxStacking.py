''' This code solves the problem of box stacting with maximum possible height

    L = [(4,5,3), (2,3,2), (3,6,2), (1,5,4), (2,4,1), (1,2,2)]
'''

def boxStackingLen(L):
    L.sort(key = lambda x: x[0])
    print(L)
    dp = [item[2] for item in L]
    print(dp)
    n = len(L)
    for i in range(n):
        for j in range(i):
            if L[j][0] < L[i][0] and L[j][1] < L[i][1] and dp[i] < dp[j] + L[i][2]:
                dp[i] = dp[j] + L[i][2]
    return max(dp)

def boxStacking(L):
    L.sort(key = lambda x: x[0])
    dp = [item[2] for item in L]
    n = len(L)
    prev = [-1]*n
    result = []
    for i in range(n):
        for j in range(i):
            if L[j][0] < L[i][0] and L[j][1] < L[i][1] and dp[i] < dp[j] + L[i][2]:
                dp[i] = dp[j] + L[i][2]
                prev[i] = j
    max_index = dp.index(max(dp))
    while max_index != -1:
        result.insert(0, L[max_index])
        max_index = prev[max_index]
    return result

L = [(4,5,3), (2,3,2), (3,6,2), (1,5,4), (2,4,1), (1,2,2)]
print(boxStacking(L))
print(boxStackingLen(L))