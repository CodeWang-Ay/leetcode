from collections import defaultdict

class Solution:

    # 方法1 滑动窗口
    def lengthOfLongestSubstring(self, s: str) -> int:
        windows = []
        max_len = 0
        for char in s:
            if char not in windows:
                windows.append(char)
                max_len = max(max_len, len(windows))
            else:
                while windows and char in windows:
                    windows.pop(0)      # 移动左指针
                windows.append(char)
                max_len = max(max_len, len(windows))

        return max_len
    
    # 方法2 hash_map 加快慢指针
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     l = 0
    #     max_len = 0
    #     char_map = defaultdict(int)
    #     for r, char in enumerate(s):
    #         if char not in char_map:
    #             char_map[char] += 1
    #             max_len = max(max_len, r - l + 1)
    #         else:                               # 准备滑动窗口 滑动左指针
    #             while char in char_map:
    #                 char_map[s[l]] -= 1
    #                 if char_map[s[l]] == 0:
    #                     del char_map[s[l]]
    #                 l += 1
    #             char_map[char] += 1
    #     return max_len

"""
题目: 3. 无重复字符的最长子串
链接: https://leetcode.cn/problems/longest-substring-without-repeating-characters
思路:
    1. 方法1
    关键点: 滑动窗口
    判断当前元素是否在窗口内，如果在则左窗口边界一直向右移动直到当前元素不在窗口中
    如果不在 当前元素加入窗口中，扩大右窗口

    2. 方法2 左右指针 + hashmap
    如果当前元素在map则一直移动左指针直到他不在map中
    
"""
if __name__ == "__main__":
    s = "abcabcbb"
    # s = "pwwkew"
    # s = "bbbbb"
    # s = "aab"
    print([].pop(0))
    solution = Solution()
    res = solution.lengthOfLongestSubstring(s)
    print(res)
    pass
