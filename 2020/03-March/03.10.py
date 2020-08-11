# AMAZON
"""
    SOLVED -- LEETCODE#83
    Given a sorted linked list of integers, remove all the duplicate elements 
    in the linked list so that all elements in the linked list are unique.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"({self.value}, {self.next})"


def remove_dup(lst):
    # Time: O(n)   Space: O(1)
    if lst == None or lst.next == None:
        return
    prev = lst
    curr = lst.next
    while curr:
        if curr.value == prev.value:
            curr = curr.next
            prev.next = curr
        else:
            prev = curr
            curr = curr.next


lst = Node(1, Node(2, Node(2, Node(3, Node(3)))))

remove_dup(lst)
print(lst)
# (1, (2, (3, None)))
