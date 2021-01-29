#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 11:29:33 2020

@author: clairegong
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)
    
# O(logn)    
    def insert_helper(self, parent, new_val):
        if new_val < parent.value:
            if parent.left == None:
                parent.left = Node(new_val)
                
            else:
                self.insert_helper(parent.left, new_val)
        elif new_val > parent.value:
            if parent.right == None:
                parent.right = Node(new_val)
                
            else:
                self.insert_helper(parent.right, new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)
#O(logn)    
    def search_helper(self, parent, find_val):
        
        if parent: #if node nor null
            if find_val == parent.value :
                return True
            elif find_val < parent.value:
                self.search_helper(parent.left, find_val)
            elif find_val > parent.value:
                self.search_helper(parent.right, find_val)
        return False
                
    def preorder_print(self, start_node, path = []):
            '''
            inputs: 
                start_node, path
            return: list of nodes passed
            '''
            #base case: start == None, path = path, return
            #base case new: if start not None, append node to path, then append left node, then right node.
            if start_node:
                #main function: append the node to the path
                path.append(start_node.value) 
                #add the left child to the path
                path = self.preorder_print(start_node.left, path)
                #add the right child to the path
                path = self.preorder_print(start_node.right, path)
            return path
    
    
##reference answer
#    def insert_helper(self, current, new_val):
#        if current.value < new_val:
#            if current.right:
#                self.insert_helper(current.right, new_val)
#            else:
#                current.right = Node(new_val)
#        else:
#            if current.left:
#                self.insert_helper(current.left, new_val)
#            else:
#                current.left = Node(new_val)
#
#    def search_helper(self, current, find_val):
#        if current:
#            if current.value == find_val:
#                return True
#            elif current.value < find_val:
#                return self.search_helper(current.right, find_val)
#            else:
#                return self.search_helper(current.left, find_val)
#        return False
#
#    
    
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print(tree.preorder_print(tree.root))

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))