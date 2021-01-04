# AMAZON
"""
	SOLVED -- LEETCODE#54
	You are given a 2D array of integers. Print out the clockwise spiral traversal 
	of the matrix.
	Example:
		grid = [[1,  2,  3,  4,  5],
		        [6,  7,  8,  9,  10],
		        [11, 12, 13, 14, 15],
		        [16, 17, 18, 19, 20]]
		The clockwise spiral traversal of this array is:
		1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12
"""

def matrix_spiral_print(M):
	# Time: O(n) 	Space: O(1)
	if len(M) == 0: return 
	m = min(len(M)//2 + len(M)%2, len(M[0])//2 + len(M[0])%2)

	for l in range(m):
		# Top
		for i in range(l, len(M[0]) - l):
			print(M[l][i], end = ' ')

		# Left
		for i in range(l+1, len(M) - l):
			print(M[i][len(M[0]) - l - 1], end = ' ')

		# Bottom
		if len(M) - 2 * l > 1:
			for i in range(len(M[0]) - l - 2, l - 1, -1):
				print(M[len(M) - l - 1][i], end = ' ')

		# Right
		if len(M[0]) - 2 * l > 1:
			for i in range(len(M) - l - 2, l , -1):
				print(M[i][l], end = ' ')

	print(' ')

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12