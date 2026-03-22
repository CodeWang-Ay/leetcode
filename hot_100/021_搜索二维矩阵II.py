from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        min_num = min(m, n)
        target_point = -1
        if matrix[0][0] > target:
            return False
        elif matrix[min_num-1][min_num-1] < target:
            target_point = min_num 
        else:
            for i in range(min_num):
                if matrix[i][i] == target:
                    return True
                elif matrix[i][i] < target:
                    target_point = i + 1

        # 先找到target  在矩阵中的零界点
        print(f'target_point: {target_point}')

        
        for i in range(m):       
            if i < target_point:                            # 上半区 在目标之前的行
                for j in range(target_point, n):            # 列的范围
                    print(f"matrix[i][j] {matrix[i][j]}" )
                    if matrix[i][j] == target:
                        return True
            else:                                           # 下半区 
                print("=" * 100)
                for j in range(target_point):               # 列的范围
                    print(f"matrix[i][j] {matrix[i][j]}" )
                    if matrix[i][j] == target:
                        return True
        return False

    # 方法2 进行行列双指针
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = 0
        col = len(matrix[0]) - 1
        m = len(matrix)
        n = len(matrix[0])
        while row < m and col >=0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        
        return False


"""
矩阵的右上角或左下角是最优的搜索起点，这两个位置的元素具有唯一的大小比较特性，能通过一次比较排除一整行或一整列：
    右上角：是当前行的最大值、当前列的最小值。
    左下角：是当前行的最小值、当前列的最大值。
# 右上角为起点
初始化行为第一行， 列为最后一列
如果指针指等于target 则返回为True
如果指针值小于target 说明指针值需要变大。row += 1
如果指针值大于target 说明指针值需要变小。col -= 1
"""

if __name__ == '__main__':
    solution = Solution()
    # matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22]]        # 3 * 5
    # matrix = [
    #     [1,4,7],
    #     [2,5,8],
    #     [3,6,9],
    #     [10,13,14],
    #     [18,21,23]
    # ]        # 3 * 5
    # matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22]]
    
    # matrix = [
    #     [1, 2, 12],
    #     [3, 4, 13],
    #     [5, 6, 15],
    #     [7, 8, 17],
    #     [9, 11, 19],
    # ]
    matrix = [[-1], [3]]
    # matrix = [[-5]]
    target = -2
    flag = solution.searchMatrix(matrix, target)
    print(flag)
 