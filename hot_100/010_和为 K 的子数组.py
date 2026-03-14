from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """前缀和 + hash列表"""
        prefix_map = {0:1}
        prefix_sum = 0
        res = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            
            if prefix_sum - k in prefix_map:
                res += prefix_map[prefix_sum - k]

            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return res

"""
题目: 560. 和为 K 的子数组
链接: https://leetcode.cn/problems/subarray-sum-equals-k
思路:
    关键点: 利用前缀和
    cur_sum [0:i]的前缀和 包含i
    sum_map 用于存放当前i之前所有的前缀和. 不包含i
        cur_sum - k是否在 [0:i-1] 的前缀和出现过，
            如果出现过，加上出现的次数
        添加当前[0:i] 的前缀和放入到sum_map字典中

    这种思路是考虑了所有情况的，当前索引为i
    依次考虑的组合是[i-1:i], [i-2:i],...[0:i]的前缀和
    假设子数组的和为k [j:i], 那么直接使用 [0:i] - [0:j-1] == k, 求[0:i] - k = [0:j-1] 求每个前缀和cur_map[[0:i]-k]的个数就行了
    然后总和加起来

    核心公式推导
    设前缀和数组 pre_sum，其中 pre_sum[i] = nums[0] + ... + nums[i-1]（pre_sum [0] = 0）。
        s那么子数组 nums [j...i-1] 的和 = pre_sum [i] - pre_sum [j]。
    我们要找 pre_sum[i] - pre_sum[j] = k → 等价于找 pre_sum[j] = pre_sum[i] - k。
    哈希表的作用
    用哈希表 prefix_map 记录「前缀和值」出现的次数，遍历过程中：
    - 计算当前前缀和 cur_sum；
    - 查哈希表中是否有 cur_sum - k，有则累加对应次数；
    - 将当前 cur_sum 加入哈希表（统计出现次数）。
"""
if __name__ == "__main__":
    # nums = [1,1,1]
    # k = 2
    # nums = [1,2,3]
    # k = 3
    nums = [1]
    k = 0
    solution = Solution()
    res_list = solution.subarraySum(nums, k)
    print(res_list)
    pass
