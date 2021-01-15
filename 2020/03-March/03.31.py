# APPLE
"""
	SOLVED -- LEETCODE#232
    Implement a queue class using two stacks. 
    A queue is a data structure that supports the FIFO protocol (First in = first out). 
    Your class should support the enqueue and dequeue methods like a standard queue.
"""


class Queue:
    def __init__(self):
    	self.stack = []

    def enqueue(self, val):
    	# Time: O(n) 	Space: O(n)
    	temp = []
    	while self.stack:
    		x = self.stack[-1]
    		self.stack.pop()
    		temp.append(x)

    	self.stack.append(val)
    	while temp:
    		x = temp[-1]
    		temp.pop()
    		self.stack.append(x)

    def dequeue(self):
    	# Time: O(1) 	Space: O(1)
    	x = self.stack[-1]
    	self.stack.pop()
    	return x

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3
