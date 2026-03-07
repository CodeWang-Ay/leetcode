# 从 typing 模块导入 List 类型
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        total_arrs = []
        for i, cur_str in enumerate(strs):
            cur_arr = [0] * 32
            for cur_char in cur_str:
                cur_arr[ord(cur_char) - 97] += 1
            if cur_arr in total_arrs:
                index = total_arrs.index(cur_arr)
                # print(f"{index}:{cur_str}")
                res[index].append(cur_str)
            else:
                total_arrs.append(cur_arr)
                begin_index = len(total_arrs) - 1
                # print(f"{begin_index}:{cur_str}")
                res.append([])
                res[begin_index].append(cur_str)
                
        # print(total_arrs)
        return res

"""
题目: 49. 字母异位词分组
链接: https://leetcode.cn/problems/group-anagrams
思路:
    利用26个英文字母组成, 然后查看数组的索引,
"""
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    res = solution.groupAnagrams(strs)
    print(ord("a"))
    print(res)
