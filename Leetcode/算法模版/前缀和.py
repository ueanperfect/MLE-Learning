'''
前缀和
'''
class NumArray:
    def __init__(self, nums: List[int]):
        # 前缀和数组
        self.preSum = [0] * (len(nums) + 1)
        # 计算 nums 的累加和
        for i in range(1, len(self.preSum)):
            self.preSum[i] = self.preSum[i - 1] + nums[i - 1]
## prSum记录的是nums[:i-1]的和

##【left,right】 = [right]-sum([left-1]) = preSum[left]


    def sumRange(self, left: int, right: int) -> int:
        # 查询闭区间 [left, right] 的累加和
        return self.preSum[right + 1] - self.preSum[left]

'''
差分数组
'''
class NumArray:
    def __init__(self, nums: List[int]):
        # 构造差分数组
        diff[0] = nums[0]
        for i in range(1, len(nums)):
            diff[i] = nums[i] - nums[i - 1]

        ##【left,right】 = [right]-sum([left-1]) = preSum[left]

    res = [0] * len(diff)
    res[0] = diff[0]
    for i in range(1, len(diff)):
        res[i] = res[i - 1] + diff[i]


# 给闭区间 [i, j] 增加 val（可以是负数）
def increment(self, i: int, j: int, val: int) -> None:
    self.diff[i] += val
    if j + 1 < len(self.diff):
        self.diff[j + 1] -= val


