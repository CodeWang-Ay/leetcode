# 从 typing 模块导入 List 类型
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        max_num = 1
        set_nums = set(nums)
        for cur_num in set_nums:
            if cur_num - 1 in set_nums:
                continue
            else:
                count = 1
                while cur_num + 1 in set_nums:
                    count += 1
                    cur_num += 1
            max_num = max(max_num, count)
        return max_num

"""
题目: 128. 最长连续序列
链接: https://leetcode.cn/problems/longest-consecutive-sequence/description
思路:
    1. 去重得到nums_set, 首先要去重 不去重复会超时
    2. 如果当前元素num-1 也在nums_set那么直接跳过 因为这个情况我们已经考虑了
    3. 判断当前元素的下一个元素是否在nums_set中 如果在继续增加遍历(考虑3，就不用考虑4)
"""
if __name__ == "__main__":
    nums = [100,4,200,1,3,2,6,7,8,9,10,11]
    # nums = [0]
    solution = Solution()
    res = solution.longestConsecutive(nums)
    print(res)
    pass
