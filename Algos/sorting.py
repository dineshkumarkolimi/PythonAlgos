#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 15:44:34 2022

@author: dineshkumarkolimi

program: Sorting
"""

def selectSort(arr):
    l = len(arr)
    for i in range(l-1):
        min = i
        for j in range(i+1,l):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            swap(arr,i,min)
            
def bubbleSort(arr):
    l = len(arr)
    for i in range(l-1):
        for j in range(i+1,l):
            if arr[j] < arr[i]:
                swap(arr,i,j)
            
                
def insertionSort(arr):
    l = len(arr)
    for i in range(l-1):
        j = i+1
        while(j>0):
            if arr[j]<arr[j-1]:
                swap(arr,j,j-1)
                j -= 1
            else:
                break
        
def mergeSort(arr):
    l = len(arr)
    if l>1:
        mid = l//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        
        i = j = k = 0
        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            elif L[i] > R[j]:
                arr[k] = R[j]
                j+=1
            else:
                arr[k] = L[i]
                j+=1
                i+=1
            k+=1
                
        while i<len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k] = R[j]
            j+=1
            k+=1
            
def quickSort(arr, low, high):
    if(low<high):
        pivot = partition(arr,low,high)
        quickSort(arr,low,pivot-1)
        quickSort(arr,pivot+1,high)

def partition(arr,low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            (arr[i],arr[j]) = (arr[j],arr[i])
    (arr[i+1],arr[high]) = (arr[high],arr[i+1])
    return i+1
    
        
def swap(arr,i,j):
    arr[i] = arr[i] + arr[j]
    arr[j] = arr[i] - arr[j]
    arr[i] = arr[i] - arr[j]

if __name__ == "__main__":
    a = [64, 25, 12, 22, 11, 45, 4] 
    quickSort(a,0,len(a)-1)
    print(a)

