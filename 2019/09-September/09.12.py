# MICROSOFT
"""
    SOLVED -- SIMILAR LEETCODE#965
    A unival tree is a tree where all the nodes have the same value. 
    Given a binary tree, return the number of unival subtrees in the tree.
    For example, the following tree should return 5:
      0
     / \
    1   0
       / \
      1   0
     / \
    1   1
    The 5 trees are:
    - The three single '1' leaf nodes. (+3)
    - The single '0' leaf node. (+1)
    - The [1, 1, 1] tree at the bottom. (+1)
"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_val(root, parent):
    # Time: O(n)    n: number of nodes in the tree
    # Space: O(h)   h: height of the tree
    if root == None:
        return (True, 0, True)

    lsol = count_val(root.left, root.val)
    rsol = count_val(root.right, root.val)
    if lsol[0] and rsol[0] and lsol[2] and rsol[2]:
        return (True, lsol[1] + rsol[1] + 1, parent == root.val)
    return (False, lsol[1] + rsol[1], parent == root.val)


def count_unival_subtrees(root):
    return count_val(root, 0)[1]


a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(count_unival_subtrees(a))
# 5
