# GOOGLE
"""
    SOLVED
    Given a string, determine if you can remove any character to create a palindrome.
"""


def create_palindrome(s):
    # Time: O(n)   Space: O(1)
    n = len(s)
    l = 0
    r = n - 1
    flag = False
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            if flag:
                return False
            else:
                if s[l] == s[r - 1]:
                    flag = True
                    r -= 1
                elif s[r] == s[l + 1]:
                    flag = True
                    l += 1
                else:
                    return False

    return flag


print(create_palindrome("abcdcbea"))
# True
print(create_palindrome("abccba"))
# False
print(create_palindrome("abccaa"))
# False
