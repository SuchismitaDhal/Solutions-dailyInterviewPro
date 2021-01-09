# FACEBOOK
"""
	SOLVED -- LEETCODE#218
	Given a list of building in the form of (left, right, height), 
	return what the skyline should look like. 
	The skyline should be in the form of a list of (x-axis, height), 
	where x-axis is the next point where there is a change in height starting from 0, 
	and height is the new height starting from the x-axis.
"""
from heapq import *
def generate_skyline(buildings):
	# Time: O(nlogn) 	Space: O(n)
	buildings.sort(key = lambda x: (x[0], -x[2], -x[1]))
	Q = []
	i = 0

	sol = []
	while i < len(buildings):
		if not Q:
			#print('empty Q at', i)
			heappush(Q, (-buildings[i][2], buildings[i][1]))
			sol.append((buildings[i][0], buildings[i][2]))
			i += 1

		elif Q[0][1] > buildings[i][0]:
			#print('pushing Q at', i)
			currh = -Q[0][0]
			heappush(Q, (-buildings[i][2], buildings[i][1]))
			if -Q[0][0] != currh:
				sol.append((buildings[i][0], buildings[i][2]))
			i += 1

		else:
			#print('popping Q at', i)
			currtime = Q[0][1]
			while Q and Q[0][1] <= currtime:
				heappop(Q)
			currh = -Q[0][0] if Q else 0
			sol.append((currtime + 1, currh))

	while Q:
		#print(Q)
		#print('popping Q at', i)
		currtime = Q[0][1]
		while Q and Q[0][1] <= currtime:
			heappop(Q)
		currh = -Q[0][0] if Q else 0
		sol.append((currtime + 1, currh))	

	return sol


#              2 2 2
#              2 2 2
#         1 1 2 2 2 1 1
#         1 1 2 2 2 1 1
#         1 1 2 2 2 1 1
# pos: 1 2 3 4 5 6 7 8 9
print(generate_skyline([(2, 8, 3), (4, 6, 5)]))
# [(2, 3), (4, 5), (7, 3), (9, 0)]
