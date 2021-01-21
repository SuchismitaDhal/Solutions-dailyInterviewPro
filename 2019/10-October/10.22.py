# AMAZON
"""
	SOLVED -- [SIMILAR] LEETCODE#560
    You are given an array of integers, and an integer K.
    Return the subarray which sums to K.
    You can assume that a solution will always exist.
"""
from collections import defaultdict

def find_continuous_k(nums, k):
	# Time: O(n) 	Space: O(n)
	seensum = defaultdict(list)
	seensum[0].append(0)

	currsum = 0
	for i in range(len(nums)):
		currsum  += nums[i]
		if currsum - k in seensum:
			st = seensum[currsum - k][0]
			ed = i + 1
			return nums[st : ed]
		seensum[currsum].append(i + 1)
	return []

print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))
# [2, 5, 7]
