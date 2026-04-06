from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    dqueue = [root]
    i = 1
    while i < len(nums):
        cur_node = dqueue.pop(0)

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
    # nums = []
    root = build_binary_tree(nums)