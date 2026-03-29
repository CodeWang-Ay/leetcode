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

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1

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
    """尾插法创建 返回头节点和尾节点"""
    tail = ListNode(0)
    pre_node = tail
    for num in nums:
        cur_node = ListNode(num)
        tail.next = cur_node
        tail = tail.next
    return pre_node.next, tail

# 遍历单链表
def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(str(cur.val))
        cur = cur.next
    print(" → ".join(res))

"""
题目: 160. 相交链表
链接: https://leetcode.cn/problems/intersection-of-two-linked-lists
思路1 (推荐):
    1. 构造一个获取链表长度的列表
    2. 让长的那个链表先移动  len_a - len_b 位置，使得起点一样
    同起点后每次判断当前元素是否相等, 相等则直接返回
    否则返回为空
思路2:
    两个指针 A 走完自己路→走对方路；B 走完自己路→走对方路👉 最终总路程绝对相等：
        路程 A = A 独有的一段 + 公共相交段 + B 独有的一段
        路程 B = B 独有的一段 + 公共相交段 + A 独有的一段
        a+b+c 完全相等 → 速度一样，必定同时间踩中交点
    没有交点 → 两个指针最后会同时走到 None，循环结束，返回 None，完全没问题。
"""
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
    print_linked_list(headA)
    print_linked_list(headB)
    interval_node =  solution.getIntersectionNode(headA, headB)
    print(f"node_val: {interval_node.val}")
