# TWITTER
"""
	Given an array containing only positive integers, 
	return if you can pick two integers from the array which cuts the array 
	into three pieces such that the sum of elements in all pieces is equal.
	Example 1:
	Input: array = [2, 4, 5, 3, 3, 9, 2, 2, 2]
	Output: true
	Explanation: choosing the number 5 and 9 results in three pieces 
	[2, 4], [3, 3] and [2, 2, 2]. Sum = 6.

	Example 2:
	Input: array =[1, 1, 1, 1]
	Output: false
"""

class Solution(object):
	def canPick2(self, arr):
		# Time: O(n) 	Space: O(1)
		n = len(arr)
		l, r = 1, n-2
		lsum, rsum = arr[0], arr[n-1]
		msum = 0
		for i in range(l+1, r): msum += arr[i]

		while r>l:
			if lsum == rsum:
				if lsum == msum: return True
				lsum += arr[l]
				rsum += arr[r]
				l += 1
				r -= 1
				msum -= arr[l] + arr[r]
			elif lsum > rsum:
				rsum += arr[r]
				r -= 1
				msum -= arr[r]
			else:
				lsum += arr[l]
				l += 1
				msum -= arr[l]

		return False

print(Solution().canPick2([2, 4, 5, 3, 3, 9, 2, 2, 2]))
# True

print(Solution().canPick2([1, 2, 3, 4, 5]))
# False