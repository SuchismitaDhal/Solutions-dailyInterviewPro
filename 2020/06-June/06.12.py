# MICROSOFT
"""
    SOLVED -- LEETCODE#234
    You are given a doubly linked list. Determine if it is a palindrome.
    Can you do this for a singly linked list?
"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def is_palindrome_util(node, l):
    if l == 0:
        return True, node
    if l == 1:
        return True, node.next

    sol, ptr = is_palindrome_util(node.next, l - 2)
    if sol == True:
        if node.val == ptr.val:
            return True, ptr.next
        else:
            return False, None
    else:
        return False, None


def is_palindrome(node):
    # For singly linked list
    # Time: O(n)    Space: O(n)
    l = 0
    ptr = node
    while ptr != None:
        l += 1
        ptr = ptr.next
    sol, p = is_palindrome_util(node, l)
    return sol


node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next

print(is_palindrome(node))
# True
