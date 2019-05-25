import sys
import math

def dijkstra(graph, initial, dest):
    dist = {}
    prev = {}
    queue = []

    for v in graph:
        queue.append(v)
        dist[v] = math.inf
        prev[v] = None
    dist[initial] = 0

    while queue:
        u = min(queue, key = lambda x: dist[x])
        queue.pop(queue.index(u))

        for v in filter(lambda x:x in queue, graph[u]):
            alt = dist[u] + graph[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist, prev

def shortest_path(prev, dest):
    S = []
    u = dest

    if prev[u] or prev[u] == dest:
        while u:
            S.insert(0,u)
            u = prev[u]
    return S

def k_shortest_paths(graph, initial, dest, K):
    print(type(K))
    dist, prev = dijkstra(graph, initial, dest)

    A = shortest_path(prev, dest)
    B = []

    for _ in range(1, K):
        for i in range(len(A)-2):
            spur = A[i]
            rootPath = A[0:i]

            for p in A:
                if rootPath == p[0:i]:
                    graph.pop(p[i])
            for rootPathNode in rootPath:
                if rootPathNode != spur:
                    graph.pop(rootPathNode)
    


def main(input_file):
    with open(input_file) as input:
        n, m = input.readline().replace('\n', '').split(' ')
        n, m = int(n), int(m)

        graph = {}

        for count, line in enumerate(input.readlines()):
            line = line.replace('\n','').split(' ')
            
            if count == m:
                initial, destination, k = line
                graph[destination] = {}
            else:
                edge_from, edge_to, vertex_weight = line
                if edge_from not in graph:
                    graph[edge_from] = {edge_to: float(vertex_weight)}
                else:
                    graph[edge_from][edge_to] = float(vertex_weight)
        k_shortest_paths(graph, initial, destination, int(k))

if __name__ == "__main__":
    main(sys.argv[1])