# APPLE
"""
	SOLVED -- LEETCODE#236
    You are given the root of a binary tree, along with two nodes, A and B. 
    Find and return the lowest common ancestor of A and B. 
    For this problem, you can assume that each node also has a pointer to its parent, 
    along with its left and right child.
"""

class TreeNode:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.parent = None
		self.val = val

def findlinage(root, a, b):
	if not root: return (0, None)

	ncurr = 0
	if root == a or root == b:
		ncurr = 1

	nleft, ancestorleft = findlinage(root.left, a, b)
	if nleft == 2: return (2, ancestorleft)
	if nleft == 1 and ncurr == 1: return(2, root)

	nright, ancestorright = findlinage(root.right, a, b)
	if nright == 2: return (2, ancestorright)
	if nright == 1 and ncurr == 1: return(2, root)

	if nleft == 1 and nright == 1: return (2, root)
	return (ncurr + nleft + nright, None)

def lowestCommonAncestor(root, a, b):
	# Time: O(n) 	Space: O(h)
	return findlinage(root, a, b)[1]

#   a
#  / \
# b   c
#    / \
#   d*  e*
root = TreeNode('a')
root.left = TreeNode('b')
root.left.parent = root
root.right = TreeNode('c')
root.right.parent = root
a = root.right.left = TreeNode('d')
root.right.left.parent = root.right
b = root.right.right = TreeNode('e')
root.right.right.parent = root.right

print(lowestCommonAncestor(root, a, b).val)
# c
