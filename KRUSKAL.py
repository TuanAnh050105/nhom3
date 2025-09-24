
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False  
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True


def kruskal(n, edges):

    edges.sort(key=lambda x: x[2])
    dsu = DSU(n)
    mst = []
    total_weight = 0

    for u, v, w in edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            total_weight += w


        if len(mst) == n - 1:
            break

    return mst, total_weight



edges = [
    (0, 1, 1),
    (0, 2, 3),
    (1, 2, 4),
    (1, 3, 2),
    (2, 3, 5)
]

n = 4  

mst, total = kruskal(n, edges)

print("Các cạnh trong cây khung nhỏ nhất:")
for u, v, w in mst:
    print(f"({u}, {v}) trọng số = {w}")
print("Tổng trọng số MST =", total)
