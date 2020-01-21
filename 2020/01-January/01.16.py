# AMAZON
"""
    SOLVED -- LEETCODE#204
    Given a positive integer n, find all primes less than n.
"""


def find_primes(n):
    # Time: O(n^2) Space: O(n)
    isPrime = [1 for i in range(n)]
    sol = []

    for i in range(2, n):
        if isPrime[i] == 1:
            sol.append(i)

            k = i * i
            while k < n:
                isPrime[k] = 0
                k += i

    return sol


print(find_primes(14))
# [2, 3, 5, 7, 11, 13]
