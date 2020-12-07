# UBER
"""
    Given a linked list of integers, remove all consecutive nodes that sum up to 0.
    Example:
        Input: 10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4
        Output: 10
        The consecutive nodes 5 -> -3 -> -3 -> 1 sums up to 0 so that sequence should be removed.
        4 -> -4 also sums up to 0 too so that sequence should also be removed.
"""
from collections import defaultdict
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def removeConsecutiveSumTo0(node):
    seensum = defaultdict(list)
    head = Node(0, node)

    presum = 0
    itr = head.next
    seensum[0].append(head)

    while itr:
        presum += itr.value
        seensum[presum].append(itr)
        itr = itr.next

    for nodes in seensum.values():
        for i in range(1, len(nodes), 2):
            nodes[i-1].next = nodes[i].next

    return head.next

node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
while node:
  print(node.value)
  node = node.next
# 10