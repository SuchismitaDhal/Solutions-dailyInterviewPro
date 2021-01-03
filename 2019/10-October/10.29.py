# LINKEDIN
"""
	SOLVED -- LEETCODE#66
    Given a non-empty array where each element represents a digit of a non-negative integer, add one to the integer. 
    The most significant digit is at the front of the array and each element in the array contains only one digit. 
    Furthermore, the integer does not have leading zeros, except in the case of the number '0'.
    Example:
    Input: [2,3,4]
    Output: [2,3,5]
"""

class Solution():
    def plusOne(self, digits):
    	# Time: O(n) 	Space: O(1)
    	digits.reverse()
    	carry = 1
    	for i in range(len(digits)):
    		x = digits[i] + carry
    		digits[i] = x % 10
    		carry = x // 10
    		if not carry: break

    	if carry: digits.append(carry)
    	return digits[::-1]

num = [2, 9, 9]
print(Solution().plusOne(num))
# [3, 0, 0]
