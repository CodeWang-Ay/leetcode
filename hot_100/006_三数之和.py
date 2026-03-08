# 从 typing 模块导入 List 类型
from typing import List
class Solution:
    # 方法1
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res_list = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:                                # 针对i 去重
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if cur_sum > 0:
                    r -= 1
                elif cur_sum < 0:
                    l += 1
                else:
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    res_list.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
            
        return res_list
    # 方法2
    # def threeSum(self, nums: list[int]) -> list[list[int]]:
        
    #     res_list = []
    #     sort_nums = sorted(nums)
    #     for i in range(0, len(nums) - 2):
    #         if i > 0 and sort_nums[i] == sort_nums[i-1]:                                # 针对i 去重
    #             continue

    #         l = i + 1
    #         r = len(sort_nums) - 1
            
    #         while l < r:
    #             while l < r and sort_nums[i] + sort_nums[l] + sort_nums[r] < 0:
    #                 l += 1

    #             while l < r and sort_nums[i] + sort_nums[l] + sort_nums[r] > 0:
    #                 r -= 1
                
    #             if sort_nums[i] + sort_nums[l] + sort_nums[r] == 0 and l < r:
    #                 res_list.append([sort_nums[i], sort_nums[l], sort_nums[r]])
    #                 while l < r and sort_nums[i] + sort_nums[l] + sort_nums[r] == 0:    # 针对l, r起到去重作用。如果同时l += 1, r -= 1 就会把好的也去掉
    #                     l += 1
    #                     # r -= 1
    #     return res_list
"""
题目: 15. 三数之和
链接: https://leetcode.cn/problems/3sum
思路:
    1. 先对nums进行排序,然后就是去重 i 范围取值为[0:len(nums)-2)
    2. 然后利用双指针 l = i + 1 r = len(nums) - 1, sum = nums[i] + nums[l] + nums[r]
    sum < 0 l += 1  sum > 0 r -= 1 如果 sum == 0 添加当前列表 
    (只有一个while循环, 里面是if)
    i 去重部分: i > 0 and nums[i] == nums[i-1] continue
    l, r去重，通过while去重， 判断和是否大于0，利用if判断
    注意:
    注意这里不需要判断lst是否在res_list中  否则会超时
"""
if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    # nums = [0, 0, 0]
    # nums = [1,2,0,1,0,0,0,0]
    solution = Solution()
    res = solution.threeSum(nums)
    print(res)
    pass

        