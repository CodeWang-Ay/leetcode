from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[:]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] + max(dp[i-1], 0)
        return max(dp)
    
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prefix_sum = 0                                              # 计算pre_nums[i]
        min_pre_sum = 0                                             # 计算pre_nums[j] 最小的
        max_num = nums[0]                                           # 最大字数组和
        for cur_num in nums:
            prefix_sum += cur_num                                   # 当前前缀和 nums[0] +... + nums[i-1]
            max_num = max(max_num, prefix_sum - min_pre_sum)        # 先计算
            min_pre_sum = min(min_pre_sum, prefix_sum)              # 然后在计算 pre_nums[j]
            print(f"prefix_sum: {prefix_sum}, min_prefix_sum: {prefix_sum}")
        return max_num

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

思路2:
核心思想：
    定义前缀和数组 pre_sum，其中 pre_sum[i] = nums[0] + ... + nums[i-1]
    子数组 nums[j...i] 的和 = pre_sum[i+1] - pre_sum[j]
    要让这个和最大，等价于：在遍历 pre_sum 时，对于当前 pre_sum[i+1]，找到之前最小的 pre_sum[j]，
    两者的差就是最大子数组和。
"""

if __name__ == "__main__":
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [-2, -1]
    solution = Solution()
    res = solution.maxSubArray(nums)
    print(res)
    pass
