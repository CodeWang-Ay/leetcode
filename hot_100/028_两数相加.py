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

    # 思路2 推荐
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """利用尾插法进行操作。 进位操作"""
        dummy = ListNode(0)
        tail_node = dummy
        carry = 0           # 进位的标志
        while l1 or l2 or carry:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0

            total = l1_value + l2_value + carry
            carry = total // 10                     # 是否有进位

            tail_node.next = ListNode(total % 10)   # 先加入个位数
            
            tail_node = tail_node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
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
题目: 2. 两数相加
链接: https://leetcode.cn/problems/add-two-numbers
思路:
    1. 用 dummy 虚拟头节点 存结果链表 [尾插法]
    2. 用 carry 进位 记录满十进一
    3. 同时遍历两个链表：
        逐位相加 = l1.val + l2.val + 进位
        当前位：总和 % 10
        更新进位：总和 // 10
    4. 链表走完，最后进位不为 0，要多补一个节点
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
