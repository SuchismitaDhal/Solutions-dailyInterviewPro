# AIRBNB
"""
    SOLVED -- LEETCODE#61
    Given a linked list and a number k, rotate the linked list by k places.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        current = self
        ret = ''
        while current:
            ret += str(current.value)
            current = current.next
        return ret


def rotate_list(list, k):
    # Time: O(n)     Space: O(1)
    head = list
    if head == None or head.next == None:
        return head

    tail = head
    n = 1
    while tail.next != None:
        n += 1
        tail = tail.next

    k = k % n
    for i in range(k):
        temp = head
        head = head.next
        temp.next = None
        tail.next = temp
        tail = tail.next

    return head

    # Order is 1, 2, 3, 4
llist = Node(1, Node(2, Node(3, Node(4))))

# Order should now be 3, 4, 1, 2
print(rotate_list(llist, 2))
# 3412
