from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.build_bst_help(nums, 0, len(nums)-1)
        return root
        
    def build_bst_help(self, nums, left, right):          
        if left > right :
            return
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        
        root.left = self.build_bst_help(nums, left, mid-1)
        root.right = self.build_bst_help(nums, mid+1, right)
        return root

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
题目: 108. 将有序数组转换为二叉搜索树
链接: https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree
思路:
    思路. 
    利用二分查找，一直选中间节点作为根节点就行了
    1.确定递归函数的参数和返回值：nums, l, r
    2.确定终止条件：            
        如果 l > r 直接返回None
    3.确定单层递归的逻辑：      
        得到当前数组的中间节点作为根节点
        根节点的左指针指向 左半部分的中间节点
        根节点的右指针指向 右半部分的中间节点 
        返回根节点
"""

if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    root = build_binary_tree(nums)
    solution = Solution()
    root = solution.sortedArrayToBST(nums)
    res = solution.levelOrder(root)
    print(f"直径: {res}")

