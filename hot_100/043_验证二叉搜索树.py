from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inoder_res = []
        self.inorder_help(root, inoder_res)
        sort_res = sorted(inoder_res)
        return inoder_res == sort_res and len(inoder_res) == len(set(inoder_res))
        
    def inorder_help(self, root:TreeNode, res):          
        if not root:
            return

        self.inorder_help(root.left, res)
        res.append(root.val)
        self.inorder_help(root.right, res)

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
题目: 98. 验证二叉搜索树
链接: https://leetcode.cn/problems/validate-binary-search-tree
思路:
    思路. 注意这里要严格大于。等于是不算的 不能存在重复元素
    搜索树的特性: 二叉搜索树他中序遍历是有序的
    首先利用中序遍历得到遍历结果，然后根据遍历结果判断该数组是否是有序的
    如果是有序则返回True否则返回False
    可能存在更优解
"""

if __name__ == "__main__":
    nums = [2,1,3]
    root = build_binary_tree(nums)
    solution = Solution()
    res = solution.isValidBST(root)
    print(f"直径: {res}")

