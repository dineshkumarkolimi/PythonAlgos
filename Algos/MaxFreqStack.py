#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 12:44:35 2022

@author: dineshkumarkolimi

Program: Design a stack which can give maximum frequency element
"""
# class Node:
#     def __init__(self, data, freq):
#         self.data = data
#         self.freq = freq

class maxFreqStack:
    hashMap = {}
    stack = []
    freq = []
    maxFreqIndex = 0
        
    
    def push(self, item):
        if(self.hashMap.get(item) == None):
            self.hashMap[item] = 1
        else:
            self.hashMap[item] += 1
        
        self.freq.append(self.hashMap[item])
        self.stack.append(item)
        
        if self.hashMap[item] >= self.freq[self.maxFreqIndex]:
            self.maxFreqIndex = len(self.freq)-1
        
    def pop(self):
        poppedElement = self.stack[self.maxFreqIndex]
        self.stack.pop(self.maxFreqIndex)
        self.hashMap[poppedElement] -= 1
        self.freq.pop(self.maxFreqIndex)
        self.maxFreqIndex = self.findMax()
        return poppedElement
    
    def findMax(self):
        maxEle = max(self.freq)
        for i in range(len(self.freq)-1,0,-1):
            if self.freq[i] == maxEle:
                return i
    
if __name__ == "__main__":
    stack = maxFreqStack()
    stack.push(4)
    stack.push(6)
    stack.push(7)
    stack.push(6)
    stack.push(8)
    stack.push(8)
    stack.push(8)
    stack.push(7)
    
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
        
        
        
        


