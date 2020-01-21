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
# taking maximum value of n as 30
MAXN = 30


class Solution():
    def fibonacci(self, n):
        # time : O(n), space : O(n)
        if n == 0:
            return 0
        if n == 1:
            return 1
        fib = list()
        fib.append(0)
        fib.append(1)
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]


n = 9
print(Solution().fibonacci(n))
# 34
