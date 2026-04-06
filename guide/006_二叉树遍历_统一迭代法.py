from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 统一迭代版本  利用栈
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        思路: 利用栈来遍历二叉树
            首次根节点(中间节点)入栈，
            每次出栈一个节点(作为中间节点)，
            出栈节点不为空: 入栈顺序: 右 左 中 null (这样可以保存出栈顺序为中左右)
            出栈节点为空: 继续出栈一个部位空的节点，放入结果集合中
                            res.append(stack.pop().val)
        前序遍历: 中左右
        中序遍历: 左中右
        后序遍历: 左右中
        """
        if not root:
            return []
        
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                if node.right:
                    stack.append(node.right)                
                if node.left:
                    stack.append(node.left)

                stack.append(node)
                stack.append(None)
            else:
                cur_node = stack.pop()
                res.append(cur_node.val)
        return res

    def inorderTraversal(self, root):
        if not root:
            return []
        
        stack = [root]
        res = []
        while len(stack) > 0:
            node = stack.pop()
            if node:

                if node.right:
                    stack.append(node.right)

                stack.append(node)
                stack.append(None)

                if node.left != None:
                    stack.append(node.left)
            else:
                node = stack.pop()
                res.append(node.val)
        return res
    
    def postorderTraversal(self, root):
        """
        利用队列， 和构建二叉树的方法是一样的
        """
        if not root:
            return []
        
        stack = [root]
        res = []
        while len(stack) > 0:
            node = stack.pop()
            if node:
                stack.append(node)
                stack.append(None)

                if node.right:
                    stack.append(node.right)

                if node.left:
                    stack.append(node.left)

            else:
                node = stack.pop()
                res.append(node.val)
        return res
    
    def levelorder(self, root):
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res

    def levelsorder(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []

        queue = deque([root])
        levels = []

        while queue:
            level = []
            cur_level_len = len(queue)
            for _ in range(cur_level_len):
                cur_node = queue.popleft()
                level.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)

                if cur_node.right:
                    queue.append(cur_node.right)
            levels.append(level)

        return levels
    
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
    dqueue = deque([root])
    i = 1
    while i < len(nums):
        cur_node = dqueue.popleft()

        # 构建左子树
        if i < len(nums) and nums[i]:
            cur_node.left = TreeNode(nums[i])
            dqueue.append(cur_node.left)
        i += 1

        # 构建右子树
        if i < len(nums) and nums[i]:
            cur_node.right = TreeNode(nums[i])
            dqueue.append(cur_node.right)
        i += 1

    return root


# 二叉树的遍历
    

if __name__ == '__main__':
    nums = [1,None,2,3]
    nums = [3,9,20,None,None,15,7]
    root = build_binary_tree(nums)
    solution = Solution()
    preOrder_res = solution.preorderTraversal(root)
    print(f"前序遍历: {preOrder_res}")
    inOrder_res = solution.inorderTraversal(root)
    print(f"中序遍历: {inOrder_res}")
    postOrder_res = solution.postorderTraversal(root)
    print(f"后续遍历: {postOrder_res}")
    levelOrder_res = solution.levelorder(root)
    print(f"层序遍历: {levelOrder_res}")
    levelsOrder_res = solution.levelsorder(root)
    print(f"层序遍历分层: {levelsOrder_res}")