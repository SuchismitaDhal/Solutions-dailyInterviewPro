# FACEBOOK
"""
	SOLVED -- LEETCODE#41
	[HINT]
		https://leetcode.com/problems/first-missing-positive/discuss/17071/My-short-c%2B%2B-solution-O(1)-space-and-O(n)-time
	You are given an array of integers. 
	Return the smallest positive integer that is not present in the array. 
	The array may contain duplicate entries.
	For example, the input [3, 4, -1, 1] should return 2 
	because it is the smallest positive integer that doesn't exist in the array.
	Your solution should run in linear time and use constant space.
"""

def first_missing_positive(nums):
	# Time: O(n) 	Space: O(1)
	for i in range(len(nums)):
		while nums[i]>0 and nums[i]<=len(nums) and nums[i] != i+1:
			temp = nums[i]
			if temp == nums[temp-1]: break
			nums[i] = nums[temp-1]
			nums[temp-1] = temp

	for i in range(len(nums)):
		if nums[i] != i+1:
			return i+1

	return len(nums)+1

print(first_missing_positive([3, 4, -1, 1]))
# 2
