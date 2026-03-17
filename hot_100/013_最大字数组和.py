from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[:]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] + max(dp[i-1], 0)
        return max(dp)

"""
题目: 53. 最大子数组和
链接: https://leetcode.cn/problems/maximum-subarray
思路:
    1. dp[i] 表示以下标i为结尾的最大子数组和, 一定要包含i
    2. 递推公式: dp[i] = nums[i] + max(dp[i-1], 0)
    3. 初始化: nums[0]
    4. for循环遍历
    5. 返回最大的dp[i], 利用res保存进行返回
    6. dp数组
    nums: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    dp  : [-2, 1, -2, 4, 3,  5, 6, 1,  5]
"""

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [-2, -1]
    solution = Solution()
    res = solution.maxSubArray(nums)
    print(res)
    pass
