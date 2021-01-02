#GOOGLE
"""
	SOLVED -- LEETCODE#394
	Given a string with a certain rule: k[string] should be expanded to string k times. 
	So for example, 3[abc] should be expanded to abcabcabc. 
	Nested expansions can happen, so 2[a2[b]c] should be expanded to abbcabbc.
"""
import string
def decompose(s):
	sol = []
	num = 0
	str = ''

	for c in s:
		if c in string.ascii_lowercase:
			if num: 
				sol.append(num)
				num = 0
			str = str + c
		elif c in ['[', ']']:
			if num:
				sol.append(num)
				num = 0
			if str:
				sol.append(str)
				str = ''
			sol.append(c)
		else:
			if str:
				sol.append(str)
				str = ''
			num = num*10 + int(c)

	if num: sol.append(num)
	if str: sol.append(str)
	return sol

def decodeString(s):
  	# Time: O(n) 	Space: O(n)
  	elements = decompose(s)
  	stack = []
  	for ele in elements:
  		if ele == ']':
  			substr = stack[-1]
  			stack.pop()
  			if stack[-1] != '[':
  				substr = stack[-1] + substr
  				stack.pop()
  			stack.pop()
  			k = stack[-1]
  			stack.pop()
  			# print(substr, k)
  			exp = substr * k
  			stack.append(exp)
  			while len(stack) > 1 and stack[-2] != '[':
  				exp = stack[-2] + stack[-1]
  				stack.pop()
  				stack[-1] = exp
  		else:
  			stack.append(ele)
  	return stack[0]

print(decodeString('2[a2[b]c]'))
# abbcabbc
