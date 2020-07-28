# TWITTER
"""
    SOLVED -- LEETCODE#333
    VALIDATION -> http://buttercola.blogspot.com/2016/02/leetcode-largest-bst-subtree.html
    You are given the root of a binary tree. 
    Find and return the largest subtree of that tree, 
    which is a valid binary search tree.
"""


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def __str__(self):
        # preorder traversal
        answer = str(self.key)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer


def largest_util(root):
        # return 0 root of largest subtree,
        #        1 if the current node is the root of largest subtree,
        #        2 number of nodes in the largest subtree,
        #        3 smallest element in the tree,
        #        4 largest element in the tree

    if root.left == None and root.right == None:
        return (root, True, 1, root.key, root.key)

    elif root.right == None:
        leftsol = largest_util(root.left)
        if leftsol[1] and root.key >= leftsol[4]:
            return (root, True, leftsol[2] + 1, leftsol[3], root.key)
        else:
            return (leftsol[0], False, leftsol[2], leftsol[3], leftsol[4])

    elif root.left == None:
        rightsol = largest_util(root.right)
        if rightsol[1] and root.key < rightsol[3]:
            return (root, True, rightsol[2] + 1, root.key, rightsol[4])
        else:
            return (rightsol[0], False, rightsol[2], rightsol[3], rightsol[4])

    else:
        leftsol = largest_util(root.left)
        rightsol = largest_util(root.right)
        if leftsol[1] and rightsol[1] and root.key >= leftsol[4] and root.key < rightsol[3]:
            return (root, True, leftsol[2] + rightsol[2] + 1, leftsol[3], rightsol[4])
        else:
            if leftsol[2] > rightsol[2]:
                return (leftsol[0], False, leftsol[2], leftsol[3], leftsol[4])
            else:
                return (rightsol[0], False, rightsol[2], rightsol[3], rightsol[4])


def largest_bst_subtree(root):
    # Time: O(n)     Space: O(logn)
    return largest_util(root)[0]


#     5
#    / \
#   6   7
#  /   / \
# 2   4   9
node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
print(largest_bst_subtree(node))
# 749
