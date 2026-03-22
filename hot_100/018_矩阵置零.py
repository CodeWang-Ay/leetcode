from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        for i in zero_rows:
            matrix[i] = [0] * len(matrix[0])

        # 列置为0
        for i in range(len(matrix)):
            for j in zero_cols:
                matrix[i][j] = 0
        
        return matrix
            


if __name__ == "__main__":
    # matrix = [[1,1,1],[1,0,1],[1,1,1]]
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solution = Solution()
    res = solution.setZeroes(matrix)
    print(res)
    pass
