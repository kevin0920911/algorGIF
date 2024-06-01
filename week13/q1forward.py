INF = float('inf')

node, edge = [int(x) for x in input().split()]
graph = [[INF for _ in range(node)] for _ in range(node)]

for i in range(edge):
    u, v, w = [int(x) for x in input().split()]
    graph[u-1][v-1] = w
for row in graph:
    for elem in row:
        print(elem, end='\t')
    print()
    
def shortestPath(graph):
    node = len(graph)
    dist = [0] * node
    for i in range(1,node):
        dist[i] = INF
        for j in range(node):
            if graph[j][i] != INF:
                dist[i] = min(dist[i], graph[j][i] + dist[j])
    print(dist)
    return dist[node-1]

print(shortestPath(graph))