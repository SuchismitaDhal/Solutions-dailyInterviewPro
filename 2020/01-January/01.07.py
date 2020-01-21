# APPLE
"""
    SOLVED
    Given a non-negative integer n, convert n to base 2 in string form. 
    Do not use any built in base 2 conversion functions like bin.
"""
def base_2(n):
    #Time: O(logn)    Space: O(logn)
    bin = list()

    while n:
        bin.append(n % 2)
        n = n // 2
    
    bin.reverse()
    return bin

print(base_2(123))
# 1111011
# In the above example, 2^6 + 2^5 + 2^4 + 2^3 + 2^1 + 2^0 = 123