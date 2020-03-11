# AMAZON
"""
    SOLVED -- LEETCODE#114
    Given a binary tree, flatten the binary tree using inorder traversal. 
    Instead of creating a new list, reuse the nodes, where the list is 
    represented by following each right child. 
    As such the root should always be the first element in the list so 
    you do not need to return anything in the implementation, 
    just rearrange the nodes such that following the right child will give us the list.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"


def rightmost(root):
    if root.left == None and root.right == None:
        return root
    if root.left == None:
        return rightmost(root.right)
    if root.right == None:
        root.right = root.left
        root.left = None
        return rightmost(root.right)

    left = rightmost(root.left)
    right = rightmost(root.right)
    left.right = root.right
    root.right = root.left
    root.left = None
    return right


def flatten_bst(root):
    # Time: O(logn)  Space: O(logn)
    rightmost(root)


n5 = Node(5)
n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n5)
n1 = Node(1, n2, n3)

#      1
#    /   \
#   2     3
#  /     /
# 5     4

flatten_bst(n1)
print(n1)

# n1 should now look like
#   1
#    \
#     2
#      \
#       5
#        \
#         3
#          \
#           4
