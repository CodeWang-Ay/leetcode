from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_num = self.get_number_by_link(l1)
        l2_num = self.get_number_by_link(l2)
        res_num = l1_num + l2_num
        if res_num == 0:
            return ListNode(0)
        sum_link = []
        while res_num > 0:
            cur_sum = res_num % 10
            sum_link.append(cur_sum)
            res_num //= 10

        dummy = ListNode(0)
        tail_node = dummy
        for cur_num in sum_link:
            tail_node.next = ListNode(cur_num)
            tail_node = tail_node.next
        
        return dummy.next

    def get_number_by_link(self, head: Optional[ListNode]):
        temp = head
        res_num = 0
        l = 0
        while temp:
            res_num += temp.val * (10 ** l)
            # print(f"temp.val: {temp.val}")
            l += 1
            temp = temp.next
        return res_num



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
题目: 2. 两数相加
链接: https://leetcode.cn/problems/add-two-numbers
思路:
    1. 首先将两个链表转化为数字进行相加
    2. 通过相加后的数字依次对10进行取余数然后构建链表
"""
if __name__ == "__main__":
    solution = Solution()
    # l1 = [2,4,3]
    # l2 = [5,6,4]
    # l1 = [0]
    # l2 = [0]
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    l1head = create_single_link_by_tail(l1)
    l2head = create_single_link_by_tail(l2)
    print_sinle_link(l1head)
    print_sinle_link(l2head)
    merge_head = solution.addTwoNumbers(l1head, l2head)
    print_sinle_link(merge_head)
