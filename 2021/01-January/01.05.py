# AMAZON
"""
	SOLVED -- NO SIMILAR PROBLEM FOUND 
	Given a binary tree and a given node value, return all of the node's cousins. 
	Two nodes are considered cousins if they are on the same level of the tree with 
	different parents. You can assume that all nodes will have their own unique value.
"""

class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def getNodeLevel(root, curr, val):
	if not root: return 0
	if root.value == val:
		return curr
	return getNodeLevel(root.left, curr + 1, val) + getNodeLevel(root.right, curr + 1, val)

def getCousins(root, lvl, val):
	cousins = []
	if not root: return []

	#print(root.value, '->', lvl)
	if lvl == 2:
		if (root.left and root.left.value == val) or (root.right and root.right.value == val):
			return []
		else:
			if root.left: cousins.append(root.left.value)
			if root.right: cousins.append(root.right.value)
			return cousins

	cousins.extend(getCousins(root.left, lvl - 1, val))
	cousins.extend(getCousins(root.right, lvl - 1, val))
	return cousins

class Solution(object):
	def list_cousins(self, tree, val):
		lvl = getNodeLevel(tree, 1, val)
		if lvl == 1: return []
		return getCousins(tree, lvl, val)

#     1
#    / \
#   2   3
#  / \   \
# 4   6   5
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

print(Solution().list_cousins(root, 5))
# [4, 6]