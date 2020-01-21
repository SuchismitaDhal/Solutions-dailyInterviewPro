# APPLE
"""
    SOLVED
    Given a list of undirected edges which represents a graph, 
    find out the number of connected components.

    In the example below, vertices 1, 2, 3, 4 are all connected, 
    and 5, 6 are connected, and thus there are 2 connected components in the graph above.
"""
adj = dict()
visited = dict()

def dfs(v):
    for u in adj[v]:
        if visited[u] == False:
            visited[u] = True
            dfs(u)

def num_connected_components0(edges):
    # dfs approach
    # Time: O(n+e)   Space: O(n)for dfs-stack + O(e)for adjacency list
    c = 0

    # building the adjacency list
    for e in edges:
        u = e[0]
        v = e[1]

        visited[u] = False
        visited[v] = False

        if u not in adj:
            adj[u] = list([v])
        else:
            adj[u].append(v)
        if v not in adj:
            adj[v] = list([u])
        else:
            adj[v].append(u)

    for node in visited:
        if visited[node] == False:
            c += 1
            visited[node] = True
            dfs(node)

    return c

##########################################################
parent = dict()

def union(u, v):
    for n in parent:
        if parent[n] == v:
            parent[n] = u

def num_connected_components1(edges):
    # union-find approach
    # Time: O(ne)   Space: O(n)

    for e in edges:
        u = e[0]
        v = e[1]

        if u not in parent:
            parent[u] = u
        if v not in parent:
            parent[v] = v

        if parent[u] < parent[v]:
            union(parent[u], parent[v])
        else:
            if parent[v] < parent[u]:
                union(parent[v], parent[u])

    c = 0
    for n in parent:
        if parent[n] == n:
            c += 1

    return c


print(num_connected_components([(1, 2), (2, 3), (4, 1), (5, 6)]))
# 2
