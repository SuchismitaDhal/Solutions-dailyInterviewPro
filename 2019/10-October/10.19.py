# FACEBOOK
"""
    SOLVED -- LEETCODE#124
    You are given the root of a binary tree.
    Find the path between 2 nodes that maximizes
    the sum of all the nodes in the path, and return the sum.
    The path does not necessarily need to go through the root.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def maxPathSum(root):
    # Time: O(n)    Space: O(h) h: height of the tree
    def maxChildPath(root):
        if not root:
            return 0, 0

        # ms: max subtree   me: max edge
        if root.left != None and root.right == None:
            msl, mel = maxChildPath(root.left)
            return max(msl, mel+root.val, root.val), max(mel+root.val, root.val, 0)
        
        if root.left == None and root.right != None:
            msr, mer = maxChildPath(root.right) 
            return max(msr, mer+root.val, root.val), max(mer+root.val, root.val, 0)
        
        if root.left != None and root.right != None:
            msl, mel = maxChildPath(root.left)
            msr, mer = maxChildPath(root.right)
            return max(msl, msr, mel + mer + root.val, max(mel, mer)+root.val), max(max(mel, mer)+root.val, 0)

        return root.val, max(root.val, 0)

    return maxChildPath(root)[0]


# (* denotes the max path)
#       *10
#       /  \
#     *2   *10
#     / \     \
#   *20  1    -25
#             /  \
#            3    4
root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
print(maxPathSum(root))
# 42
