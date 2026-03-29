from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 打印链表
def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(str(cur.val))
        cur = cur.next
    print("→".join(res))

# 1. 尾插法构建单链表
def create_single_link_by_tail(arr):
    """
    尾插法构建单链表
    """
    dummy = ListNode(0)                         # 虚拟头结点
    tail_node = dummy
    for cur_num in arr:
        cur_node = ListNode(cur_num)            # 当前待插入的节点
        tail_node.next = cur_node               # 进行插入
        tail_node = tail_node.next              # 尾指针移动
    return dummy.next

# 2. 头插法构建单链表
def create_single_link_by_head(arr):
    """
    头插法构建单链表  dummy 虚拟头节点
    """
    reverse_arr = arr[::-1]                     # 首先反转链表
    dummy = ListNode(0)
    for cur_num in reverse_arr:
        cur_node = ListNode(cur_num)
        cur_node.next = dummy.next
        dummy.next = cur_node
    return dummy.next

if __name__ == "__main__":
    intersectVal = 8
    listA = [4,1,8,4,5]
    headinsert_headA = create_single_link_by_tail(listA)
    tailinsert_headA = create_single_link_by_head(listA)
    print_linked_list(headinsert_headA)
    print_linked_list(tailinsert_headA)