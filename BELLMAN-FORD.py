def bellman_ford(n, edges, src):
    dist = [float("inf")] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            print("Phát hiện chu trình âm!")
            return None
    return dist
edges = [
    (0, 1, 1),
    (0, 2, 4),
    (1, 2, -3),
    (2, 3, 2)
]

print("=== Đồ thị ban đầu ===")
dist = bellman_ford(4, edges, 0)
print("Khoảng cách ngắn nhất từ 0:", dist)
print()


edges2 = edges + [(3, 4, -2)]
print("=== Thêm cạnh (3,4,-2) ===")
dist = bellman_ford(5, edges2, 0)
print("Khoảng cách ngắn nhất từ 0:", dist)
print()


edges3 = edges + [(2, 3, -6), (3, 2, 4)]
print("=== Kiểm tra chu trình âm ===")
dist = bellman_ford(4, edges3, 0)
if dist:
    print("Khoảng cách ngắn nhất từ 0:", dist)
print()


edges4 = [
    (0, 1, 5),
    (0, 2, 2),
    (1, 2, 1),
    (2, 3, 7)
]
print("=== Đồ thị không có cạnh âm ===")
dist = bellman_ford(4, edges4, 0)
print("Khoảng cách ngắn nhất từ 0:", dist)
