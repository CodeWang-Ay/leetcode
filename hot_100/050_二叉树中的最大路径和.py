from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        self.path_sum(root)
        print(f"max_sum: {self.max_sum}")
        return self.max_sum

    
    def path_sum(self, root: Optional[TreeNode]) -> int:
        """当前节点的为起点的最大路径和"""
        if not root:
            return 0
        
        left_sum = self.path_sum(root.left)
        rgiht_sum = self.path_sum(root.right)
        self.max_sum = max(self.max_sum, root.val, left_sum + rgiht_sum + root.val, rgiht_sum + root.val, left_sum + root.val)
        root_max_sum = max(root.val, rgiht_sum + root.val, left_sum + root.val)
        print(f"sum: {self.max_sum }")              # 经过当前节点的最大路径和 可以左右都走
        print(f"root_max_sum: {root_max_sum}")      # 当前节点的为起点的最大路径和 但是不能左右都走
        return root_max_sum
        

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        self.level_order_help(root, 0, levels)
        return levels
        
    def level_order_help(self, root:TreeNode, depth, levels):          # 获取最大深度不变，但是利用中间值去保存直径的结果
        if not root:
            return
        if depth == len(levels):
            levels.append([])
        
        levels[depth].append(root.val)
        self.level_order_help(root.left, depth + 1, levels)
        self.level_order_help(root.right, depth + 1, levels)

def build_binary_tree(nums:List[int]):
    '''
    从层序遍历数组构建
    通过数组构建二叉树
    1. 用队列保存待分配孩子的节点
    2. 每次取一个节点，分配左、右两个数组元素
    3. 新节点继续入队，保证一层一层往下建
        1. 根节点入队
        2. 对头出队， 每次出队之后还有元素则依次左右孩子赋值并入队, i + 1
    '''
    if len(nums) == 0:
        return None
    root = TreeNode(nums[0])
    stack = [root]
    i = 1
    p_node, q_node = None, None
    while i < len(nums):
        cur_node = stack.pop(0)


        # 构建左子树
        if i < len(nums) and nums[i] is not None:
            cur_node.left = TreeNode(nums[i])
            stack.append(cur_node.left)
        i += 1

        # 构建右子树
        if i < len(nums) and nums[i] is not None:
            cur_node.right = TreeNode(nums[i])
            stack.append(cur_node.right)
        i += 1

    return root, p_node, q_node

"""
题目: 543. 二叉树的直径
链接: https://leetcode.cn/problems/invert-binary-tree
思路:
    1. 当前节点的为起点的最大路径和， 经过当前节点的最大和路径进行分工
"""

if __name__ == "__main__":
    # nums = [1,2,3]
    # nums = [-10, 9, 20, None, None, 15, 7]
    nums = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    # nums = [2, -1]
    # nums = [1,-2,3]
    root, p_node, q_node = build_binary_tree(nums)
    solution = Solution()
    new_root = solution.maxPathSum(root)
    # res = solution.levelOrder(new_root)
    print(f"直径: {new_root}")

