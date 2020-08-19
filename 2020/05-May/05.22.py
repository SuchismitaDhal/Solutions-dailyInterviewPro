# APPLE
"""
    SOLVED -- LEETCODE#160
    You are given two singly linked lists. The lists intersect at some node. 
    Find, and return the node. Note: the lists are non-cyclical.
    Example:
        A = 1 -> 2 -> 3 -> 4
        B = 6 -> 3 -> 4
    This should return 3 (you may assume that any nodes with the same value are the same node).
"""


def getlen(head):
    p = head
    len = 0
    while p:
        len += 1
        p = p.next
    return len


def pointto(head, diff):
    if diff <= 0:
        return head
    p = head
    while diff:
        p = p.next
        diff -= 1
    return p


def intersection(headA, headB):
    # Time: O(n)     Space: O(1)
    nA = getlen(headA)
    nB = getlen(headB)
    if nA == 0 or nB == 0:
        return None

    p = pointto(headA, nA-nB)
    q = pointto(headB, nB-nA)

    # p == q is for weaklings

    while p.next:
        if p.val == q.val:
            temp = p.next
            p.next = None
            if q.next == None:
                p.next = temp
                return q
            p.next = temp
        p = p.next
        q = q.next
    if p.val == q.val:
        p.next = ListNode(0)
        if q.next:
            p.next = None
            return p
        p.next = None
    return None


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def prettyPrint(self):
        c = self
        while c:
            print(c.val)
            c = c.next


a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersection(a, b)
c.prettyPrint()
# 3 4
