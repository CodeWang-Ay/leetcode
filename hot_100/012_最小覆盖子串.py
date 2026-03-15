class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_str = ""
        min_len = len(s)
        require_map = {}
        for t_char in t:
            require_map[t_char] = require_map.get(t_char, 0) + 1

        require_char = len(require_map)
        l = 0
        for r, s_char in enumerate(s):
            # 右指针移动
            if s_char in require_map:
                require_map[s_char] -= 1
                if require_map[s_char] == 0:
                    require_char -= 1
                
            # 左指针移动
            while require_char == 0:
                cur_len = r - l + 1
                if cur_len <= min_len:
                    min_str = s[l:r+1]
                    min_len = cur_len           # 
                
                if s[l] in require_map:
                    require_map[s[l]] += 1
                    if require_map[s[l]] > 0:
                        require_char += 1
                l += 1
        
        return min_str
    
"""

题目: 76. 最小覆盖子串
链接: https://leetcode.cn/problems/minimum-window-substring
思路:
    require_map:  当前s字符串中包含t字符串的情况，如果key对value就说明需要几个才能包含t字符串
    require_char: 表示需要的字符个数 为0表示相等
    注意这里不需要用del key
    1. 利用一个哈希map+滑动窗口
    2. 首先将字符串t的所有字符组成key value的形式, 以及初始化总的字符个数放入require_map中
    3. 然后遍历字符串s, 判断当前字符s[r] 是否在require_map的key中, 如果在则s[r]对应的value-1, 判断value是否为0, 如果为0, 那么require_char可以减1
    4. while 循环判断 判断require_char==0,  [只要一直包含做指针就一直移动，直到不包含了] 
        表示当前滑动窗口包含t字符串, 
        判断当前字符串 [l:i+1]的长度是否小于最小字符长度，如果小于则进行赋值
        判断左指针元素是否在require_map中如果在 value+1, 判断其值是否大于0, 如果大于0则 require_chars += 1, 
            这里一定要判断是否大于0 因为require_map[s[l]]可能是负数， 少这个判断会漏掉情况
        左指针移动，l+= 1
    5. 返回res_str
"""

if __name__ == "__main__":
    # s = "ADOBECODEBANC"
    # t = "ABC"
    s = "A"
    t = "AA"
    solution = Solution()
    res = solution.minWindow(s, t)
    print(res)
    pass
