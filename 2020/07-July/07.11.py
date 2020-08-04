# TWITTER
"""
    SOLVED -- LEETCODE#82
    Given a linked list, remove all duplicate values from the linked list.
    For instance, given 1 -> 2 -> 3 -> 3 -> 4, 
    then we wish to return the linked list 1 -> 2 -> 4.
"""


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return str(self.val)
        return str(self.val) + " " + str(self.next)


class Solution(object):
    def deleteDuplicates(self, node):
        sol = Node('.')
        last = sol
        prev = None
        ptr = node

        while ptr:
            if not ptr.next or ptr.next.val != ptr.val:
                if prev != ptr.val:
                    last.next = ptr
                    prev = ptr.val
                    ptr = ptr.next
                    last = last.next
                    last.next = None
                else:
                    temp = ptr
                    prev = ptr.val
                    ptr = ptr.next
                    temp.next = None
                    del temp

            else:
                prev = ptr.val
                temp = ptr
                ptr = ptr.next
                temp.next = None
                del temp

        node = sol.next


n = Node(1, Node(2, Node(3, Node(3, Node(4)))))
print(n)
# 1 2 3 3 4
Solution().deleteDuplicates(n)
print(n)
# 1 2 4
