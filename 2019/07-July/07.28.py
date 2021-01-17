# MICROSOFT
"""
    SOLVED -- LEETCODE#2
    You are given two linked-lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.
"""
import math

class ListNode(object):
	# object is the base class for all classes in Python.
	# It is a new-style class, so inheriting from object makes ListNode a new-style class.
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def addTwoNumbers(self, l1, l2, c=0):
		# O(n) time and O(n) space
		p = ListNode(0)
		lst = p

		while l1 != None and l2 != None:
			x = l1.val + l2.val + c
			c = math.floor(x / 10)
			x = x - c*10
			p.next = ListNode(x)
			p = p.next
			l1 = l1.next
			l2 = l2.next

		if l1 == None:
			while l2 != None:
				x = l2.val + c
				c = math.floor(x / 10)
				x = x - c*10
				p.next = ListNode(x)
				p = p.next
				l2 = l2.next

		if l2 == None:
			while l1 != None:
				x = l1.val + c
				c = math.floor(x / 10)
				x = x - c*10
				p.next = ListNode(x)
				p = p.next
				l1 = l1.next

		if c > 0:
			p.next = ListNode(c)

		if lst.next != None:
			lst = lst.next

		return lst


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
# output : 7 0 8
