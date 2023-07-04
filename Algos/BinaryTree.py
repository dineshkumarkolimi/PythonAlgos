#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 21:29:18 2022

@author: dineshkumarkolimi

Program: Tree Implementation
"""

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
class Tree:
        
    def insert(self, root, data):
        if root is None:
            root = Node(data)
        else:
            if(root.data >= data):
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
        return root
            
    def search(self, root, item):
        if root is None:
            return False
        else:
            if root.data == item:
                return True
            elif item > root.data:
                return self.search(root.right, item)
            else:
                return self.search(root.left, item)
            
    def height(self, root):
        if root == None:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1
        
    def preOrder(self, root):
        if root:
            print(root.data)
            self.preOrder(root.left)
            self.preOrder(root.right)
    
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.data)
            self.inOrder(root.right)
            
    def postOrder(self,root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data)
    
    def levelOrder(self,root):
        h = self.height(root)
        for i in range(1,h+1):
            self.printLevel(root, i)
            
    def printLevel(self, root, level):
        if root == None:
            return
        if level == 1:
            print(root.data)
        else:
            self.printLevel(root.left, level-1)
            self.printLevel(root.right, level-1)
            
    def reverseLevelOrder(self,root):
        h = self.height(root)
        for i in range(h+1,0,-1):
            self.printLevel(root,i)
    

if __name__ == "__main__":
    root = None
    tree = Tree()
    root = tree.insert(root, 8)
    root = tree.insert(root, 6)
    root = tree.insert(root, 10)
    root = tree.insert(root, 1)
    root = tree.insert(root, 2)
    root = tree.insert(root, 4)
    root = tree.insert(root, 9)
    root = tree.insert(root, 7)
    print(tree.search(root, 6))
    print(tree.search(root, 9))
    print(tree.height(root));
    tree.preOrder(root)
    tree.inOrder(root)
    tree.postOrder(root)
    tree.levelOrder(root)
    tree.reverseLevelOrder(root)
    
    