# APPLE
"""
    The Fibonacci sequence is the integer sequence 
    defined by the recurrence relation: F(n) = F(n-1) + F(n-2), 
    where F(0) = 0 and F(1) = 1. In other words, 
    the nth Fibonacci number is the sum of the prior two Fibonacci numbers. 
    Below are the first few values of the sequence:

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

    Given a number n, print the n-th Fibonacci Number.
"""

class Solution():
    def fibonacci(self, n):
        # time : O(n), space : O(1)
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        fibb1, fibb2 = 0, 1
        for i in range(2, n + 1):
            next = fibb1 + fibb2
            fibb1 = fibb2
            fibb2 = next
        return fibb2


n = 9
print(Solution().fibonacci(n))
# 34
