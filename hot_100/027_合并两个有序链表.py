from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail_node = dummy
        l1 = list1
        l2 = list2
        while l1 and l2:
            if l1.val <= l2.val:
                tail_node.next = l1
                l1 = l1.next
            else:
                tail_node.next = l2
                l2 = l2.next

            tail_node = tail_node.next

        tail_node.next = l1 if l1 else l2
        return dummy.next

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
题目: 21. 合并两个有序链表
链接: https://leetcode.cn/problems/merge-two-sorted-lists/description
思路:
    1. 利用尾插法
    建一个 dummy 虚拟头结点，用 cur 跟着拼链表
    谁当前节点值小，就先接谁
    剩下没拼完的链表，直接尾巴接上
    tail.next = small_node

    tail = tail
    small_node = small_node.next
"""
if __name__ == "__main__":
    solution = Solution()
    l1 = [1,2,4]
    l2 = [1,3,4]
    pos = 1
    l1head = create_single_link_by_tail(l1)
    l2head = create_single_link_by_tail(l2)
    print_sinle_link(l1head)
    print_sinle_link(l2head)
    merge_head = solution.mergeTwoLists(l1head, l2head)
    print_sinle_link(merge_head)
