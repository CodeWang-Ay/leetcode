# 从 typing 模块导入 List 类型
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            cur_area = min(height[left], height[right]) * (right - left)
            max_area = max(cur_area, max_area)

        return max_area
        # pass
"""
    1. 每次左右指针只移动到比自己大的节点，比自己小的节点不用比觉
    2. 
"""

if __name__ == "__main__":
    # height = [1,8,6,2,5,4,8,3,7]
    # height = [1,3,2,5,25,24,5]
    height = [1,1]
    solution = Solution()
    res = solution.maxArea(height)
    print(res)
    pass

