# 从 typing 模块导入 List 类型
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}
        for i, num in enumerate(nums):
            if target - num in sum_map:
                return [sum_map[target-num], i]
            sum_map[num] = i
        return [-1, -1]

"""
题目: 1. 两数之和
链接: https://leetcode.cn/problems/two-sum/description/
思路:
     利用map记录 key:value=元素值:索引
     依次判断target-元素值 是否在map中 在则直接返回 不在则map[key] = value继续判断
"""
if __name__ == "__main__":
    # nums = [2,7,11,15]
    # target = 9

    nums = [3,2,4]
    target = 6

    solution = Solution()
    res = solution.twoSum(nums, target)
    print(res)