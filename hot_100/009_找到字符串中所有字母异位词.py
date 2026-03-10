from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res_list = []
        p_arr = [0] * 26
        for char in p:
            p_arr[ord(char) - 97] += 1

        s_arr = [0] * 26
        s_windows = []
        for char in s[:len(p)]:
            s_arr[ord(char) - 97] += 1
            s_windows.append(char)

        if s_arr == p_arr:
            res_list.append(0)
        
        for r in range(len(p), len(s)):
            pop_char = s_windows.pop(0)
            s_windows.append(s[r])
            s_arr[ord(pop_char) - 97] -= 1
            s_arr[ord(s[r]) - 97] += 1
            if s_arr == p_arr:
                res_list.append(r - len(p) + 1)
        return res_list


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    solution = Solution()
    res = solution.findAnagrams(s, p)
    print(res)
