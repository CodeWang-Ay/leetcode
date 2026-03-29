from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headA_len = self.get_link_len(headA)
        headB_len = self.get_link_len(headB)
        head_ap = headA
        head_bp = headB
        if headA_len > headB_len:
            for i in range(headA_len - headB_len):
                head_ap = head_ap.next
        elif headA_len < headB_len:
            for i in range(headB_len - headA_len):
                head_bp = head_bp.next       
        for i in range(headB_len):
            if head_ap == head_bp:
                return head_bp
            head_bp = head_bp.next
            head_ap = head_ap.next
        return None

    def get_link_len(self, head):
        link_len = 0
        temp = head
        while temp:
            link_len += 1
            temp = temp.next
        return link_len



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


if __name__ == "__main__":
    intersectVal = 8
    listA = [4,1,8,4,5]
    listB = [5,6,1,8,4,5]
    skipA = 2
    skipB = 3
    solution = Solution()
    # headA = create_single_link(listA)
    # traverse_single_link(headA)
    headA, headB = create_public_link(listA, listB, skipA, skipB)
    traverse_single_link(headA)
    traverse_single_link(headB)
    interval_node =  solution.getIntersectionNode(headA, headB)
    print(f"node_val: {interval_node.val}")
    pass
