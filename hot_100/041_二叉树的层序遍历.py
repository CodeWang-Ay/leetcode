from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
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
    while i < len(nums):
        cur_node = stack.pop(0)

        # 构建左子树
        if i < len(nums) and nums[i]:
            cur_node.left = TreeNode(nums[i])
            stack.append(cur_node.left)
        i += 1

        # 构建右子树
        if i < len(nums) and nums[i]:
            cur_node.right = TreeNode(nums[i])
            stack.append(cur_node.right)
        i += 1

    return root

"""
题目: 102. 二叉树的层序遍历
链接: https://leetcode.cn/problems/binary-tree-level-order-traversal
思路:
    思路. 层序遍历
    利用递归
    levels: 存放层序遍历结果  levels[i]: 第i层的遍历结果
    level: 当前深度
    1.确定递归函数的参数和返回值: root 满足条件时 返回值放在levels中
    2.确定终止条件：            
        root 为空
    3.确定单层递归的逻辑:
        判断当前深度(层数)的刚好等于levels列表长度, 说明当前节点是该层从左往右的第一个节点, 新建一个子列表进行存放该层的遍历结果
            levels.append([])
        levels[depth] 第i层的当前节点添加到列表中，
        左右孩子节点继续遍历
"""

if __name__ == "__main__":
    # nums = [1,2,2,3,4,4,3]
    # nums = [1,2,2, None,3, None,3]
    # nums = [1,2,2,2,None,2]
    # nums = [1,2,3,4,5]
    nums = [3, 9, 20, None, None, 15, 7]
    root = build_binary_tree(nums)
    solution = Solution()
    res = solution.levelOrder(root)
    print(f"直径: {res}")

