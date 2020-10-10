# AIRBNB
"""
    SOLVED -- NO SIMILAR PROBLEM FOUND
    Given a phone number, return all valid words 
    that can be created using that phone number.
    For instance, given the phone number 364
    we can construct the words ['dog', 'fog'].
"""

lettersMaps = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}

validWords = ['dog', 'fish', 'cat', 'fog']

# if validWords changes frequently (is not same for many phone),
# the brute force approach is better. For q queries [Time: O(q*n*m) Space: O(1)]
# otherwise,
# we can process all validwords once and create a segment tree
# [Time: O(n*m) Space: O(n*m)] For q queries [Time: O(q*m) Space: O(1)]


def makeWords_brute(phone):
    sol = []
    for w in validWords:
        if len(w) == len(phone):
            i = 0
            while i < len(w):
                if w[i] not in lettersMaps[int(phone[i])]:
                    break
                i += 1
            if i == len(w):
                sol.append(w)
    return sol


print(makeWords_brute('364'))
# ['dog', 'fog']
