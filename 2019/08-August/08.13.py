# GOOGLE
"""
    Given a mathematical expression with just single digits, 
    plus signs, negative signs, and brackets, evaluate the expression. 
    Assume the expression is properly formed.
    Example:
    Input: - ( 3 + ( 2 - 1 ) )
    Output: -4
"""


def solve(exp):
    if len(exp) <= 2:
        return exp

    # no negative integers
    if len(exp) == 3:
        if exp[1] == '+':
            return int(exp[0]) + int(exp[2])
        else:
            return int(exp[0]) - int(exp[2])

    # one negetive integer
    if len(exp) == 4:
        if exp[0] == '-':
            if exp[2] == '+':
                return - (int(exp[0]) - int(exp[2]))
            else:
                return - (int(exp[0]) + int(exp[2]))
        else:
            if exp[1] == '+':
                return int(exp[0]) - int(exp[2])
            else:
                return int(exp[0]) + int(exp[2])

    # two negetive integers
    if len(exp) == 5:
        if exp[2] == '+':
            return -(int(exp[0]) + int(exp[2]))
        else:
            return -(int(exp[0]) - int(exp[2]))


def eval(expression):
    # Time: O(n)    Space: O(n)
    stack = list()
    e = list()

    for i in range(len(expression)):
        c = expression[i]
        if c != ' ':
            if c == ')':
                p = stack.pop()
                while p != '(':
                    e.append(p)
                    p = stack.pop()

                stack.append(str(solve(e[::-1])))
                e.clear()
            else:
                stack.append(c)

    sol = ""
    for c in stack:
        sol += c
    return sol


print(eval('- (3 + ( 2 - 1 ) )'))
# -4
