import sys
import math

def dijkstra(graph, initial, destination):
    dists = dict()
    visited = set()
    queue: int = [key for key in graph]
    for key in graph:
        if key == initial:
            dists[key] = 0
        else:
            dists[key] = math.inf

    while queue:
        min_dist_node = min(filter(lambda x: x not in visited, queue))
        queue.pop(queue.index(min_dist_node))
        visited.add(min_dist_node)
        for neighbour in graph[min_dist_node]:
            alt = dists[min_dist_node] + graph[min_dist_node][neighbour]
            if alt < dists[neighbour]:
                dists[neighbour] = alt
    return dists[destination]

def k_shortest_paths(graph, initial, destination, k):
    """
    Find the K shortest loopless paths from the initial edge to destination edge
    """
    shortest_path = dijkstra(graph, initial, destination)

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
                    graph[edge_from] = {edge_to: int(vertex_weight)}
                else:
                    graph[edge_from][edge_to] = int(vertex_weight)
        a = k_shortest_paths(graph, initial, destination, k)

if __name__ == "__main__":
    main(sys.argv[1])