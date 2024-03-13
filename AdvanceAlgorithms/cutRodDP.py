"""_summary_

    cut a rod of given lengths in such a way that it gives maximum profit
    by cutting them in given possible proportions.

    Given a rod of length n inches and an array of prices that includes prices of all pieces of size smaller than n. 
    Determine the maximum value obtainable by cutting up the rod and selling the pieces. 
    For example, if the length of the rod is 8 and the values of different pieces are given as the following, 
    then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6) 

    Dynamic Programming
    Complexity: O(n^2)
"""
def cutRodDP(arr, n):
    """_summary_

    Args:
        arr (_type_): _description_
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    dp_sol = [0 for i in range(n+1)]
    dp_sol[0] = 0
    for i in range(1,n+1):
        max_profit = -1
        for j in range(i):
            max_profit = max(max_profit , arr[j] + dp_sol[i-j-1])
        dp_sol[i] = max_profit
    return dp_sol[n]


if __name__ == "__main__":
    arr = [1,5,8,9,10,17,17,20]
    size = len(arr)
    max_profit = cutRodDP(arr,size)
    print("Maximum profit is: " + str(max_profit))
