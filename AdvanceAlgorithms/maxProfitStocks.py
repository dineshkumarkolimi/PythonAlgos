#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 20:17:56 2022

@author: dineshkumarkolimi

Program: Stock Buy Sell to Maximize Profit
    The cost of a stock on each day is given in an array.
    Find the maximum profit that you can make by buying and
    selling on those days. If the given array of prices is sorted
    in decreasing order, then profit cannot be earned at all.

Examples:

Input: arr[] = {100, 180, 260, 310, 40, 535, 695}
Output: 865
Explanation: Buy the stock on day 0 and sell it on day 3 => 310 – 100 = 210
                       Buy the stock on day 4 and sell it on day 6 => 695 – 40 = 655
                       Maximum Profit  = 210 + 655 = 865

Input: arr[] = {4, 2, 2, 2, 4}
Output: 2
Explanation: Buy the stock on day 1 and sell it on day 4 => 4 – 2 = 2
                       Maximum Profit  = 2
"""

def maxProfit(arr,n):
    maxProfit = 0
    for i in range(0,n-1):
        if arr[i+1] > arr[i]:
            maxProfit += (arr[i+1]-arr[i])
    return maxProfit

if __name__ == "__main__":
    a=[100, 180, 260, 310, 40, 535, 695]
    print(maxProfit(a,len(a)))
    b=[4, 2, 2, 2, 4]
    print(maxProfit(b,len(b)))
