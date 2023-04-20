'''
单调栈
'''
def nextGreaterElement(nums: List[int]) -> List[int]:
    n = len(nums)
    # 存放答案的数组
    res = [0 for _ in range(n)]
    s = []
    # 倒着往栈里放
    for i in range(n - 1, -1, -1):
        # 判定个子高矮
        while s and s[-1] <= nums[i]:
            # 矮个起开，反正也被挡着了。。。
            s.pop()
        # nums[i] 身后的更大元素
        res[i] = s[-1] if s else -1
        s.append(nums[i])
    return res

'''
单调队列
'''
class MonotonicQueue:
    def __init__(self):
        self.maxq = []

    def push(self, n):
        # 将小于 n 的元素全部删除
        while self.maxq and self.maxq[-1] < n:
            self.maxq.pop()
        # 然后将 n 加入尾部
        self.maxq.append(n)

    def max(self):
        return self.maxq[0]

    def pop(self, n):
        if n == self.maxq[0]:
            self.maxq.pop(0)