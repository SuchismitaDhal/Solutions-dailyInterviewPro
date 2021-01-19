# APPLE
"""
	SOLVED -- LEETCODE#303
	Create a class that initializes with a list of numbers and has one method called sum. 
	sum should take in two parameters, start_idx and end_idx and return the sum of the list 
	from start_idx (inclusive) to end_idx` (exclusive).
	You should optimize for the sum method.
"""


class ListFastSum:
	def __init__(self, nums):
		self.nums = nums
		self.initsum()

	def sum(self, start_idx, end_idx):
		# For each query; time: O(1)
		return self.partial_sum[end_idx] - self.partial_sum[start_idx]

	def initsum(self):
		self.partial_sum = []
		s = 0
		for x in self.nums:
			self.partial_sum.append(s)
			s += x
		self.partial_sum.append(s)


print(ListFastSum([1, 2, 3, 4, 5, 6, 7]).sum(2, 5))
# 12 because 3 + 4 + 5 = 12
