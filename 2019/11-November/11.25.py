# TWITTER
"""
    SOLVED -- LEETCODE#110
    Given a tree, find if the binary tree is height balanced or not. 
    A height balanced binary tree is a tree where every node's 2 subtree 
    do not differ in height by more than 1.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def get_balanced_height(root):
    if not root: return 0
    lh = get_balanced_height(root.left)
    rh = get_balanced_height(root.right)

    if lh < 0 or rh < 0: return -1
    if abs(lh - rh) > 1: return -1

    return max(lh, rh) + 1

def is_height_balanced(tree):
    # Time: O(n)    Space: O(h)
    return get_balanced_height(tree) >= 0

#     1
#    / \
#   2   3
#  /
# 4
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4)
n1 = Node(1, n2, n3)

print(is_height_balanced(n1))
# True

#     1
#    /
#   2
#  /
# 4
n1 = Node(1, n2)
print(is_height_balanced(n1))
# False
