# UBER
"""
    SOLVED -- LEETCODE#1249
    You are given a string of parenthesis. 
    Return the minimum number of parenthesis that 
    would need to be removed in order to make the string valid. 
    "Valid" means that each open parenthesis has a matching closed parenthesis.
    Example:
    "()())()"
    The following input should return 1.
    ")("
"""


def count_invalid_parenthesis(s):
    stack = list()
    n = len(s)

    for i in range(n):
        if s[i] == '(' or s[i] == ')':
            if len(stack) > 0 and s[i] == ')' and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)

        return len(stack)


print(count_invalid_parenthesis("()())()"))
# 1
