from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        for i in range(len(nums)):
            if i + 1 not in set_nums:
                return i + 1
        return len(nums) + 1

if __name__ == "__main__":
    # nums = [1,2,0]
    # nums = [3,4,-1,1]
    # nums = [7,8,9,11,12]
    nums = [-1, -2, -3]
    # nums = [1]
    solution = Solution()
    res = solution.firstMissingPositive(nums)
    print(res)
