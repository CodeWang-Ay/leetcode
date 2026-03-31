from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pre_node = dummy
        # l r 节点都不为空时
        while pre_node.next and pre_node.next.next:
            l_node = pre_node.next
            r_node = pre_node.next.next

            # 交换指针指向
            pre_node.next = r_node
            l_node.next = r_node.next
            r_node.next = l_node

            # 移动pre_node节点
            pre_node = l_node

        return dummy.next

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = head.next
        # 下一个头节点new_head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head
        return new_head

def print_sinle_link(head):
    temp = head
    node_list = []
    res = []
    while temp:
        if temp not in node_list:
            node_list.append(temp)
        else:
            break
        res.append(str(temp.val))
        temp = temp.next
    print(' -> '.join(res))

def create_single_link_by_tail(arr):
    dummy = ListNode(0)
    tail_node = dummy
    for cur_num in arr:
        tail_node.next = ListNode(cur_num)
        tail_node = tail_node.next
    return dummy.next


"""
题目: 24. 两两交换链表中的节点
链接: https://leetcode.cn/problems/swap-nodes-in-pairs
思路:
    思路. 通过三个节点进行计算
    p, l, r, 
    
    p.next -> r
    r.next -> l
    l.next -> next_lnode
    
    p = l
    l = next_lnoe
思路2:
    主要是操作两个头节点， 当前头节点和新的头节点
    思路. 通过递归, 画图比较好理解,   
    1. 新的头节点是当前头节点的下一个节点， 
    2. 头节点指向的是下个需要调换的新的头节点
    3. 新的头节点指向旧的头节点
    newHead = head.next                         
    head.next = self.swapPairs(newHead.next)
    newHead.next = head
"""
if __name__ == "__main__":
    solution = Solution()
    # arr = [1,2,3,4]
    arr = [1,2,3,4, 5, 6]
    # arr = [1]

    head = create_single_link_by_tail(arr)
    print_sinle_link(head)
    merge_head = solution.swapPairs(head)
    print_sinle_link(merge_head)