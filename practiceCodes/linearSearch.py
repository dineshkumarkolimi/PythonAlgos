#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 12:30:54 2022

@author: dineshkumarkolimi

Program: Linear Search, Binary Search
"""

def linearSearch(arr, item):
    for ele in arr:
        if ele == item:
            return True
    return False

def binarySearch(arr, item):
    mid = len(arr)//2
    if(mid >  0):
        if arr[mid] == item:
            return True
        elif arr[mid] > item:
            return binarySearch(arr[:mid], item)
        else:
            return binarySearch(arr[mid+1:],item)

if __name__ == "__main__":
    arr = [2,3,4,10,40,50]
    X = 10
    arr.sort()
    if binarySearch(arr, X):
        print("Item Found")
    else:
        print("Item Not Found")

