#FACEBOOK
"""
    SOLVED -- NO SIMILAR PROBLEM FOUND
    Given a directed graph, reverse the directed graph so all directed edges are reversed.
    Example:
    Input:
        A -> B, B -> C, A ->C
    Output:
        B -> A, C -> B, C -> A
"""

from collections import defaultdict

class Node:
  def __init__(self, value):
    self.adjacent = []
    self.value = value

def reverse_graph(graph):
    # Time: O(n + e)    Space: O(n + e)
    reverseadj = defaultdict(list)

    for node in graph.values():
        for adj in node.adjacent:
            reverseadj[adj].append(node.value)

    for node in graph.values():
        node.adjacent = reverseadj[node]
        
    return graph

a = Node('a')
b = Node('b')
c = Node('c')

a.adjacent += [b, c]
b.adjacent += [c]

graph = {
    a.value: a,
    b.value: b,
    c.value: c,
}

for _, val in reverse_graph(graph).items():
  print(val.adjacent)
# []
# ['a']
# ['a', 'b']
# changed to correct output