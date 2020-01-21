# APPLE
"""
    SOLVED -- LEETCODE#151
    Given a list of words in a string, reverse the words in-place 
    (ie don't create a new string and reverse the words). 
    Since python strings are not mutable, you can assume the input will be a mutable sequence (like list).
"""


def reverse_words(words):
    # Time: O(n)    Space: O(n)
    words.reverse()
    s = 0
    e = 0
    for word in words:
        if word == ' ':
            words[s:e] = reversed(words[s:e])
            s = e+1
        e += 1
    words[s:e] = reversed(words[s:e])


s = list("can you read this")
reverse_words(s)
print(''.join(s))
# this read you can
