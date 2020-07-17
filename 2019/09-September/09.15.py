# APPLE
"""
    SOLVED -- LEETCODE#953
    Given a list of words, and an arbitrary alphabetical order, 
    verify that the words are in order of the alphabetical order.
    Example:
        Input:
        words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"
        Output: False
        Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'
    Example 2:
        Input:
        words = ["zyx", "zyxw", "zyxwy"],
        order="zyxwvutsrqponmlkjihgfedcba"
        Output: True
        Explanation: The words are in increasing alphabetical order
"""


def id(c):
    return ord(c) - ord('a')


def comp(first, second, rank):
    for i in range(min(len(first), len(second))):
        if first[i] != second[i]:
            if rank[id(first[i])] > rank[id(second[i])]:
                return False
            else:
                return True
    return len(first) <= len(second)


def isSorted(words, order):
    # Time: O(n*m)  n: size of words; m: size of each word
    # Space: O(1)
    rank = [0] * 26
    for i in range(len(order)):
        h = id(order[i])
        rank[h] = i

    for i in range(len(words) - 1):
        if not comp(words[i], words[i + 1], rank):
            return False
    return True


print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(isSorted(["zyx", "zyxw", "zyxwy"],
               "zyxwvutsrqponmlkjihgfedcba"))
# True
