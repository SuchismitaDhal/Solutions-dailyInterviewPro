# AIRBNB
"""
	SOLVED -- LEETCODE#859
	Given two strings A and B of lowercase letters, return true if and only if we can swap two letters 
	in A so that the result equals B.
	Example 1:
		Input: A = "ab", B = "ba"
		Output: true
	Example 2:
		Input: A = "ab", B = "ab"
		Output: false
	Example 3:
		Input: A = "aa", B = "aa"
		Output: true
	Example 4:
		Input: A = "aaaaaaabc", B = "aaaaaaacb"
		Output: true
	Example 5:
		Input: A = "", B = "aa"
		Output: false
"""

class Solution:
  def buddyStrings(self, A, B):
    # Time: O(n) 	Space: O(n)
    if len(A) != len(B): return False

    changePositions = []
    hasDupl = False
    seenLetters = set()
    for i in range(len(A)):
    	if A[i] != B[i]: changePositions.append(i)
    	if len(changePositions) > 2: return False
    	if A[i] in seenLetters: hasDupl = True
    	seenLetters.add(A[i])

    if len(changePositions) == 0 and hasDupl: return True

    return len(changePositions) == 2 and A[changePositions[0]] == B[changePositions[1]] and A[changePositions[1]] == B[changePositions[0]]

print (Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print (Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False