'''
快慢指针
'''

def removeDuplicates(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    # 维护 nums[0..slow] 无重复
    slow = 0
    fast = 1
    while fast < len(nums):
        if (慢指针往前面走):
            slow += 1
        fast += 1
    # 数组长度为索引 + 1
    return slow +

'''
滑动窗口
'''
def slidingWindow(s: str, t: str):
    from collections import defaultdict
    need = defaultdict(int)
    window = defaultdict(int)
    for c in t:
        need[c] += 1

    left, right = 0, 0
    valid = 0
    while right < len(s):
        c = s[right]
        right += 1
        # 进行窗口内数据的一系列更新
        window[c] += 1

        while window needs shrink:
            d = s[left]
            left += 1
            # 进行窗口内数据的一系列更新

'''
二分查找
'''
def binarySearch(nums: List[int], target: int) -> int:
    # 一左一右两个指针相向而行
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binarySearch_for_left(nums: List[int], target: int) -> int:
    # 一左一右两个指针相向而行
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            right = mid-1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def def binarySearch_for_right(nums: List[int], target: int) -> int:
    # 一左一右两个指针相向而行
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            left = mid+1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return right

'''
判断回文字符串
'''
def palindrome(s: str, l: int, r: int) -> str:
    # 防止索引越界
    while l >= 0 and r < len(s) and s[l] == s[r]:
        # 双指针，向两边展开
        l -= 1
        r += 1
    # 返回以 s[l] 和 s[r] 为中心的最长回文串
    return s[l + 1 : r]


