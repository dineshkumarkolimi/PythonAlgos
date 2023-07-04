#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:48:29 2022

@author: dineshkumarkolimi

program: priority queue or min heap
"""
import heapq

def priorityQueue():
    L = [2,4,3,7,8,6,9]
    heapq.heapify(L)
    
    heapq.heappush(L, 1)
    heapq.heappush(L, 5)
    print(list(L))
    print(heapq.heappop(L))
    print(heapq.heappop(L))
    print(list(L))
    
