# 从 typing 模块导入 List 类型
from typing import List
class Solution:

    # 方法1 (推荐)
    def trap(self, height: List[int]) -> int:

        # 从左往右数
        l = 0                   # 左指针，初始在数组最左端
        r = len(height) - 1     # 右指针，初始在数组最右端
        l_max = 0               # 左指针左侧的最大高度
        r_max = 0               # 右指针右侧的最大高度
        res_rain = 0            # 存储接雨水的总量

        while l < r:
            # 左指针位置的高度 <= 右指针位置的高度，处理左指针
            if height[l] <= height[r]:
                if height[l] >= l_max:  # 如果当前左指针高度 >= left_max，更新left_max（无法存水）
                    l_max = height[l]
                else:                   # 否则，计算当前位置能存的水量
                    res_rain += l_max - height[l]
                l += 1
            else:
                if height[r] >= r_max:
                    r_max = height[r]
                else:
                    res_rain += r_max - height[r]
                r -= 1
        return res_rain


    # 方法2 (自己想的)
    def trap(self, height: List[int]) -> int:

        # 从左往右数
        left_rain = self.caclu_rain(height)
        right_rain = self.caclu_rain(height[::-1])

        max_num = max(height)
        print(max_num)
        first_index = height.index(max_num)
        last_index = len(height) - 1 - height[::-1].index(max_num)
        overlap_rain = 0
        for cur_rain in height[first_index:last_index]:
            overlap_rain += max_num - cur_rain

        return left_rain + right_rain - overlap_rain

    def caclu_rain(self, height):
        l = 0
        r = 1
        sum_rain = 0
        while l < r and r <= len(height) - 1:
            if height[l] <= height[r]:
                print(l, r)
                cur_low = min(height[l], height[r])
                for cur_num in height[l+1:r]:
                    sum_rain += (cur_low - cur_num)
                l = r
                cur_right_num = height[r]
                if r < len(height) - 1:
                    r += 1
                while r <= len(height) - 1 and cur_right_num > height[r]:
                    r += 1
            else:                                   # 此时需要向右移动
                r += 1
        return sum_rain


"""

思路1(推荐):
    双指针法核心思路
    雨水能存储的条件：当前位置的左右两侧都有更高的柱子，存水量 = min (左侧最高高度，右侧最高高度) - 当前高度。
    双指针从两端向中间移动：
    维护 left_max（左指针左侧的最大高度）和 right_max（右指针右侧的最大高度）。
    每次移动高度较小的一侧指针（因为存水量由较低的一侧决定）。
    若当前指针位置的高度 < 对应侧的最大高度，说明能存水；否则更新最大高度。

思路2: 
    1. 初始化左右指针都为0, 1, 右指针找到第一个比左指针的数字的索引
    2. 移动到第一个比他大的数字，然后计算l, r之间的可以接住的雨水面积， 从左从右各来一次，让后减掉重复的面积即可

"""
if __name__ == "__main__":
    # height = [0,1,0,2,1,0,1,3,2,1,2,3]
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # height = [4,2,0,3,2,5]
    solution = Solution()
    res = solution.trap(height)
    print(res)
    pass
