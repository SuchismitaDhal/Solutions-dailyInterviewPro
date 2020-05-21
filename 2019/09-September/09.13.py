# MICROSOFT
"""
    SOLVED -- LEETCODE#105
    You are given the preorder and inorder traversals of a binary tree in the form of arrays.
    Write a function that reconstructs the tree represented by these traversals.

    Example:
    Preorder: [a, b, d, e, c, f, g]
    Inorder: [d, b, e, a, f, c, g]

    The tree that should be constructed from these traversals is:

        a
       / \
      b   c
     / \ / \
    d  e f  g
"""

from collections import deque


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            n = q.popleft()
            result += n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return result


def reconstruct(preorder, inorder):
    # Time: O(nlogn)     Space: O(logn)      Average cases
    # Time: O(n^2)       Space: O(n)         Worst case: edge tree
    if len(preorder) == 0:
        return None
    root = Node(preorder[0])
    idx = inorder.index(preorder[0])
    root.left = reconstruct(preorder[1:idx+1], inorder[:idx])
    root.right = reconstruct(preorder[idx+1:], inorder[idx+1:])
    return root


tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                   ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
print(tree)
# abcdefg
