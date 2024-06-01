INF = float('inf')

node, edge = [int(x) for x in input().split()]
graph = [[INF for _ in range(node)] for _ in range(node)]

for i in range(edge):
    u, v, w = [int(x) for x in input().split()]
    graph[u-1][v-1] = w

def shortestPath(graph):
    node = len(graph)
    dist = [0] * node
    for i in range(node-2,-1,-1):
        dist[i] = INF
        for j in range(node):
            if graph[i][j] != INF:
                dist[i] = min(dist[i], graph[i][j] + dist[j])
    return dist[0]

print(shortestPath(graph))