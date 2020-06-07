# LINKEDIN
"""
    SOLVED -- LEETCODE#111
    Given a binary tree, find the minimum depth of the binary tree. 
    The minimum depth is the shortest distance from the root to a leaf.
"""
from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def min_depth_bst(root):
    if root == None:
        return 0
    Q = deque()
    Q.append((root, 1))

    while len(Q):
        node, lvl = Q.popleft()
        if node.left == None and node.right == None:
            return lvl
        if node.left != None:
            Q.append((node.left, lvl + 1))
        if node.right != None:
            Q.append((node.right, lvl + 1))


n3 = Node(3, None, Node(4))
n2 = Node(2)
n1 = Node(1, n2, n3)

#     1
#    / \
#   2   3
#        \
#         4
print(min_depth_bst(n1))
# 2
