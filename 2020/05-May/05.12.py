# FACEBOOK
"""
    SOLVED -- LEETCODE#150
    Given an expression (as a list) in reverse polish notation, evaluate the expression. 
    Reverse polish notation is where the numbers come before the operand. 
    Note that there can be the 4 operands '+', '-', '*', '/'. 
    You can also assume the expression will be well formed.
    Example
    Input: [1, 2, 3, '+', 2, '*', '-']
    Output: -9
    The equivalent expression of the above reverse polish notation would be (1 - ((2 + 3) * 2)).
"""
import math

comp = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}


def reverse_polish_notation(expr):
    # Time: O(n)     Space: O(n)
    # assuming no divide by 0
    stack = list()
    for c in expr:
        if type(c) == str:
            b = stack.pop()
            a = stack.pop()
            c = comp[c](a, b)
        stack.append(c)

    return stack[0]


# 1 - (2 + 3) * 2
print(reverse_polish_notation([1, 2, 3, '+', 2, '*', '-']))
# -9
