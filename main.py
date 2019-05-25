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
    return dist[dest], shortest_path(prev, dest)

def shortest_path(prev, dest):
    S = []
    u = dest

    if prev[u] or prev[u] == dest:
        while u:
            S.insert(0,u)
            u = prev[u]
    return S

def k_shortest_paths(graph, initial, dest, K):
    dist, path = dijkstra(graph, initial, dest)
    A = []
    B = []
    A.append({"cost": dist, "path": path})
    print(len(A[0]["path"]) - 2)
    # for k in range(1, K):
    #     for i in range(len(A[k-1]["path"]) - 2):
    #         spurNode = A[k-1]["path"][i]
    #         rootPath = A[k-1]["path"][0:i]

    


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