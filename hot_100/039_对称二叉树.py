from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        flag = self.symmetric_help(root.left, root.right)

        return flag

    def symmetric_help(self, left_node:TreeNode, right_node:TreeNode):
        if not left_node and not right_node:
            return True
        if not left_node and right_node:
            return False
        if left_node and not right_node:
            return False
        if left_node.val != right_node.val:
            return False
        left_flag = self.symmetric_help(left_node.left, right_node.right)
        right_flag = self.symmetric_help(left_node.right, right_node.left)
        return left_flag and right_flag


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
题目: 101. 对称二叉树
链接: https://leetcode.cn/problems/symmetric-tree
思路:
    思路. 
    利用递归
    1.确定递归函数的参数和返回值：p, q 
    2.确定终止条件：            
        如果 p和q都是空节点 则返回True
        如果 有一个不为空一个为空, 或者值不太相等 返回False
    3.确定单层递归的逻辑：      
        q.的左节点和p的右节点进行比较， q的右节点和p的左节点进行比较
"""

if __name__ == "__main__":
    # nums = [1,2,2,3,4,4,3]
    # nums = [1,2,2, None,3, None,3]
    nums = [1,2,2,2,None,2]
    root = build_binary_tree(nums)
    solution = Solution()
    res = solution.isSymmetric(root)
    print(f"反转之前: {res}")

