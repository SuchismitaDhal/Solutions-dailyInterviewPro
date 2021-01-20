# TWITTER
"""
	SOLVED -- LEETCODE#24
	Given a linked list, swap the position of the 1st and 2nd node, 
	then swap the position of the 3rd and 4th node etc.
"""

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def __repr__(self):
		return f"{self.value}, ({self.next.__repr__()})"

def swap_every_two(llist):
	# Time: O(n)    Space: O(1)
	if not llist or not llist.next:
		return llist
	
	head = Node(0, llist)
	ptr = head

	while ptr.next and ptr.next.next:
		temp = ptr.next
		ptr.next = temp.next
		temp.next = ptr.next.next
		ptr.next.next = temp
		ptr = temp		

	return head.next

llist = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(swap_every_two(llist))
# 2, (1, (4, (3, (5, (None)))))
