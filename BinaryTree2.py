# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:19:42 2019

@author: Lori
"""
#Binary Tree

class BTNode:
    def __init__(self, val=None, left=None, right= None):
        self.val=val
        self.left=left
        self.right=right
    def grow_left(self, val=None):
        if self.left != None:
            print ("This Node Already has Left Child")
        else:
            self.left = BTNode(val)
    def grow_right(self, val = None):
        if self.right != None:
            print("This Node Already has Right Child")
        else:
            self.right =BTNode(val)
    def print_tree(self):
        print('(', end='')
        if self.left != None:
            self.left.print_tree()
        print(self.val, end='')
        if self.right != None:
            self.right.print_tree()
        print(')', end= '')
    
class BTree:
    def __init__(self):
        self.root=None

                                
                            
                            
                            
                            
                            
                            
my_tree = BTree()

my_tree.root = BTNode("Root")
my_tree.root.grow_left("Left Node")
my_tree.root.grow_right("Right Node")


my_tree.root.print_tree()
