from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_product = []
        r_product = []
        l_product_num = 1
        r_product_num = 1
        for i in range(len(nums)):
            l_product_num *= nums[i]
            r_product_num *= nums[len(nums) - 1 - i]
            l_product.append(l_product_num)
            r_product.append(r_product_num)
        r_product.reverse()
        res_list = []
        for i in range(len(nums)):
            if i <= 0:
                cur_product = r_product[i+1]
            elif 0 < i and i < len(nums) - 1:
                cur_product = l_product[i-1] * r_product[i+1]
            else:
                cur_product = l_product[i-1]
            res_list.append(cur_product)
            pass

        print(f"l_product: {l_product}")
        print(f"r_product: {r_product}")
        return res_list
        
"""
前缀的乘积 + 后缀乘积

"""
if __name__ == "__main__":
    # nums = [1,2,3,4]
    # nums = [-1,1,0,-3,3]
    nums = [4,3,2,1,2]
    solution = Solution()
    res = solution.productExceptSelf(nums)
    print(res)
    pass
