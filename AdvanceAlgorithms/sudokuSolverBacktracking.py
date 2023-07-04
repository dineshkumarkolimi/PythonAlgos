#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 2023

@author: dineshkumarkolimi

program: Sudoku solver using backtracking algorithm
"""

def findEmptyLocation(arr,l):
    """_summary_
    Args:
        arr (int): sudoku with rows and coloumns
    Returns:
        boolean: returns whether sudoku is solved or not
    """    
    # iterating over rows and columns
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False

def presentInRow(arr,num,row):
    for i in range(9):
        if arr[row][i] == num:
            return True
    return False

def presentInCol(arr,num,col):
    for i in range(9):
        if arr[i][col] == num:
            return True
    return False

def presentInCell(arr,num, row,col):
    for i in range(3):
        for j in range(3):
            if arr[row+i][col+j] == num:
                return True
    return False

def checkIsNumSafe(arr,num,row,col):
    return not presentInRow(arr,num,row) and \
        not presentInCol(arr,num,col) and \
            not presentInCell(arr,num,row-row%3,col-col%3)

def sudokuSolver(arr):
    """_summary_

    Args:
        arr (int): sudoku with rows and coloumns

    Returns:
        boolean: returns true once sudoku is solved
    """    
    l=[0,0]
    
    if not findEmptyLocation(arr,l):
        return True
    
    row = l[0]
    col = l[1]
    
    for num in range(1,10):
        if checkIsNumSafe(arr,num,row,col):
            arr[row][col] = num
        
            if sudokuSolver(arr):
                return True
        
            arr[row][col] = 0
            
    return False

def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" ")
        print()

if __name__=='__main__':
    # creating a 2D array for the grid
    grid =[[0 for x in range(9)]for y in range(9)]
     
    # assigning values to the grid
    grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    
    if sudokuSolver(grid):
        print_grid(grid)
    else:
        print("No solution exists")
    
    
    