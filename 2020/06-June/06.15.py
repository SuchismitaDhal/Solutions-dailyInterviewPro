# GOOGLE
"""
    SOLVED -- NO SIMILAR QUESTION
    Given a binary tree, remove the nodes in which there is only 1 child, 
    so that the binary tree is a full binary tree.
    So leaf nodes with no children should be kept, and nodes with 2 children should be kept as well.
"""
from collections import deque


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            num = len(q)
            while num > 0:
                n = q.popleft()
                result += str(n.value)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                num = num - 1
            if len(q):
                result += "\n"

        return result


def fullBinUtil(root):
    if root.left == None and root.right == None:
        return root
    if root.left != None and root.right != None:
        root.left = fullBinUtil(root.left)
        root.right = fullBinUtil(root.right)
        return root
    return root.left if root.left else root.right


def fullBinaryTree(node):
    # Time: O(n)     Space: O(logn)
    if node == None:
        return None
    return fullBinUtil(node)

    # Given this tree:
    #     1
    #    / \
    #   2   3
    #  /   / \
    # 0   9   4

    # We want a tree like:
    #     1
    #    / \
    #   0   3
    #      / \
    #     9   4


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.right.right = Node(4)
tree.right.left = Node(9)
tree.left.left = Node(0)
print(fullBinaryTree(tree))
# 1
# 03
# 94
