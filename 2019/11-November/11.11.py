# TWITTER
"""
    SOLVED -- LEETCODE#921
    Given a string with only ( and ), find the minimum number of characters 
    to add or subtract to fix the string such that the brackets are balanced.
    Example:
    Input: '(()()'
    Output: 1
    Explanation:
    The fixed string could either be ()() by deleting the first bracket, 
    or (()()) by adding a bracket. These are not the only ways of fixing the string, 
    there are many other ways by adding it in different positions!
"""


def fix_brackets(s):
    stack = list()
    for c in s:
        if len(stack) > 0:
            l = stack[len(stack) - 1]
            if l == '(' and c == ')':
                stack.pop()
                continue
        stack.append(c)

    return len(stack)


print fix_brackets('(()()')
# 1
