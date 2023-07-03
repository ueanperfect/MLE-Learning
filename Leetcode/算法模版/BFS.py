from typing import List, Set, Tuple


class Node:
    def adj(self) -> List[Node]:
        pass


def BFS(start: Node, target: Node) -> int:
    q: List[Node] = []  # 核心数据结构
    visited: Set[Node] = set()  # 避免走回头路

    q.append(start)  # 将起点加入队列
    visited.add(start)
    step: int = 0  # 记录扩散的步数

    while q:
        sz: int = len(q)
        # 将当前队列中的所有节点向四周扩散
        for i in range(sz):
            cur: Node = q.pop(0)
            # 划重点：这里判断是否到达终点
            if cur is target:
                return step
            # 将 cur 的相邻节点加入队列
            for x in cur.adj():
                if x not in visited:
                    q.append(x)
                    visited.add(x)
        # 划重点：更新步数在这里
        step += 1