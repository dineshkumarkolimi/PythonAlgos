"""_summary_

    Target sum or coins problem to find out respective possibilities
    to reach a target sum. This is using Dynamic Programming Algorithm.
"""

def coinChange(coins, n, sum):
    """_summary_

    Args:
        coins (_list_): List of coins 
        n (_int_): number of coins
        sum (_int_): target sum to achieve

    Returns:
        int: returns number of possibilities to get to the target sum.
    """
    dp_sum = [0 for k in range(sum+1)]
    dp_sum[0] = 1

    for i in range(n):
        for j in range(coins[i], sum+1):
            dp_sum[j]  += dp_sum[j - coins[i]]

    return dp_sum[sum]

if __name__ == "__main__":
    # coins = [1,2,5,10,100]
    # sum = 124
    coins = [2,3,5]
    sum = 8
    print(coinChange(coins, len(coins), sum))