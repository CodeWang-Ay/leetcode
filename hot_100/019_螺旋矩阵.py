from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_top = 0
        row_down = len(matrix) - 1
        col_l = 0
        col_r = len(matrix[0]) - 1
        res_list = []
        N = len(matrix[0]) * len(matrix)
        while len(res_list) < N:
            for i in range(col_l, col_r+1):             # 行固定，从左向右遍历
                if len(res_list) < N:
                    res_list.append(matrix[row_top][i])
            row_top += 1

            for i in range(row_top, row_down+1):
                if len(res_list) < N:
                    res_list.append(matrix[i][col_r])
            col_r -= 1
            
            for i in range(col_r, col_l-1, -1):
                if len(res_list) < N:
                    res_list.append(matrix[row_down][i])
            row_down -= 1

            for i in range(row_down, row_top-1, -1):
                if len(res_list) < N:
                    res_list.append(matrix[i][col_l])
            col_l += 1
            
        return res_list


if __name__ == "__main__":
    solution = Solution()
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    res = solution.spiralOrder(matrix)
    print(res)

