# GOOGLE
"""
    SOLVED -- LEETCODE#104
    You are given the root of a binary tree. 
    Return the deepest node (the furthest node from the root).
    Example:
        a
       / \
      b   c
     /
    d
    The deepest node in this tree is d at depth 3.
"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val


def deepest(node):
    # Time: O(n)    Space: O(h) (h : height of the tree)
    if not node:
        return (None, 0)

    leftSol = deepest(node.left)
    rightSol = deepest(node.right)

    if leftSol[1] >= rightSol[1]:
        if leftSol[1] == 0:
            return (node.val, 1)
        return (leftSol[0], leftSol[1] + 1)
    else:
        return (rightSol[0], rightSol[1] + 1)


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))
# (d, 3)
