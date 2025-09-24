import heapq

def prim(n, edges, start=0):

    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w)) 

    visited = [False] * n
    mst = []
    total_weight = 0

  
    pq = []
    visited[start] = True
    for v, w in graph[start]:
        heapq.heappush(pq, (w, start, v))

    print(f"Bắt đầu từ đỉnh {start}")

    while pq and len(mst) < n - 1:
        w, u, v = heapq.heappop(pq)
        if visited[v]:
            continue
        visited[v] = True
        mst.append((u, v, w))
        total_weight += w
        print(f"Chọn cạnh ({u}, {v}) với trọng số {w}")

        for nxt, w2 in graph[v]:
            if not visited[nxt]:
                heapq.heappush(pq, (w2, v, nxt))

    return mst, total_weight



edges = [
    (0, 1, 1),
    (0, 3, 2),
    (1, 2, 3),
    (1, 4, 2),
    (2, 4, 1),
    (2, 5, 3),
    (3, 5, 2)
]

print("=== Chạy Prim từ đỉnh 0 ===")
mst, total = prim(6, edges, start=0)
print("MST:", mst)
print("Tổng trọng số:", total)
print()

print("=== Chạy Prim từ đỉnh 3 ===")
mst, total = prim(6, edges, start=3)
print("MST:", mst)
print("Tổng trọng số:", total)
print()

print("=== Chạy Prim sau khi thay đổi trọng số (0,3) = 6 ===")
edges_mod = [
    (0, 1, 1),
    (0, 3, 6),  
    (1, 2, 3),
    (1, 4, 2),
    (2, 4, 1),
    (2, 5, 3),
    (3, 5, 2)
]
mst, total = prim(6, edges_mod, start=0)
print("MST:", mst)
print("Tổng trọng số:", total)
