class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1

# 示例
disjoint_set = DisjointSet(8) # 节点编号0-7
disjoint_set.union(0, 5)
print(disjoint_set.find(0))
print(disjoint_set.find(5))
print(disjoint_set.find(2)) # 0,5是队友，但和2还不是队友
disjoint_set.union(2, 4)
disjoint_set.union(0, 4)
print(disjoint_set.find(2))
print(disjoint_set.find(5)) # 2, 5是队友了

print(disjoint_set.parent)
print(disjoint_set.rank)