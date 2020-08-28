# FACEBOOK
"""
    QUESTION NOT CLEAR
    Given an undirected graph, determine if a cycle exists in the graph.
    Can you solve this in linear time, linear space?
"""


def find_cycle(graph):
    # Fill this in.
    return True


graph = {
    'a': {'a2': {}, 'a3': {}},
    'b': {'b2': {}},
    'c': {}
}
print(find_cycle(graph))
# False
graph['c'] = graph
print(find_cycle(graph))
# True
