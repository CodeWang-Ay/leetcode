from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return         
        root_val = preorder[0]
        mid = inorder.index(root_val)
        root = TreeNode(root_val)
        # 切割中序数组
        in_left, in_right= inorder[:mid], inorder[mid+1:]
        # 切割前序书序
        pre_left, pre_right = preorder[1:len(in_left)+1], preorder[len(in_left)+1:]
        root.left = self.buildTree(pre_left, in_left)
        root.right = self.buildTree(pre_right, in_right)
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
题目: 543. 二叉树的直径
链接: https://leetcode.cn/problems/invert-binary-tree
思路:
    思路. (知识点还是二叉树的最大深度)
    通过当前节点，判断当前节点中的左右节点的深度，那么经过当前节点的节点个数就是 L + R + 1
    判断直径也就是路程就是节点减去1  self.ans -1
    或者直径直接等于当前左右节点的深度之和 也是可以ac的
    1.确定递归函数的参数和返回值：root
    2.确定终止条件：            
        如果 当前节点为空 那么直接返回0
    3.确定单层递归的逻辑：      
        左节点的深度 L
        右节点的深度 R
        经过当前节点的最长节点数 self.ans = max(self.ans, L + R + 1)
        return max(L, R) + 1
    depth(root)
    retur self.ans -1 
"""

if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    solution = Solution()
    new_root = solution.buildTree(preorder, inorder)
    res = solution.levelOrder(new_root)
    print(f"直径: {res}")

