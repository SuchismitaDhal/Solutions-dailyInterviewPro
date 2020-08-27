# LINKEDIN
"""
    SOLVED -- LEETCODE#94
    Given a binary tree, perform an in-order traversal both recursively and iteratively.
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(node):
    # Time: O(n)    Space: O(h) h: height of the tree
    if not node:
        return
    inorder(node.left)
    print(node.val, end=" ")
    inorder(node.right)


def inorder_iterative(node):
    # Time: O(n)    Space: O(h) h: height of the tree
    if not node:
        return " "
    stack = [node]
    lastopr = 1

    while stack:
        if lastopr == 1:
            if stack[-1].left:
                stack.append(stack[-1].left)
            else:
                lastopr = -1
        else:
            temp = stack[-1]
            stack.pop()
            print(temp.val, end=" ")
            if temp.right:
                stack.append(temp.right)
                lastopr = 1
            del temp


#     12
#    /  \
#   6    4
#  / \   / \
# 2   3 7   8
n = Node(12, Node(6, Node(2), Node(3)), Node(4, Node(7), Node(8)))

inorder(n)
# 2 6 3 12 7 4 8
print(" ")
inorder_iterative(n)
# 2 6 3 12 7 4 8
print(" ")
