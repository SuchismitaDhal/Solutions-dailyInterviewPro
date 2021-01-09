# AMAZON
"""
    SOLVED -- LEETCODE#95
    Given a number n, generate all binary search trees 
    that can be constructed with nodes 1 to n.
"""


class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self):
		result = str(self.value)
		if self.left:
			result = result + str(self.left)
		if self.right:
			result = result + str(self.right)
		return result

def generate_subtree(dx, l, trees):
	sol = []
	for tree in trees[l]:
		sol.append(clone_tree(dx, tree))
	return sol

def clone_tree(dx, root):
	if not root:
		return None
	dupl = Node(dx + root.value)
	dupl.left = clone_tree(dx, root.left)
	dupl.right = clone_tree(dx, root.right)
	return dupl

def generate_bst(n):
	trees = [[None]]
	for l in range(1, n + 1):
		lentrees = []
		for r in range(1, l + 1):
			lsubtree = trees[r-1]
			rsubtree = generate_subtree(r, l - r, trees)
			# print('@', l, r, lsubtree, rsubtree)
			for lst in lsubtree:
				for rst in rsubtree:
					root = Node(r, lst, rst)
					lentrees.append(root)
		trees.append(lentrees)

	return trees[-1]

for tree in generate_bst(3):
	print(tree)

# Pre-order traversals of binary trees from 1 to n.
# 123
# 132
# 213
# 312
# 321

#   1      1      2      3      3
#    \      \    / \    /      /
#     2      3  1   3  1      2
#      \    /           \    /
#       3  2             2  1
