from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 构建一个相交链表
def create_public_link(listA, listB, skipA, skipB):
    public_num = listA[skipA:]
    public_head, public_tail = create_single_link(public_num)
    head_a, tail_a = create_single_link(listA[:skipA])
    head_b, tail_b = create_single_link(listB[:skipB])
    tail_a.next = public_head
    tail_b.next = public_head
    return head_a, head_b

# 创建一个单链表
def create_single_link(nums):
    """尾插法创建 单链表"""
    tail = ListNode(0)
    pre_node = tail
    for num in nums:
        cur_node = ListNode(num)
        tail.next = cur_node
        tail = tail.next
    return pre_node.next, tail

# 遍历单链表
def traverse_single_link(head):
    temp = head
    res_links = []
    link_len = 0
    while temp:
        res_links.append(temp.val)
        temp = temp.next
        link_len += 1
    print(f"遍历链表结果: {res_links}")    
    return res_links, link_len

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
    listB = [5,6,1,8,4,5]
    skipA = 2

    # headA = create_single_link_by_tail(listA)
    headA = create_single_link_by_head(listA)
    headA_arr, headA_len = traverse_single_link(headA)

    print(f"headA_arr: {headA_arr} headA_len:{headA_len}")
    # headA = create_single_link(listA)
    # traverse_single_link(headA)
    # headA, headB = create_public_link(listA, listB, skipA, skipB)
    # traverse_single_link(headA)
    # traverse_single_link(headB)
    # interval_node =  solution.getIntersectionNode(headA, headB)
    # print(f"node_val: {interval_node.val}")
    # pass
