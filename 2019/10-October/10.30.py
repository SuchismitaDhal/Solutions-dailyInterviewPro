# UBER
"""
	SOLVED -- LEETCODE#141
    Given a linked list, determine if the linked list has a cycle in it. 
    For notation purposes, we use an integer pos 
    which represents the zero-indexed position where the tail connects to.
    Example:
    Input: head = [4,3,2,1,0], pos = 1.  
    Output: true
    The example indicates a list where the tail connects to the second node.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        # Time: O(n)    Space: O(1)
        fast = slow = head
        while True:
            slow = slow.next
            if not fast.next or not fast.next.next:
                return False
            fast = fast.next.next
            if fast == slow: return True

testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail
testTail.next = node1

print(Solution().hasCycle(testHead))
# True
