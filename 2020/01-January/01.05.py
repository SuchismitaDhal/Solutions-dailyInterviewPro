# MICROSOFT
"""
    SOLVED -- LEETCODE#1021
    Given a valid parenthesis string (with only '(' and ')', 
    an open parenthesis will always end with a close parenthesis, 
    and a close parenthesis will never start first), 
    remove the outermost layers of the parenthesis string and 
    return the new parenthesis string.

    If the string has multiple outer layer parenthesis (ie (())()), 
    remove all outer layers and construct the new string. 
    So in the example, the string can be broken down into (()) + (). 
    By removing both components outer layer we are left with () + '' 
    which is simply (), thus the answer for that input would be ().
"""

def remove_outermost_parenthesis(s):
    sol = []
    rank = 0
    for i in range(len(s)):
        if s[i] == '(':
            rank += 1
            if rank != 1: sol.append(s[i])
        else:
            rank -= 1
            if rank != 0: sol.append(s[i])

    return ''.join(sol)


print(remove_outermost_parenthesis('(())()'))
# ()

print(remove_outermost_parenthesis('(()())'))
# ()()

print(remove_outermost_parenthesis('()()()'))
# ' '
