# -*- coding: utf-8 -*-
"""
subtree
"""
class Tree:
    #each node of a tree has data, left, and right.
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def areSame(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    return (root1.data == root2.data and
            areSame(root1.left, root2.left)and
            areSame(root1.right, root2.right)
            )
 
 
def isSubtree(one, two):
 
    if two is None:
        return True
 
    if one is None:
        return False

    if (areSame(one, two)):
        return True
    return isSubtree(one.left, two) or isSubtree(one.right, two)
 
 
""" TREE 1
              10
            /   \
          4     6
           \     
           30      
       
        
    """
 
T = Tree(10)
T.right = Tree(6)
T.left = Tree(4)
T.left.right = Tree(30)
 
""" TREE 2
              26
            /   \
          10     3
        /    \     \
      4      6      3
       \
        30
    """
 
S = Tree(26)
S.right = Tree(3)
S.right.right = Tree(3)
S.left = Tree(10)
S.left.left = Tree(4)
S.left.left.right = Tree(30)
S.left.right = Tree(6)
 
if isSubtree(S,T):
    print("Tree one is subtree of Tree two")
else:
    print("Tree one is not a subtree of Tree two")
 
