from typing import Optional, List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. 建图：邻接表
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        # 2. 统计每个节点的入度
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        # 3. 把入度为 0 的节点加入队列
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        # 4. BFS 遍历，每学一门课，后继课程入度 -1
        count_course = 0
        while queue:
            u = queue.popleft()
            count_course += 1

            for v in graph[u]:  # graph[u] 表示v之前一定要学u, u -> v
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        # 5. 最后学过的课程数 == 总课程数 → 无环，返回 True；否则有环，返回 False
        print(f"count_course: {count_course}, numCourses: {numCourses}")
        return count_course == numCourses




"""
题目: 207. 课程表
链接: https://leetcode.cn/problems/course-schedule/description/?envType=study-plan-v2&envId=top-100-liked
思路:
    1. 建图：邻接表
    2. 统计每个节点的入度
    3. 把入度为 0 的节点加入队列
    4. BFS 遍历，每学一门课，后继课程入度 -1
    5. 最后学过的课程数 == 总课程数 → 无环，返回 True；否则有环，返回 False

"""
if __name__ == "__main__":
    numCourses = 2
    # prerequisites = [
    #     [1,0],
    #     [0,1]
    # ]
    prerequisites = [[1,0]]
    solution = Solution()
    res = solution.canFinish(numCourses, prerequisites)
    print(f"res: {res}")

