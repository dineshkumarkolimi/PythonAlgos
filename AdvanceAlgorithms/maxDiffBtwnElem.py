#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 19:34:48 2022

@author: dineshkumarkolimi

Program: Maximum difference between two elements such that larger element appears after the smaller number
"""

def maxDiff(arr,n):
    maxDiff = arr[1] - arr[0]
    minElement = arr[0]
    
    for i in range(1,n):
        if arr[i] - minElement > maxDiff:
            maxDiff = arr[i] - minElement
        if arr[i] < minElement:
            minElement = arr[i]
    return maxDiff

if __name__ == "__main__":
    a = [2, 3, 10, 6, 4, 8, 1]
    print(maxDiff(a, len(a)))
    b = [7, 9, 5, 6, 3, 2]
    print(maxDiff(b,len(b)))