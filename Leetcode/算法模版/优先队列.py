# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码还未经过力扣测试，仅供参考，如有疑惑，可以参照我写的 java 代码对比查看。

class MaxPQ:
    """
    <Key extends Comparable<Key>>
    """
    def __init__(self, cap: int):
        """
        存储元素的数组
        """
        self.pq = [None] * (cap + 1)
        """
        当前 Priority Queue 中的元素个数
        """
        self.size = 0

    def max(self) -> int:
        """
        返回当前队列中最大元素
        """
        return self.pq[1]

    def insert(self, e: int) -> None:
        """
        插入元素 e
        """
        self.size += 1
        # 先把新元素加到最后
        self.pq[self.size] = e
        # 然后让它上浮到正确的位置
        self.swim(self.size)

    def delMax(self) -> int:
        """
        删除并返回当前队列中最大元素
        """
        max = self.pq[1]
        # 把这个最大元素换到最后，删除之
        self.swap(1, self.size)
        self.pq[self.size] = None
        self.size -= 1
        # 让 pq[1] 下沉到正确位置
        self.sink(1)
        return max

    def swim(self, x: int) -> None:
        """
        上浮第 x 个元素，以维护最大堆性质
        """
        while (x > 1 and self.bigger(self.parent(x), x)):
            # 如果第 x 个元素比上层大
            # 将 x 换上去
            self.swap(self.parent(x), x)
            x = self.parent(x)

    def bigger(self,i,j):
        return self.pq[i] >= self.pq[j]

    def sink(self, x: int) -> None:
        """
        下沉第 x 个元素，以维护最大堆性质
        """
        while self.left(x) <= self.size:
            # 先假设左边节点较大
            max = self.left(x)
            # 如果右边节点存在，比一下大小
            if self.right(x) <= self.size and self.less(max, self.right(x)):
                max = self.right(x)
            # 结点 x 比俩孩子都大，就不必下沉了
            if self.less(max, x):
                break
            # 否则，不符合最大堆的结构，下沉 x 结点
            self.swap(x, max)
            x = max

    def swap(self, i: int, j: int) -> None:
        """
        交换数组的两个元素
        """
        temp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = temp

    def less(self, i: int, j: int) -> bool:
        """
        pq[i] 是否比 pq[j] 小？
        """
        return self.pq[i] < self.pq[j]

    def left(self, index: int) -> int:
        """
        还有 left 三个方法
        """
        return index * 2

    def right(self, index: int) -> int:
        return index * 2 + 1

    def parent(self, index: int) -> int:
        return index // 2