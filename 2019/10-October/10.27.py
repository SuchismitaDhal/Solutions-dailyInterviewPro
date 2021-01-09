# TWITTER
"""
	SOLVED -- LEETCODE#1161
    You are given the root of a binary tree. 
    Find the level for the binary tree with the minimum sum, and return that value.
    For instance, in the example below, the sums of the trees are 10, 2 + 8 = 10, and 4 + 1 + 2 = 7. 
    So, the answer here should be 7.
"""
from collections import deque
import math

class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def minimum_level_sum(root):
    # Time: O(n) 	Space: O(n)
    if not root: return 0
    sol = math.inf
    curr = 0
    Q = deque()

    Q.append(root)
    Q.append('.')
    while len(Q) > 1:
    	ele = Q.popleft()
    	if ele == '.':
    		Q.append('.')
    		sol = min(sol, curr)
    		curr = 0
    	else:
    		curr += ele.val
    		if ele.left:
    			Q.append(ele.left)
    		if ele.right:
    			Q.append(ele.right)

    return min(sol, curr)

#     10
#    /  \
#   2    8
#  / \    \
# 4   1    2
node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

print(minimum_level_sum(node))
#7