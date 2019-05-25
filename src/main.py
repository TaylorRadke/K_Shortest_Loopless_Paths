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

        for v in graph[u]:                
            alt = graph[u][v] + path_cost
            if (v in prev and alt < dist[u]) or v not in prev:
                prev[v] = u
                heappush(queue, (alt, v))


    return dist[dest], shortest_path(prev, initial, dest)

def shortest_path(prev, initial, dest):
    S = []
    u = dest
    if prev[u] or prev[u] == dest:
        while u:
            S.insert(0,u)
            if u == initial:
                break
            u = prev[u]
    print(S)
    return S

def k_shortest_paths(graph, initial, dest, K):
    dist, path = dijkstra(graph, initial, dest)
    A = [{"cost": dist, "path": path}]
    B = []

    
    # for k in range(1, K):
    
    #     for i in range(len(A[k-1]["path"]) - 2):
    #         edges_removed = []
    #         spurNode = A[k-1]["path"][i]
    #         rootPath = A[k-1]["path"][0:i]

    #         for p in A:
    #             if rootPath == p["path"][0:i]:
    #                 if p["path"][i] in graph:
    #                     edges_removed.append({
    #                         p["path"][i]: graph[p["path"][i]]
    #                         })

    #                     graph.pop(p["path"][i])
    #                 if p["path"][i+1] in graph:
    #                     edges_removed.append(
    #                         {
    #                             p["path"][i+1]: graph[p["path"][i+1]]
    #                         })
    #                     graph.pop(p["path"][i+1])

    #         for root_path_node in rootPath:
    #             if root_path_node != spurNode:
    #                 if root_path_node in graph:
    #                     edges_removed.append({
    #                         root_path_node: graph[root_path_node]
    #                         })
    #                     graph.pop(root_path_node)

    #         spur_dist, spur_path = dijkstra(graph, spurNode, dest)

    #         total_path = []
    #         total_path.extend(rootPath)
    #         total_path.extend(spur_path)
            
    #         print(f"i is {i}")

    #         B.append(total_path)
        
    #     if len(B) == 0:
    #         break
    #     B.sort()
    #     A[k] = B[0]
    #     B.pop()
    # return A
            


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