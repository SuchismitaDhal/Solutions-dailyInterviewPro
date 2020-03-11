# UBER
"""
    SOLVED -- LEETCODE#652
    Given a binary tree, find all duplicate subtrees (subtrees with the same value and same structure) 
    and return them as a list of list [subtree1, subtree2, ...] where subtree1 is a duplicate of subtree2 etc.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left and self.right:
            return f"({self.value}, {self.left}, {self.right})"
        if self.left:
            return f"({self.value}, {self.left})"
        if self.right:
            return f"({self.value}, None, {self.right})"
        return f"({self.value})"


def generatestr(root, hash, sol):
    if root == None:
        return ""

    s = "(" + generatestr(root.left, hash, sol) + "," + \
        str(root.value) + "," + generatestr(root.right, hash, sol) + ")"
    if s not in hash:
        hash[s] = 1
    else:
        if hash[s] == 1:
            sol.append(root)
        hash[s] += 1

    if hash[s] > 1:
        sol.append(root)

    return s


def dup_trees(root):
    #Time : O(n)
    # Space : O(n + logn)   since there are n subtree for n noded tree (rooted at each node)

    hash = dict()
    sol = []
    generatestr(root, hash, sol)

    return sol


n3_1 = Node(3)
n2_1 = Node(2, n3_1)
n3_2 = Node(3)
n2_2 = Node(2, n3_2)
n1 = Node(1, n2_1, n2_2)
# Looks like
#     1
#    / \
#   2   2
#  /   /
# 3   3

print(dup_trees(n1))
# [[(3), (3)], [(2, (3)), (2, (3))]]
# There are two duplicate trees
#
#     2
#    /
#   3
# and just the leaf
#
# 3
