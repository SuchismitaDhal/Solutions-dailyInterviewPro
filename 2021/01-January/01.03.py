# FACEBOOK
"""
	SOLVED -- NO SIMILAR PROBLEM FOUND
	Kaprekar's Constant is the number 6174. 
	This number is special because it has the property where 
	for any 4-digit number that has 2 or more unique digits, 
	if you repeatedly apply a certain function it always reaches the number 6174.
	This certain function is as follows:
	- Order the number in ascending form and descending form to create 2 numbers.
	- Pad the descending number with zeros until it is 4 digits in length.
	- Subtract the ascending number from the descending number.
	- Repeat.
	Given a number n, find the number of times the function needs 
	to be applied to reach Kaprekar's constant.
"""
KAPREKAR_CONSTANT = 6174

def isFourDigit(x):
	return x > 999

def makenum(arr):
	sol = 0
	for x in arr:
		sol = sol*10 + x
	return sol

def makearr(n):
	sol = []
	while n:
		sol.append(n%10)
		n //= 10
	return sol[::-1]

def num_kaprekar_iterations(n):
	# Time: O(1) takes at most 7 iteration, by definition
	# Space: O(1)
	if n == KAPREKAR_CONSTANT:
		return 0

	asc = makearr(n)
	asc.sort()
	desc = asc[::-1]
	while len(desc) != 4:
		desc.append(0)

	return 1 + num_kaprekar_iterations(makenum(desc) - makenum(asc))


print(num_kaprekar_iterations(123))
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)