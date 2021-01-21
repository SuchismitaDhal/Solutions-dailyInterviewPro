# APPLE
"""
	SOLVED -- LEETCODE#796
	You are given two strings, A and B.
	Return whether A can be shifted some number of times to get B.
	Eg. A = abcde, B = cdeab should return true because A can be shifted 3 times to the right to get B. 
	A = abc and B= acb should return false.
"""

def getpi(patt):
	pi = [0 for _ in patt]

	i, l = 1, 0
	while i < len(patt):
		if patt[i] == patt[l]:
			pi[i] = l + 1
			i += 1
			l += 1
		else:
			if l == 0: i += 1
			else: l = pi[l - 1]

	return pi


def kmp(str, pat, pi):
	i, j = 0, 0
	while i < len(str):
		# print(i, j)
		# print(str[i], pat[j])
		if str[i] == pat[j]:
			i += 1
			j += 1
			if j == len(pi) - 1:
				# print('found@', i)
				return True
		else:
			if j == 0:
				i += 1
			else:
				j = pi[j - 1]
	return False


def is_shifted(a, b):
	# Time: O(n) 	Space: O(n)
	return len(a) == len(b) and kmp(a + a, b, getpi(b))


# print(is_shifted('abcde', 'cdeab'))
# True
print(is_shifted("vcuszhlbtpmksjleuchmjffufrwpiddgyynfujnqblngzoogzg",
				 "fufrwpiddgyynfujnqblngzoogzgvcuszhlbtpmksjleuchmjf"
				 ))
