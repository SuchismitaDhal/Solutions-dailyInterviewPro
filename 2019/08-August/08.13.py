# GOOGLE
"""
    SOLVED -- LEETCODE#224
    Given a mathematical expression with just single digits, 
    plus signs, negative signs, and brackets, evaluate the expression. 
    Assume the expression is properly formed.
    Example:
    Input: - ( 3 + ( 2 - 1 ) )
    Output: -4
"""


def convertuni(e):
    sol = []
    i = 0
    while i < len(e):
        if e[i] >= '0' and e[i] <= '9':
            num = 0
            while i < len(e) and e[i] >= '0' and e[i] <= '9':
                num = num * 10 + (ord(e[i]) - ord('0'))
                i += 1
            sol.append(num)
        if i < len(e) and e[i] != ' ':
            sol.append(e[i])
        i += 1
    print(sol)
    return sol


def assignsign(e):
    sol = []
    neg = False
    stack = list()

    for i in range(len(e)):
        if isinstance(e[i], int):
            if i - 1 >= 0 and e[i - 1] == '-':
                val = e[i] if neg else - e[i]
            else:
                val = -e[i] if neg else e[i]
            sol.append(val)
        if e[i] == '(':
            if i - 1 >= 0 and e[i - 1] == '-':
                stack.append('-')
                neg = neg ^ True
            else:
                stack.append('+')
        if e[i] == ')':
            if stack[-1] == '-':
                neg = neg ^ True
            stack.pop()
    return sol


def eval(expression):
    # Time: O(n)     Space: O(n)
    exp = convertuni(expression)
    exp = assignsign(exp)
    return sum(exp)


#print(eval('- (3 + ( 2 - 1 ) )'))
# -4
print(eval(" 2-1 + 2 "))
