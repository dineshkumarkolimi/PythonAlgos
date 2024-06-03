'''Find longest common substring between two strings provided'''


def longestCommonSubsequence(text1: str, text2: str) -> int:
    n1 = len(text1)
    n2 = len(text2)
    dps = [[0 for i in range(n2+1)] for j in range(n1+1)]
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            dps[i][j] += max(dps[i][j-1], dps[i-1][j], dps[i-1][j-1]) + (1 if text1[i-1]==text2[j-1] else 0)
    return dps[n1][n2]

a = "abcde"
b = "abc"
print(longestCommonSubsequence(a,b))
