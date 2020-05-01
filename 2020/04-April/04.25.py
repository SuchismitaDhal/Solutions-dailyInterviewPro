# AIRBNB
"""
    SOLVED -- LEETCODE#19
    You are given a singly linked list and an integer k. 
    Return the linked list, removing the k-th last element from the list.
    Try to do it in a single pass and using constant space.
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)


def remove_kth_from_linked_list(head, k):
    # Time: O(n)     Space: O(1)
    c = 1
    fwd = head
    bck = None

    if head == None:
        return head

    while fwd.next != None:
        if c == k:
            bck = head
        elif c > k:
            bck = bck.next
        fwd = fwd.next
        c += 1

    if c == k:
        temp = head
        head = head.next
        temp.next = None
        del temp

    elif bck != None:
        temp = bck.next
        bck.next = temp.next
        temp.next = None
        del temp

    return head


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]
head = remove_kth_from_linked_list(head, 1)
print(head)
# [1, 2, 4, 5]
