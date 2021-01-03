# AIRBNB
"""
	SOLVED -- LEETCODE#692
    Given a non-empty list of words, return the k most frequent words. 
    The output should be sorted from highest to lowest frequency, 
    and if two words have the same frequency, 
    the word with lower alphabetical order comes first. 
    Input will contain only lower-case letters.
    Example:
    Input: ["daily", "interview", "pro", "pro", 
    "for", "daily", "pro", "problems"], k = 2
    Output: ["pro", "daily"]
"""
from collections import defaultdict
from heapq import *

class HeapObj(object):
	def __init__(self, val): self.val = val
	def __lt__(self, other): 
		if self.val[0] == other.val[0]:
			return self.val[1] > other.val[1]
		return self.val[0] < other.val[0]
	def __eq__(self, other): return self.val == other.val
	def __str__(self): return str(self.val)

class Solution(object):
    def topKFrequent(self, words, k):
    	# Time: O(nlogk) 	Space: O(n)
        bckt = defaultdict(int)
        for word in words:
            bckt[word] += 1

        minheap = []
        for word in bckt:
            if len(minheap) == k:
            	if HeapObj((bckt[word], word)) > minheap[0] :
                	heapreplace(minheap, HeapObj((bckt[word], word)))
            else:
                heappush(minheap, HeapObj((bckt[word], word)))
            #print([i.val for i in minheap])

        sol = []
        while minheap:
        	sol.append(heappop(minheap).val[1])
        return sol[::-1]


words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
