#TWITTER
"""
    SOLVED -- LEETCODE#23
    You are given an array of k sorted singly linked lists. 
    Merge the linked lists into a single sorted linked list and return it.
"""
import heapq

class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer

def merge(lists):
    # Time: O(nlogk)  Space: O(k)
    pq = []
    for i in range(len(lists)):
        temp = lists[i]
        lists[i] = lists[i].next
        temp.next = None
        heapq.heappush(pq, (temp.val, i, temp))

    head, tail = None, None
    while pq:
        val, idx, node = heapq.heappop(pq)
        if not head:
            head, tail = node, node
        else:
            tail.next = node
            tail = tail.next
        if lists[idx]:
            temp = lists[idx]
            lists[idx] = lists[idx].next
            temp.next = None
            heapq.heappush(pq, (temp.val, idx, temp))

    return head

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print (merge([a, b]))
# 123456
