# GOOGLE
"""
    SOLVED -- VERIFIED[https://www.programcreek.com/2013/02/leetcode-inorder-successor-in-bst-ii-java/]
    Given a node in a binary search tree (may not be the root), 
    find the next largest node in the binary search tree (also known as an inorder successor). 
    The nodes in this binary search tree will also have a parent field to traverse up the tree.
"""


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"(Value: {self.value}, Left: {self.left}, Right: {self.right})"


def inorder_successor(node):
    # Time: O(logn)  Space:O(1)

    # in right subtree
    if node.right != None:
        node = node.right
        while node.left != None:
            node = node.left
        return node.value

    # in parent
    while node.parent != None:
        if node.parent.value > node.value:
            return node.parent.value
        node = node.parent

    # node is the rightmost element
    return None


tree = Node(3)
tree.left = Node(2)
tree.right = Node(4)
tree.left.parent = tree
tree.right.parent = tree
tree.left.left = Node(1)
tree.left.left.parent = tree.left
tree.right.right = Node(5)
tree.right.right.parent = tree.right
#     3
#    / \
#   2   4
#  /     \
# 1       5
print(inorder_successor(tree.left))
# 3
print(inorder_successor(tree.right))
# 5
