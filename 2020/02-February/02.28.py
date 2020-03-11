# APPLE
"""
    You are given a tree, and your job is to print it level-by-level with linebreaks.
        a
       / \
      b   c
     / \ / \
    d  e f  g
    The output should be

    a
    bc
    defg
"""

from collections import deque


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        # Fill this in.


tree = Node('a')
tree.left = Node('b')
tree.right = Node('c')
tree.left.left = Node('d')
tree.left.right = Node('e')
tree.right.left = Node('f')
tree.right.right = Node('g')

print(tree)
# a
# bc
# defg
