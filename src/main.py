import sys
import math
from heapq import heappush, heappop          
import timeit


def dijkstra(graph, initial, dest):
    dist = {}
    prev = {}
    queue = [(0, initial)]

    while queue:
        path_cost, u = heappop(queue)

        dist[u] = path_cost
        if u in graph:
            for v in graph[u]:                
                alt = graph[u][v] + path_cost
                if (v in prev and alt < dist[u]) or v not in prev:
                    prev[v] = u
                    heappush(queue, (alt, v))

    return dist[dest], shortest_path(prev, initial, dest)

def shortest_path(prev, initial, dest):
    path = []
    u = dest
    if prev[u] or prev[u] == dest:
        while u:
            path.insert(0, u)
            if u == initial:
                break
            u = prev[u]
    return path

def k_shortest_paths(graph, initial, dest, K):
    dist, path = dijkstra(graph, initial, dest)

    dists = [dist]
    A = [path]
    B = []
    
    for k in range(1, 2):
        for i in range(len(A[k-1]) - 2):
          
            nodes_removed = []
            vertex_removed = []
            spur_node = A[k-1][i]
            root_path = A[k-1][0:i]
        
            for p in A:
                if root_path == p[0:i] and p[i] in graph:
                    vertex_removed.append((p[i], p[i+1], graph[p[i]][p[i+1]]))
                    graph[p[i]].pop(p[i+1])
            
            for root_path_node in root_path:
                if root_path_node != spur_node:
                    nodes_removed.append((root_path_node, graph[root_path_node]))
                    graph.pop(root_path_node)
            
            spur_dist, spur_path = dijkstra(graph, spur_node, dest)
            print(spur_dist)
            total_path = [item for item in root_path]
            total_path.extend(spur_path)
            
            heappush(B, total_path)

            for ver in vertex_removed:
                graph[ver[0]][ver[1]] = ver[2]

            for node in nodes_removed:
                graph[node[0]] = node[1]
            

            


    
            
        
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