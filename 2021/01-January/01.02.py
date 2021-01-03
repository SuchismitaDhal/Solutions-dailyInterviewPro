# GOOGLE
"""
	SOLVED -- LEETCODE#108
	Given a sorted list, create a height balanced binary search tree, 
	meaning the height differences of each node can only differ by at most 1.
"""

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self):
		answer = str(self.value)
		if self.left:
			answer += str(self.left)
		if self.right:
			answer += str(self.right)
		return answer

def create_height_balanced_bst(nums):
  	# Time: O(n) 	Space: O(n)
  	if len(nums) == 0: return None
  	if len(nums) == 1: return Node(nums[0])

  	m = len(nums) // 2
  	root = Node(nums[m])
  	root.left = create_height_balanced_bst(nums[:m])
  	root.right = create_height_balanced_bst(nums[m+1:])
  	return root

tree = create_height_balanced_bst([1, 2, 3, 4, 5, 6, 7, 8])
# 53214768
#  (pre-order traversal)
#       5
#      / \
#     3    7
#    / \  / \
#   2   4 6  8
#  /
# 1