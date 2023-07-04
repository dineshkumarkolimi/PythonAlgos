#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 20:17:56 2022

@author: dineshkumarkolimi

Program: Stock Buy Sell to Maximize Profit
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