from typing import Optional, List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        row = len(grid)
        col = len(grid[0])

        num_islands = 0
        for i in range(row):
            for j in range(col):
                # 为大陆并且没有被访问过
                if grid[i][j] == "1" and visited[i][j] == 0:
                    self.dfs_help(grid, visited, i, j) 
                    # print(f"visited: {visited}")
                    num_islands += 1

        return num_islands
    
    def dfs_help(self, grid, visted, i, j):
        # 是否越界, 为海洋，或已经访问过
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j]=='0' or visted[i][j]:
            return
        visted[i][j] = 1
        # grid[i][j] = "0"

        # 上下左右遍历
        self.dfs_help(grid, visted, i - 1, j)
        self.dfs_help(grid, visted, i + 1, j)
        self.dfs_help(grid, visted, i, j - 1)
        self.dfs_help(grid, visted, i, j + 1)

    def numIslands(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    queue = deque()
                    queue.append((i, j))        # 根节点入队
                    grid[i][j] = "0"
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in dirs:
                            nx = x + dx
                            ny = y + dy
                            if 0<= nx < m and 0<= ny < n and grid[nx][ny] == "1":
                                queue.append((nx, ny))
                                grid[nx][ny] = "0"
        return res



"""
题目: 200. 岛屿数量
链接: https://leetcode.cn/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-100-liked
思路:
    1. 遍历每个格子
    2. 是陆地且没被访问过 → 岛屿 + 1
    3. DFS 把上下左右相连的陆地都淹成 0（或标记 visited）
        1. 结束条件； 越界，当前为0，或者已经拜访过
        2. visited[i][j] = 1,
        3. 上下左右搜索
思路2: (广度优先搜索)
    遇到陆地 → 入队 → 一圈一圈扩散淹掉
    1. 根节点入队
    2. 出队一个元素入队他所有的元素
    3. 
"""

if __name__ == "__main__":
    grid = [
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0']
    ]
    grid = [
    ['1','0','0','0','0'],
    ['0','0','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
    ]
    solution = Solution()
    res = solution.numIslands(grid)
    print(f"res: {res}")

