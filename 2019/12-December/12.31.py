# FACEBOOK
"""
    SOLVED -- LEETCODE#279
    Given a number n, find the least number of squares needed to sum up to the number.
"""


def init(n):
    sol = [0 for _ in range(n + 1)]
    i = 0
    while i * i <= n:
        sol[i * i] = 1
        i += 1
    return sol


def square_sum(n):
    # Time: O(n^2)   Space: O(n)
    minsum = init(n)
    for i in range(2, n + 1):
        if not minsum[i]:
            minsum[i] = n + 1
            for j in range(1, i // 2 + 1):
                minsum[i] = min(minsum[i], minsum[j] + minsum[i - j])
    return minsum[n]


print(square_sum(13))
# Min sum is 3^2 + 2^2
# 2
