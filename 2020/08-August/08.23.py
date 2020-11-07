#TWITTER
"""
	SOLVED -- LEETCODE#215
	Find the k-th largest number in a sequence of unsorted numbers.
	Can you do this in linear time?
"""
import heapq

def findKthLargest(arr, k):
	# Time: O(nlogk) 	Space: O(k)
	maxq = []
	for i in range(min(k, len(arr))):
		heapq.heappush(maxq, arr[i])

	for i in range(k, len(arr)):
		if arr[i] > maxq[0]:
			heapq.heappushpop(maxq, arr[i])

	return maxq[0]
  
print(findKthLargest([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 3))
# 7

