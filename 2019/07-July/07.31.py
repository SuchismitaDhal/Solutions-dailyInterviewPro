# UBER
"""
    SOLVED -- LEETCODE#20
    Imagine you are building a compiler. 
    Before running any code, the compiler must check that the parentheses in the program are balanced. 
    Every opening bracket must have a corresponding closing bracket. 
    We can approximate this using strings.

    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.
    An input string is valid if:
    - Open brackets are closed by the same type of brackets.
    - Open brackets are closed in the correct order.
    - Note that an empty string is also considered valid.

    Example:
    Input: "((()))"
    Output: True

    Input: "[()]{}"
    Output: True

    Input: "({[)]"
    Output: False
"""


class Solution:
    def isValid(self, s):
        # Time: O(n)    Space: O(n)
        stack = list()
        for c in s:
            if len(stack) > 0:
                l = stack[len(stack)-1]
                if c == ')' and l == '(':
                    stack.pop()
                    continue
                if c == '}' and l == '{':
                    stack.pop()
                    continue
                if c == ']' and l == '[':
                    stack.pop()
                    continue
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False


s = "()(){(())"
print(Solution().isValid(s))
# False

s = ""
print(Solution().isValid(s))
# True

s = "([{}])()"
print(Solution().isValid(s))
# True
