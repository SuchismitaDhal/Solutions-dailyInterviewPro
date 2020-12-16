# MICROSOFT
"""
    SOLVED -- GFG Longest Consecutive 1's 
    Return the longest run of 1s for a given integer n's binary representation.
    Example:
        Input: 242
        Output: 4
        242 in binary is 0b11110010, so the longest run of 1 is 4.
"""
def longest_run(n):
    # Time: O(logn)     Space: O(1)
    run = curr = 0
    while n:
        if not n % 2:
            run = max(run, curr)
            curr = 0
        else:
            curr += 1
        n = n // 2

    return max(run, curr)


print(longest_run(242))
# 4