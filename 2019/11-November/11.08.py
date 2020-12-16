# APPLE
"""
    SOLVED -- LEETCODE#168
    In many spreadsheet applications, the columns are marked with letters. 
    From the 1st to the 26th column the letters are A to Z. 
    Then starting from the 27th column it uses AA, AB, ..., ZZ, AAA, etc.
    Given a number n, find the n-th column name.
"""
import string

chars = string.ascii_uppercase
def column_name(n):
    # Time: O(logn)     
    # Space: O(logn) can be optimesed to O(1) if string is mutable
    sol = []
    
    while n:
        n -= 1
        r = n % 26
        sol.append(chars[r])
        n = n // 26

    return ''.join(sol[::-1])

print(column_name(26))
print(column_name(27))
print(column_name(28))
# Z
# AA
# AB