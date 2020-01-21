# AMAZON
"""
    SOLVED
    Given a string, return the first recurring letter that appears. 
    If there are no recurring letters, return None.
    Example:
    Input: qwertty
    Output: t

    Input: qwerty
    Output: None
"""


def first_recurring_char(s):
    # Time: O(n)   Space: O(1)
    exist = [False] * 26
    for c in s:
        i = ord(c) - ord('a')
        if exist[i]:
            return c
        exist[i] = True
    return None


print(first_recurring_char('qwertty'))
# t

print(first_recurring_char('qwerty'))
# None
