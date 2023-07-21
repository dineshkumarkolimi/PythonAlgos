"""_summary_

    This is a knapsack fraction problem which uses Greedy Algorithm. 
    This algo will return maximum profit for a given target weight 
    using a given sack of weigths available and corresponding profits.

    Complexity: O(nlogn)
    Greedy Algorithm: https://www.geeksforgeeks.org/greedy-algorithms/
"""
class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit

def knapSackProb(targetWeight, arr):
    """This method returns maximum profit that can be achieved using the given
        weights and profits for a given amount of target weight.

    Args:
        targetWeight (float): This is the profit that we need to achieve
                             using the given weights
        arr (Item): This items contain Item comprising of weights and profits
    """
    arr.sort(reverse = True, key=lambda x: (x.profit/x.weight))
    totalProfit = 0
    for item in arr:
        if item.weight <= targetWeight:
            targetWeight -= item.weight
            totalProfit += item.profit
        else:
            totalProfit += item.profit * targetWeight/item.weight
            break
    return totalProfit
    


if __name__ == "__main__":
    arr = [Item(10,60), Item(20,100), Item(30,120)]
    Weight = 50
    max_profit = knapSackProb(Weight, arr)
    print(max_profit)