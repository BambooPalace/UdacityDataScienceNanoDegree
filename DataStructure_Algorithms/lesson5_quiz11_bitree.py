#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 22:32:15 2020

@author: clairegong
"""

class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.preorder_search(tree.root, find_val)

    def print_tree(self):
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False
    
    def preorder_search(self, start, value):
        if start:#if node is true
            if start.value == value:
                return True
            else:
                return self.preorder_search(start.left,value) or self.preorder_search(start.right, value)
        return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
#            print('traversing: ',start.value)#test
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def preorder_traversal(self, start, traversal):
        #if node is empty, do nothing
        if start:
            traversal.append(start.value)
            traversal = (self.preorder_traversal(start.left, traversal))
            traversal = (self.preorder_traversal(start.right, traversal))
        return traversal
        


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.right.right = Node(7)
tree.root.right.right = Node(6)

# Test search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print (tree.print_tree())
print(tree.preorder_traversal(tree.root, []))