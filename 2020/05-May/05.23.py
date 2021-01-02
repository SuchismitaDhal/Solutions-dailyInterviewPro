# MICROSOFT
"""
	SOLVED -- LEETCODE#93
    An IP Address is in the format of A.B.C.D, 
    where A, B, C, D are all integers between 0 to 255.
    Given a string of numbers, return the possible IP addresses 
    you can make with that string by splitting into 4 parts of A, B, C, D.
    Keep in mind that integers can't start with a 0! (Except for 0)
    Example:
    Input: 1592551013
    Output: ['159.255.101.3', '159.255.10.13']
"""

def isValidIP(s, i, j, k):
	parts = list(map(int, [s[:i], s[i:j], s[j:k], s[k:]]))
	
	# print(parts)
	if parts[0] and s[0] == '0': return False 
	if parts[1] and s[i] == '0': return False 
	if parts[2] and s[j] == '0': return False 
	if parts[3] and s[k] == '0': return False

	for p in parts:
		if p > 255: return False

	return True 

def ip_addresses(s, ip_parts=[]):
	if len(s) > 12 or len(s) < 4:
		return []

	sol = []
	for i in range(1, 4):
		for j in range(i + 1, i + 4):
			for k in range(j + 1, j + 4):
				if isValidIP(s, i, j, k):
					ip = [s[:i], s[i:j], s[j:k], s[k:]]
					sol.append('.'.join(ip))

	return sol

print(ip_addresses('1592551013'))
# ['159.255.101.3', '159.255.10.13']
