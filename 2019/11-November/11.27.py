# UBER
"""
	SOLVED -- GEEKS FOR GEEKS#Construct a Binary Search Tree from given postorder
    Given a postorder traversal for a binary search tree, reconstruct the tree. 
    A postorder traversal is a traversal order where the left child always comes 
    before the right child, and the right child always comes before the parent for all nodes.
"""
class Node():
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __repr__(self):
		return "(" + str(self.value) + ", " + self.left.__repr__() + ", " + self.right.__repr__() + ")"

def create_tree(postorder):
	# Time: O(n^2) 	Space: O(n)
	# Time complexity can be further optimised by using inorder traversal
	if not postorder: return None
	root = Node(postorder[-1])

	i = 0
	while postorder[i] <= postorder[-1] and i < len(postorder) - 1:
		i += 1
	print(postorder, i)
	root.left = create_tree(postorder[:i])
	root.right = create_tree(postorder[i:-1])

	return root

# 2 is the root node, with 1 as the left child and 3 as the right child
print(create_tree([1, 3, 2]))


