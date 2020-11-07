# MICROSOFT
"""
    SOLVED -- NO SIMILAR PROBLEM FOUND
    A k-ary tree is a tree with k-children, and a tree is symmetrical 
    if the data of the left side of the tree is the same as the right side of the tree.
    Here's an example of a symmetrical k-ary tree.
             4
          /     \
        3        3
      / | \     / | \
    9   4  1  1  4  9
    Given a k-ary tree, figure out if the tree is symmetrical.
"""


class Node():
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def is_pair_symmetric(root1, root2):
    if root1.value != root2.value or len(root1.children) != len(root2.children): 
        return False
    n = len(root1.children)
    for i in range(n):
        if not is_pair_symmetric(root1.children[i], root2.children[n-1-i]):
            return False
    return True

def is_symmetric(root):
    # Time: O(n)    Space: O(h)
    # n: number of nodes in the tree
    # h: height of the tree
    if not root: return False
    l, r = 0, len(root.children) - 1
    while r > l:
        if not is_pair_symmetric(root.children[l], root.children[r]):
            return False
        l += 1
        r -= 1
    if l == r and not is_symmetric(root.children[l]):
        return False
    return True

tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]
print (is_symmetric(tree))
# True
