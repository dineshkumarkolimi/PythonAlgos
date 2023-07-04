"""_summary_

    Target sum or coins problem to find out respective possibilities
    to reach a target sum. 
"""

answer = []

def targetSum(coins, current_index, current_sum, combination, target):
    """_summary_

    Args:
        coins (_type_): _description_
        current_index (_type_): _description_
        current_sum (_type_): _description_
        combination (_type_): _description_
        target (_type_): _description_
    """
    if current_sum == target:
        answer.append(combination)
        return
    if current_sum>target:
        return
    for i in range(current_index,len(coins)):
        targetSum(coins, i, current_sum + coins[i], combination + [coins[i]], target)
        
if __name__=='__main__':
    coins = [2,3,5]
    target = 8
    targetSum(coins, 0,0,[],target)
    print(answer)
    print(len(answer))