from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        print(sorted_intervals)
        l = 0
        r = 1
        res_list = []
        while r < len(sorted_intervals):
            l_s, l_e = sorted_intervals[l]
            r_s, r_e = sorted_intervals[r]
            if abs(r_e - l_s) > (l_e - l_s) + (r_e - r_s):  # 不需要合并区间
                res_list.append(sorted_intervals[l])
                if r == len(sorted_intervals) - 1:
                    res_list.append(sorted_intervals[r])
            else:                                           # 需要合并区间
                new_merge = [min(l_s, r_s), max(l_e, r_e)]  # 最大区间
                if r == len(sorted_intervals) - 1:
                    res_list.append(new_merge)
                sorted_intervals[r] = new_merge
            l += 1
            r += 1
            print(f"l: {l}, r:{r}")
        
        return res_list

if __name__ == "__main__":
    # intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals = [[4,7]]
    solution = Solution()
    res = solution.merge(intervals)
    print(res)
    pass
