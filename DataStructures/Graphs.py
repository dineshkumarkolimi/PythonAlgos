#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:39:56 2022

@author: dineshkumarkolimi

Program: Depth first search For a graph
"""

from collections import defaultdict

class Graph:
    def __init__(self, Vertices):
        self.graph = defaultdict(list)
        self.V = Vertices
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def BFS(self,v):
        visited = set()
        self.BFStraversal(v,visited)
        
    def BFSdisconnectedGraph(self):
        visited = set()
        for v in self.graph:
            if v not in visited:
                self.BFStraversal(v,visited)
        
    def BFStraversal(self,v,visited):
        print(v)
        visited.add(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.BFStraversal(neighbour,visited)
                
    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                self.topologicalSortUtil(neighbour, visited, stack)
        stack.append(v)
                
    
    def topologicalSort(self):
        visited = [False]*self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
                
        print(stack[::-1])
                
    

if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
 
    print("Following is a Topological Sort of the given graph")
 
    # Function Call
    g.topologicalSort()