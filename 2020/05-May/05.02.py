# GOOGLE
"""
	SOLVED -- [SIMILAR] TECHIE DELIGHT - Find maximum sum root to leaf path in a binary tree
	Given a binary tree, find and return the largest path from root to leaf.
"""
class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def largest_path_sum_util(root):
	if not root: return ([], 0)
	leftpath, leftsum = largest_path_sum_util(root.left)
	rightpath, rightsum = largest_path_sum_util(root.right)

	if leftsum > rightsum:
		leftpath.append(root.value)
		return (leftpath, leftsum + root.value)
				
	rightpath.append(root.value)				
	return (rightpath, rightsum + root.value)

def largest_path_sum(tree):
	# Time: O(n) 	Space: O(h)
	revpath = largest_path_sum_util(tree)[0]
	return revpath[::-1]

tree = Node(1)
tree.left = Node(3)
tree.right = Node(2)
tree.right.left = Node(4)
tree.left.right = Node(5)
#    1
#  /   \
# 3     2
#  \   /
#   5 4
print(largest_path_sum(tree))
# [1, 3, 5]
