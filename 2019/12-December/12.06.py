# MICROSOFT
"""
	SOLVED -- NO SIMILAR PROBLEM FOUND
	Given a string, determine if there is a way to arrange the string 
	such that the string is a palindrome. If such arrangement exists, 
	return a palindrome (There could be many arrangements). 
	Otherwise return None.
"""
from collections import defaultdict

def find_palindrome(s):
	# Time: O(n) 	Space: O(1)
	freq = defaultdict(int)
	for x in s: freq[x] += 1
	odds = sum([1 for x in freq if freq[x] % 2])

	if len(s) % 2 != odds: return None 
	sol = [' ' for x in s]

	i = 0
	for x in freq:
		while freq[x] > 1:
			sol[i] = sol[len(s) - i - 1] = x
			freq[x] -= 2
			i += 1
		if freq[x] == 1:
			sol[len(s)//2] = x
			freq[x] = 0

	return ''.join(sol)

print(find_palindrome('momom'))
# momom
