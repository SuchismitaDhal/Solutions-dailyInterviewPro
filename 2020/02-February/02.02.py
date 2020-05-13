# APPLE
"""
    SOLVED -- LEETCODE#22
    Given a number n, generate all possible combinations of n well-formed brackets.
"""


def gen_h(n, h, l):
    sol = []
    # nothing to add
    if h == 0 and l == n:
        return [""]

    # add left bracket
    if l < n:
        sfx = gen_h(n, h + 1, l + 1)
        for s in sfx:
            sol.append('(' + s)

    # add right bracket
    if h - 1 >= 0:
        sfx = gen_h(n, h - 1, l)
        for s in sfx:
            sol.append(')' + s)

    return sol


def generate_brackets(n):
    # Time: O(2^n), number of possible strings
    # Space: O(n), depth of recursion tree
    return gen_h(n, 0, 0)


print(generate_brackets(1))
# ['()']

print(generate_brackets(3))
# ['((()))', '(()())', '()(())', '()()()', '(())()']
