# MICROSOFT
"""
    You are given a doubly linked list. Determine if it is a palindrome.
    Can you do this for a singly linked list?
"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def dllend(node):
    while node.next != None:
        node = node.next
    return node


def sllend(node):
    rev = Node(node.val)

    while node.next != None:
        node = node.next
        nw = Node(node.val)
        nw.next = rev
        rev = nw

    return rev


def is_palindrome_dll(node):
    # Time : O(n)
    # Space : O(1)
    if node == None:
        return True

    head = node
    tail = dllend(node)

    while tail != head and tail.next != head:
        if head.val != tail.val:
            return False
        head = head.next
        tail = tail.prev
    return True


def is_palindrome_sll(node):
    # Time : O(n)
    # Space : O(n), can be optimised to O(1)
    # if we reverse only the second half of
    # the linked list inplace

    head = node
    tail = sllend(node)

    while head != None:
        if head.val != tail.val:
            return False
        head = head.next
        tail = tail.next
    return True


node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next

print(is_palindrome_dll(node))
# True
