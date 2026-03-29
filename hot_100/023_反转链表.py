from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # 思路1 利用头插法
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = ListNode(0)
        pre_node = pre_head
        temp = head
        while temp:
            cur_node = ListNode(temp.val)
            cur_node.next = pre_head.next
            pre_head.next = cur_node
            temp = temp.next
        return pre_node.next

    # 思路2 直接操作指针
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_node = None
        cur_node = head
        while cur_node:
            next_node = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node
        
        return pre_node



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
        tail = cur_node
    return pre_node.next, tail

def create_single_link_head_insert(nums):
    """尾插法创建 单链表"""
    pre_head = ListNode(0)
    pre_node = pre_head
    for num in nums:
        cur_node = ListNode(num)
        cur_node.next = pre_head.next
        pre_head.next = cur_node
    return pre_node.next

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


if __name__ == "__main__":

    listA = [1,2,3,4,5]
    solution = Solution()
    # headA, tailA = create_single_link(listA)
    headA, tailA = create_single_link(listA)

    # print(f"listA: {headA.val} tailA: {tailA.val}")
    # print(f"listA: {headA.val}")
    # print(traverse_single_link(headA))
    resheadA = solution.reverseList(headA)
    print(traverse_single_link(resheadA))


