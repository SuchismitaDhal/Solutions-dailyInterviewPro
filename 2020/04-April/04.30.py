# AIRBNB
"""
    Given a non-empty list of words, return the k most frequent words. 
    The output should be sorted from highest to lowest frequency, 
    and if two words have the same frequency, the word with lower alphabetical 
    order comes first. Input will contain only lower-case letters.
    Example:
    Input: ["daily", "interview", "pro", "pro", 
    "for", "daily", "pro", "problems"], k = 2
    Output: ["pro", "daily"]
"""


class Solution(object):
    def topKFrequent(self, words, k):
        occ = dict()
        for word in words:
            if word in occ:
                occ[word] += 1
            else:
                occ[word] = 1


words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
