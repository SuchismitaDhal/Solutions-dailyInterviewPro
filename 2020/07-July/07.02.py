# AMAZON
"""
    Given a number like 159, 
    add the digits repeatedly until you get a single number.
    For instance, 1 + 5 + 9 = 15.
    1 + 5 = 6.
    So the answer is 6.
"""


class Solution(object):
    def addDigits(self, n):
        if n < 10:
            return n
        sol = 0
        while n:
            sol += n % 10
            n = n // 10
        return self.addDigits(sol)


print(Solution().addDigits(159))
# 1 + 5 + 9 = 15
# 1 + 5 = 6
# 6
