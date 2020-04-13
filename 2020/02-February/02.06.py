# LINKEDIN
"""
    Given a binary tree, find the minimum depth of the binary tree. 
    The minimum depth is the shortest distance from the root to a leaf.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def min_depth_bst(root):


n3 = Node(3, None, Node(4))
n2 = Node(2, Node(3))
n1 = Node(1, n2, n3)

#     1
#    / \
#   2   3
#        \
#         4
print(min_depth_bst(n1))
# 2
