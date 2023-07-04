#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:16:22 2022

@author: dineshkumarkolimi
program: Stack Implementation
"""
from queue import LifoQueue

def stackFromList():
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    
    print(stack)
    stack.pop()
    stack.pop()
    print(stack)
    
def stackFromQueue():
    stack = LifoQueue(maxsize=3)
    stack.put(1)
    stack.put(2)
    stack.put(3)
    
    print(stack)
    print(stack.full())
    
    stack.get()
    stack.get()
    stack.get()
    
    print(stack)
    print(stack.empty())
    
#From Node
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None;
        
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def strStack(self):
        cur = self.head
        out = ""
        if cur == None:
            print("stack is empty")
        else:
            while cur:
                out += str(cur.data) + "->"
                cur = cur.next
        return out
        
    def push(self,data):
        if self.size == 0:
            self.head = Node(data)
            print("entered")
        else:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp
        self.size += 1
        
    def pop(self):
        if self.size == 0:
            print("Stack is empty!")
            return
        else:
            temp = self.head.data
            self.head = self.head.next
            self.size -= 1
            return temp
        
        
        
if __name__ == "__main__":
    print("stack Implementation")
    head = None
    stack = Stack()
    for i in range(10):
        stack.push(i)
        
    print(stack.strStack())
    print(stack.pop())
    print(stack.pop())
    

