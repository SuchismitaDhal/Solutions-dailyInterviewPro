# APPLE
"""
    SOLVED 
    Given an integer k and a binary search tree, 
    find the floor (less than or equal to) of k, 
    and the ceiling (larger than or equal to) of k. 
    If either does not exist, then print them as None.
"""


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(root, k, floor=None, ceil=None):
    # Time: O(logn)  Space: O(logn)
    if root.value == k:
        return (k, k)

    if root.value > k:
        if root.left != None:
            return findCeilingFloor(root.left, k, floor, root.value)
        else:
            return (floor, root.value)

    if root.value < k:
        if root.right != None:
            return findCeilingFloor(root.right, k, root.value, ceil)
        else:
            return (root.value, ceil)


root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print(findCeilingFloor(root, 5))
# (4, 6)
