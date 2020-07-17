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


class Solution(object):
    def comp(self, x):
        return x

    def add(self):
        return

    def topKFrequent(self, words, k):
        bckt = dict()

        for word in words:
            if word not in bckt:
                bckt[word] = 1
            else:
                bckt[word] += 1

        print("hash made ")
        print(bckt)
        bckt = sorted(bckt, key=self.comp)
        # bckt = sorted(bckt, key=lambda x: bckt[x])
        return bckt


words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
