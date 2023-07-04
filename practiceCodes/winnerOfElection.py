#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 23:18:55 2022

@author: dineshkumarkolimi

Program: Find winner of election and votes are represented as names
"""

votes = ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john"] 

map = {}

max_votes = 1
winner = [votes[0]]

for vote in votes:
    if map.get(vote) != None:
        map[vote] = map[vote] + 1
        if map[vote] > max_votes:
            max_votes=map[vote]
            winner[0] = vote
        if map[vote] == max_votes and winner[0]>vote:
            winner[0] =  vote
    else:    
        map.setdefault(vote, 1)
        
print(winner[0])

