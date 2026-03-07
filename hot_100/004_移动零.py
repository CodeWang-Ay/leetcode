# 从 typing 模块导入 List 类型
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nozero_count = 0
        for cur_num in nums:
            if cur_num != 0:
                nums[nozero_count] = cur_num
                nozero_count += 1
        
        # print(nums)
        # print(nozero_count)
        # 将剩余的元素赋值为0
        for cur_num in nums[nozero_count:]:
            nums[nozero_count] = 0
            nozero_count += 1
            pass
        return nums

"""
题目: 128. 最长连续序列
链接: https://leetcode.cn/problems/longest-consecutive-sequence
思路:
    1. 利用快慢指针，快指针每次移动一步
    2. 如果当前元素不等于0，慢指针进行赋值移动，
    3. 如果当前元素等于0，慢指针不懂，
    4. 最后将nums[slow:] 都赋值为0
"""
if __name__ == "__main__":
    # nums = [0,1,0,3,12]
    nums = [0]
    solution = Solution()
    res = solution.moveZeroes(nums)
    print(res)
    pass
