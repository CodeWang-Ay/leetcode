from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res_list = []
        double_end_queue = []               # 存的索引
        for i in range(len(nums)):
            # 出队条件
            # 1. 队尾出队 [队列不为空且当前元素大于等于队尾元素时,  队尾出队]
            while double_end_queue and nums[i] > nums[double_end_queue[-1]]:
                double_end_queue.pop(-1)                    # 队尾出队
            # 2. 队头出队 当前队列最大元素不在索引取值范围内时( <= i - k)   i - double_end_queue[0] >= k. 表示不在窗口内
            while double_end_queue and i - double_end_queue[0] >= k:
                double_end_queue.pop(0)
            
            # 入队条件 1. 执行队尾出队条件之后 可以从队尾入队了
            double_end_queue.append(i)
            if i >= k - 1:
                index = double_end_queue[0]
                res_list.append(nums[index])
        
        return res_list

"""
题目: 239. 滑动窗口最大值
链接: https://leetcode.cn/problems/sliding-window-maximum
思路:
    构造一个双端队列q, q存放的是索引列表(递增), 其对应的值递减, q存放当前窗口范围内的有效索引值 
    这里的递增和递减说的从队头开始计算的
    出队条件:
        1. 队列不为空且当前元素大于等于队尾元素时,  队尾出队
        2. 当前队列最大元素不在索引取值范围内时( <= i - k),    队头出队
    入队条件:  只能从队尾进行入队，从队头入队破坏了索引是递增的规则了
        1. 执行出队条件1后 即可从队尾入队
"""
if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    # nums = [1, -1]
    # k = 1
    solution = Solution()
    res = solution.maxSlidingWindow(nums, k)
    print(res)
    pass
