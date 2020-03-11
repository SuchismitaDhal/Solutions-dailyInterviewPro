# APPLE
"""
    SOLVED -- LEETCODE#1047
    Given a string, we want to remove 2 adjacent characters that are the same, 
    and repeat the process with the new string until we can no longer perform the operation.
"""


def remove_adjacent_dup(s):
    # Time: O(n)     Space: O(n)
    stack = list()

    for c in s:
        if len(stack) == 0:
            stack.append(c)
        else:
            if c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

    return "".join(stack)


print(remove_adjacent_dup("cabba"))
# Start with cabba
# After remove bb: caa
# After remove aa: c
# print c
