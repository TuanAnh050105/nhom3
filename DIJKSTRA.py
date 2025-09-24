import heapq

def dijkstra(graph, start):

    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]  

    while pq:
        current_dist, u = heapq.heappop(pq)


        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return dist



G = {
    0: [(1, 1), (2, 4)],
    1: [(2, 2), (3, 5)],
    2: [(3, 1)],
    3: []
}

print("Kết quả với đồ thị ban đầu:")
distances = dijkstra(G, 0)
for node in distances:
    print(f"Khoảng cách từ 0 -> {node}: {distances[node]}")


G2 = {
    0: [(1, 1), (2, 1)], 
    1: [(2, 2), (3, 5)],
    2: [(3, 1)],
    3: []
}

print("\nKết quả sau khi thay đổi trọng số (0,2) = 1:")
distances2 = dijkstra(G2, 0)
for node in distances2:
    print(f"Khoảng cách từ 0 -> {node}: {distances2[node]}")


G3 = {
    0: [(1, 2), (2, 6)],
    1: [(2, 3), (3, 1)],
    2: [(3, 1), (4, 5)],
    3: [(4, 2)],
    4: []
}

print("\nKết quả với đồ thị 5 đỉnh:")
distances3 = dijkstra(G3, 0)
for node in distances3:
    print(f"Khoảng cách từ 0 -> {node}: {distances3[node]}")
