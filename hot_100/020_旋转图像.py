from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先对角线赋值
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                print(matrix[i][j])
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 然后每一行倒排就行了
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

        return matrix

"""
1. 先写一个对角线赋值
2. 然后遍历每一行， 每一行再进行翻转
"""
        
if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    solution = Solution()
    res = solution.rotate(matrix)
    print(res)
    pass
