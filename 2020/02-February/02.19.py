# AMAZON
"""
    SOLVED -- LEETCODE#129
    A number can be constructed by a path from the root to a leaf. 
    Given a binary tree, sum all the numbers that can be constructed from the root to all leaves.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"


def sum_util(root, pfx):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return pfx * 10 + root.value
    sol = 0
    pfx = pfx*10 + root.value
    sol += sum_util(root.left, pfx)
    sol += sum_util(root.right, pfx)
    return sol


def bst_numbers_sum(root, num=0):
    # Time: O(n)    Space: O(h), his the height of the tree
    return sum_util(root, 0)


sol = 0
n5 = Node(5)
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4, n5)
n1 = Node(1, n2, n3)

#      1
#    /   \
#   2     3
#  / \
# 4   5

print(bst_numbers_sum(n1))
# 262
# Explanation: 124 + 125 + 13 = 262
