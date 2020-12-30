# AIRBNB
"""
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

class MaxHeapObj(object):
  def __init__(self, val): self.val = val
  def __lt__(self, other): return self.val > other.val
  def __eq__(self, other): return self.val == other.val
  def __str__(self): return str(self.val)

class Solution(object):
    def topKFrequent(self, words, k):
        bckt = defaultdict(int)

        for word in words:
            bckt[word] += 1

        minheap = []
        for word in bckt:
            if len(minheap) == k:
                # replace the lowest occurance 
                # if the occurance is same, replace if smaller string
                if bckt[word] > 
                heapreplace(minheap, (bckt[word], word))
            else:
                # in the last pop max
                heappush(minheap, (bckt[word], word))
        
        return bckt


words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
