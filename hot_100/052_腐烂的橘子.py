from typing import Optional, List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row, col= len(grid), len(grid[0])
        min_minute = 0
        queue = deque()
        good_num = 0
        # 1. 将所有的坏橘子加入队列, 统计好橘子的数量
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    good_num += 1

        if good_num == 0:
            return good_num

        # 2. BFS 广度优先遍历 针对每一个坏橘子进行广搜
        while queue:
            for i in range(len(queue)):     # 层序遍历
                x, y = queue.popleft()
                # 四个方向扩散
                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy
                    if 0<= nx < row and 0 <= ny < col and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        good_num -= 1
                        queue.append((nx, ny))

            if queue:
                min_minute += 1
            
            
        # 3. 好橘子 == 0 → 返回时 - 否则返回 -1
        return min_minute if good_num == 0 else -1



"""
题目: 994. 腐烂的橘子
链接: https://leetcode.cn/problems/rotting-oranges/description/?envType=study-plan-v2&envId=top-100-liked
思路:
    # 1. 将所有的坏橘子加入第一层队列, 统计好橘子的数量
    2. BFS 广度优先遍历 针对每一个坏橘子进行广搜
    3. 好橘子 == 0 → 返回时 - 否则返回 -1
"""

if __name__ == "__main__":

    grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    # grid = [[0,2]]
    # grid = [
    #     [2,1,1],
    #     [0,1,1],
    #     [1,0,1]
    # ]
    # grid = [[0,2,2]]
    solution = Solution()
    res = solution.orangesRotting(grid)
    print(f"res: {res}")

