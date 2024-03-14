#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 15:44:34 2022

@author: dineshkumarkolimi

program: Sorting
"""

"""
    Selection sort is a simple and efficient sorting algorithm that works by 
    repeatedly selecting the smallest (or largest) element from the unsorted 
    portion of the list and moving it to the sorted portion of the list. 

    The algorithm repeatedly selects the smallest (or largest) element from
    the unsorted portion of the list and swaps it with the first element of
    the unsorted part. This process is repeated for the remaining unsorted 
    portion until the entire list is sorted. 
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

"""
    In Bubble Sort algorithm, 
        1. traverse from left and compare adjacent elements and the higher one is placed at right side. 
        2. In this way, the largest element is moved to the rightmost end at first. 
        3. This process is then continued to find the second largest and place it and so on until the data is sorted.
"""
def bubbleSort(arr):
    l = len(arr)
    for i in range(l-1):
        for j in range(i+1,l):
            if arr[j] < arr[i]:
                swap(arr,i,j)
            

"""
    Insertion sort is a simple sorting algorithm that works similarly to the way you sort playing cards
    in your hands. The array is virtually split into a sorted and an unsorted part. Values from the
    unsorted part are picked and placed in the correct position in the sorted part.

    To sort an array of size N in ascending order iterate over the array and compare the current element
    (key) to its predecessor, if the key element is smaller than its predecessor, compare it to the elements before. 
    Move the greater elements one position up to make space for the swapped element.
"""
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

"""
    Merge sort is defined as a sorting algorithm that works by dividing an array 
    into smaller subarrays, sorting each subarray, and then merging the sorted 
    subarrays back together to form the final sorted array.

    Merge sort is a recursive algorithm that continuously splits the array in half 
    until it cannot be further divided i.e., the array has only one element left 
    (an array with one element is always sorted). Then the sorted subarrays are merged into one sorted array.
"""
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

"""
    QuickSort is a sorting algorithm based on the Divide and Conquer algorithm 
    that picks an element as a pivot and partitions the given array around the picked 
    pivot by placing the pivot in its correct position in the sorted array.

    The key process in quickSort is a partition(). The target of partitions is to place 
    the pivot (any element can be chosen to be a pivot) at its correct position in the sorted 
    array and put all smaller elements to the left of the pivot, and all greater elements to the right of the pivot.

    Partition is done recursively on each side of the pivot after the pivot is placed
    in its correct position and this finally sorts the array.
"""
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

