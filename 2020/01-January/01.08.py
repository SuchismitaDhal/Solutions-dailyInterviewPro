# TWITTER
"""
    SOLVED -- NO SIMILAR QUESTION FOUND
    Given a binary search tree (BST) and a value s, 
    split the BST into 2 trees, where one tree has all values less than or equal to s, 
    and the other tree has all values greater than s 
    while maintaining the tree structure of the original BST. 
    You can assume that s will be one of the node's value in the BST. 
    Return both tree's root node as a tuple.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"
        """
        if self.left and self.right:
            return f"({self.value}, {self.left}, {self.right})"
        if self.left:
            return f"({self.value}, {self.left})"
        if self.right:
            return f"({self.value}, None, {self.right})"
        return f"({self.value})"
        """


def split_bst(bst, s):
    # Time: O(logn)  Space: O(logn) //for recursion stack
    if bst.value == s:
        ltree = bst
        rtree = bst.right
        ltree.right = None

    if bst.value > s:
        l, r = split_bst(bst.left, s)
        ltree = l
        rtree = bst
        rtree.left = r

    if bst.value < s:
        l, r = split_bst(bst.right, s)
        rtree = r
        ltree = bst
        ltree.right = l

    return(ltree, rtree)


n2 = Node(2)
n1 = Node(1, None, n2)

n5 = Node(5)
n4 = Node(4, None, n5)

root = Node(3, n1, n4)
"""
n1 = Node(2, Node(1), Node(3))
n2 = Node(6, Node(5), Node(7))
root = Node(4, n1, n2)
"""
# (3, (1, (2)), (4, None, (5)))
# How the tree looks like
#     3
#   /   \
#  1     4
#   \     \
#    2     5

l, r = split_bst(root, 2)
print(l, "%", r)

#print(split_bst(root, 2))
# ((1, (2)), (3, None, (4, None, (5))))
# Split into two trees
# 1    And   3
#  \          \
#   2          4
#               \
#                5
