from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        l = 0
        while l < len(nums) - k:
            temp_num = nums.pop(0)
            nums.append(temp_num)
            l += 1

        return nums



if __name__ == "__main__":
    # nums = [1,2,3,4,5,6,7]
    # k = 0
    nums = [1,2]
    k = 7
    solution = Solution()
    res = solution.rotate(nums, k)
    print(res)