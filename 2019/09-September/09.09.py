# FACEBOOK
"""
    SOLVED -- LEETCODE#98
    You are given the root of a binary search tree.
    Return true if it is a valid binary search tree, and false otherwise.
    Recall that a binary search tree has the property that all values in the left subtree are less
    than or equal to the root, and all values in the right subtree are greater than or equal to the root.
"""
import collections


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def is_bst(root):
    # Since, inorder traversal of bst is ordered
    # Time:  O(n)   Space: O(n)
    stack = list()
    order = list()

    if root == None:
        return True

    stack.append(root)
    while len(stack):
        n = stack[len(stack)-1]
        if n.left == None:
            if len(order) > 0 and n.key <= order[-1]:
                return False
            order.append(n.key)
            stack.pop()
            if n.right != None:
                stack.append(n.right)
        else:
            stack.append(n.left)
            n.left = None

    return True


a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print(is_bst(a))

#    5
#   / \
#  3   7
# / \ /
# 1  4 6
