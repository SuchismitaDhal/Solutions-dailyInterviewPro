# FACEBOOK
"""
	SOLVED -- LEETCODE#71
	Given a file path with folder names, '..' (Parent directory), 
	and '.' (Current directory), return the shortest possible file path 
	(Eliminate all the '..' and '.').
	Example
		Input: '/Users/Joma/Documents/../Desktop/./../'
		Output: '/Users/Joma/'
"""

def shortest_path(file_path):
  	# Time: O(n)	Space: O(n)
 	dirs = file_path.split('/')
 	path = []
 	for dir in dirs:
 		if dir == '..':
 			path.pop()
 		elif dir != '.':
 			path.append(dir)

 	return '/'.join(path)

print(shortest_path('/Users/Joma/Documents/../Desktop/./../'))
# /Users/Joma/


