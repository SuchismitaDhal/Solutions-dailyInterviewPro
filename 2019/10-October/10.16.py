# LINKEDIN
"""
    Given a string, rearrange the string so that no character
    next to each other are the same.
    If no such arrangement is possible, then return None.
    Example:
    Input: abbccc
    Output: cbcbca
"""

def rearrangeString(s):
    freq = collections.defaultdict(int)
    for c in s:
      freq[c] += 1

    orderedfreq = [ (freq[x], c) for x in freq]
    orderedfreq.sort()


print (rearrangeString('abbccc'))
# cbcabc
