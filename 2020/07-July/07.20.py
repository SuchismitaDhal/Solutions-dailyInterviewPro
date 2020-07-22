# UBER
"""
    SOLVED -- LEETCODE#322
    Given a list of possible coins in cents, and an amount (in cents) n, 
    return the minimum number of coins needed to create the amount n. 
    If it is not possible to create the amount using the given coin denomination, return None.
"""


def make_change(coins, n):
    # Time: O(n*m)   Space: O(n)
    dp = [n+1] * (n+1)
    dp[0] = 0

    for i in range(1, n + 1):
        for c in coins:
            if c <= i:
                dp[i] = min(dp[i], 1 + dp[i - c])

    if dp[n] == n + 1:
        return None
    else:
        return dp[n]


print(make_change([1, 5, 10, 25], 36))
# 3 coins (25 + 10 + 1)
