# MICROSOFT
"""
	SOLVED -- [SIMILAR] LEETCODE#102
	Given the root of a binary tree, print its level-order traversal. For example:
			  1
			 / \
			2   3
			   / \
			  4   5
	The following tree should output 1, 2, 3, 4, 5.
"""
from collections import deque
class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def print_level_order(root):
	# Time : O(n)   Space : O(n)
	# same as breadth-first traversal using queue
	# no need of keeping track of visited node
	# as no node will be visited twice
	Q = deque()
	if root: Q.append(root)

	while Q:
		curr = Q.popleft()
		print(curr.val, end = ' ')
		if curr.left: Q.append(curr.left)
		if curr.right: Q.append(curr.right)

	print('')

root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_level_order(root)
# 1 2 3 4 5
