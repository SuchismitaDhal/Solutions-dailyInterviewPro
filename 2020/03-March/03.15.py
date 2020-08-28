# AMAZON
"""
    SOLVED -- NO SIMILAR PROBLEM
    Given a binary tree, return all values given a certain height h.
"""
from collections import deque


class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def valuesAtHeight(root, height):
    # Time: O(n)    Space: O(n)
    if not root:
        return []
    Q = deque()
    Q.append(root)
    Q.append('.')
    lvl = 1

    while lvl != height:
        curr = Q.popleft()
        if curr == '.':
            lvl += 1
            if not Q:
                print('not enough lvl')
                return []
            Q.append('.')
        else:
            if curr.left:
                Q.append(curr.left)
            if curr.right:
                Q.append(curr.right)

    sol = []
    while 1:
        curr = Q.popleft()
        if curr == '.':
            break
        sol.append(curr.value)

    return sol

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7


a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(valuesAtHeight(a, 3))
# [4, 5, 7]
