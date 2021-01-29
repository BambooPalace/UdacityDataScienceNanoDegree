#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 10:48:49 2020

@author: clairegong
"""

class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree():
    def __init__(self, root = None):
        self.root = Node(root)
        
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
    
    def preorder_search(self, start_node, find_val):
        if start_node:
            if start_node.value == find_val:
                return True
            else:
                return self.preorder_search(start_node.left, find_val) or\
                        self.preorder_search(start_node.right, find_val)
        return False
    
    def levelOrder(self) -> list:
        # Code here
        
        queue = [self.root]
        path = []
        
        while queue:
            current = queue.pop(0)
            path.append(current.value)
 
            if current.left:
                queue.append(current.left)
                
            if current.right:
                queue.append(current.right)
        return path     
    
    
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print('DFS:preorder traversal')
print(tree.preorder_print(tree.root))
print(tree.preorder_search(tree.root, 6))
print('BFS or level order traversal')
print(tree.levelOrder())
