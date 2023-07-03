import random
import heapq
class State:
    def __init__(self, id, disToStart):
        self.id = id
        self.disToStart = disToStart

'''
DIJKSTRA 算法模板
'''
def Dijkstra(start: int, graph: [[int]]):
    disToStart = [float('inf') for i in range(len(graph))]
    disToStart[start] = 0
    pq = []
    start_point = State(start, 0)
    heapq.heappush(pq, (start_point.disToStart, random.random(), start_point))
    while pq:
        distance, _, point = heapq.heappop(pq)
        if point.disToStart > disToStart[point.id]:
            continue
        for i in graph[point.id]:
            next_point_id = i[0]
            distance = i[1]
            next_point_distance = disToStart[point.id] + distance
            if disToStart[next_point_id] > next_point_distance:
                next_point = State(next_point_id, next_point_distance)
                heapq.heappush(pq, (next_point_distance, random.random(), next_point))
                disToStart[next_point_id] = next_point_distance
    return disToStart

'''
查并集模版
'''

class UF:
    def __init__(self, n: int):
        self.count = n
        self.parent = [i for i in range(n)]
        # 新增一个数组记录树的“重量”
        self.size = [1] * n

    def union(self, p: int, q: int) -> None:
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return

        # 小树接到大树下面，较平衡
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        self.count -= 1

    def connected(self, p: int, q: int) -> bool:
        root_p = self.find(p)
        root_q = self.find(q)
        return root_p == root_q

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            # 这行代码进行路径压缩
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def count(self) -> int:
        return self.count

