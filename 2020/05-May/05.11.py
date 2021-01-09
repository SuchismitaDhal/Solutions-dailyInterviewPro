# GOOGLE
"""
	SOLVED -- LEETCODE#205
    Given two strings, find if there is a one-to-one mapping 
    of characters between the two strings.
    Example
        Input: abc, def
        Output: True # a -> d, b -> e, c -> f

        Input: aab, def
        Ouput: False # a can't map to d and e 
"""

def has_character_map(str1, str2):
	if len(str1) != len(str2): return False
	forward = dict()
	backward = dict()

	for i in range(len(str1)):
		if str1[i] in forward:
			if forward[str1[i]] != str2[i]:
				return False
			if backward[str2[i]] != str1[i]:
				return False
		else:
			if str2[i] in backward:
				return False
			forward[str1[i]] = str2[i]
			backward[str2[i]] = str1[i]

	return True

print(has_character_map('abc', 'def'))
# True
print(has_character_map('aac', 'def'))
# False
