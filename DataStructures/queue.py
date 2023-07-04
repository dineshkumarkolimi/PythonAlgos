#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:36:58 2022

@author: dineshkumarkolimi

Program: Queue Implementation
"""

from queue import Queue

def queueFromList():
    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)
    
    print(queue)
    queue.pop(0)
    queue.pop(0)
    
    print(queue)
    
def queueFromQueue():
    q = Queue(maxsize=3)
    q.put(1)
    q.put(2)
    q.put(3)
    
    print(q.full())
    print(q)
    
    q.get()
    q.get()
    q.get()
    print(q)
    print(q.empty())