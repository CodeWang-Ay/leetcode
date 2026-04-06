from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root
    
    def invert(self, root:TreeNode):
        if not root:
            return 
        root.left, root.right = root.right, root.left
        self.invert(root.left)
        self.invert(root.right)

    def levelsOrder(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels = []
        self.levelshelp(root, 0, levels)
        return levels

    def levelshelp(self, root:TreeNode, level, levels):
        if not root:
            return 
        if level == len(levels):
            levels.append([])
        
        levels[level].append(root.val)
        self.levelshelp(root.left, level + 1, levels)
        self.levelshelp(root.right, level + 1, levels)



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
题目: 94. 二叉树的中序遍历
链接: https://leetcode.cn/problems/binary-tree-inorder-traversal
思路:
    思路. 中序遍历  左中右
    递归三要数:   
    1. 确定参数和返回值  (self, root, res)
    2. 确定终止条件      root = None
    3. 单层递归逻辑:
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)
"""

if __name__ == "__main__":
    # nums = [1, None, 2, 3]
    # nums = [1, 2, 3]
    nums = [4,2,7,1,3,6,9]
    # nums = []
    root = build_binary_tree(nums)
    solution = Solution()
    res = solution.levelsOrder(root)
    print(f"反转之前: {res}")
    invert_root = solution.invertTree(root)
    reinvert_res = solution.levelsOrder(invert_root)
    print(f"反转之后: {reinvert_res}")
