from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        self.res = []
        res = []
        self.ancesto_help(root, res)
        p_min_len = float("inf")
        q_min_len = float("inf")
        p_res, q_res = [], []
        for cur_res in self.res:
            if p in cur_res:
                p_min_len = min(p_min_len, len(cur_res))
                if len(cur_res) <= p_min_len:
                    p_res = cur_res
            if q in cur_res:
                q_min_len = min(q_min_len, len(cur_res))
                if len(cur_res) <= q_min_len:
                    q_res = cur_res
        print(f"q_res: {q_res}")
        print(f"p_res: {p_res}")
        common = None
        min_len = min(q_min_len, p_min_len)
        for i in range(min_len):
            if q_res[i] == p_res[i]:
                common = q_res[i]
        
        return common       
    
    def ancesto_help(self, root: Optional[TreeNode], res) -> int:
        if not root:
            return False
        new_res = res[:] + [root]
        self.res.append(new_res)        
        
        self.ancesto_help(root.left, new_res)
        self.ancesto_help(root.right, new_res)

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

def build_binary_tree(nums:List[int], p = 5, q = 1):
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
            if cur_node.left.val == p:
                p_node = cur_node.left
            if cur_node.left.val == q:
                q_node = cur_node.left
            stack.append(cur_node.left)
        i += 1

        # 构建右子树
        if i < len(nums) and nums[i] is not None:
            cur_node.right = TreeNode(nums[i])
            if cur_node.right.val == p:
                p_node = cur_node.right
            if cur_node.right.val == q:
                q_node = cur_node.right
            stack.append(cur_node.right)
        i += 1

    return root, p_node, q_node

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
    nums = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 5
    q = 4
    root, p_node, q_node = build_binary_tree(nums, p, q)
    solution = Solution()
    new_root = solution.lowestCommonAncestor(root, p_node, q_node)
    # res = solution.levelOrder(new_root)
    print(f"直径: {new_root}")

