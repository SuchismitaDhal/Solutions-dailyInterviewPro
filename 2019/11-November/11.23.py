# APPLE
"""
	SOLVED -- LEETCODE#103
    Given a binary tree, return the list of node values 
    in zigzag order traversal. Here's an example

   Input:
           1
         /   \
        2     3
       / \   / \
      4   5 6   7

   Output: [1, 3, 2, 4, 5, 6, 7]
"""
from collections import deque

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def zigzag_order(tree):
    # Time: O(n) 	Space: O(n)
    if not tree: return []
    Q = deque()

    sol = []
    currlvl = []
    lvl = 0

    Q.append(tree)
    Q.append('.')
    while len(Q) > 1:
    	ele = Q.popleft()
    	if ele == '.':
    		if lvl % 2:
    			currlvl.reverse()
    		sol.extend(currlvl)
    		currlvl = []
    		lvl += 1
    		Q.append('.')
    	else:
    		currlvl.append(ele.value)
    		if ele.left: Q.append(ele.left)
    		if ele.right: Q.append(ele.right)

    if lvl % 2:
    	currlvl.reverse()
    sol.extend(currlvl)

    return sol

n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, n4, n5)
n3 = Node(3, n6, n7)
n1 = Node(1, n2, n3)

print(zigzag_order(n1))
# [1, 3, 2, 4, 5, 6, 7]
