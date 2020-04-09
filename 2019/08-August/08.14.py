# FACEBOOK
"""
    SOLVED
    Given a sequence of numbers, 
    find the longest sequence that contains only 2 unique numbers.
    Example:
    Input: [1, 3, 5, 3, 1, 3, 1, 5]
    Output: 4
    The longest sequence that contains just 2 unique numbers is [3, 1, 3, 1]
"""


def findSequence(seq):
    # Time: O(n)     Space: O(1)
    if len(seq) < 3:
        return len(seq)

    f, s = 0, 1
    counter = 0
    sol = 0

    for i in range(len(seq)):
        if seq[i] != seq[f] and seq[i] != seq[s]:
            if seq[f] == seq[s]:
                s = i
            else:
                #print(f, "@", counter)
                sol = max(sol, counter)
                f = s
                s = i
                counter = s - f + 1
        else:
            if seq[f] != seq[s]:
                if seq[i] == seq[f]:
                    f = s
                    s = i
                else:
                    s = i
            counter += 1

    #print(f, "@", counter)
    sol = max(sol, counter)

    return sol


print(findSequence([1, 3, 5, 3, 1, 3, 1, 5]))
# 4
