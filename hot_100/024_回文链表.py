from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        link_nums = []
        temp = head
        while temp:
            link_nums.append(temp.val)
            temp = temp.next
        return link_nums == link_nums[::-1]

def print_sinle_link(head):
    temp = head
    res = []
    while temp:
        res.append(str(temp.val))
        temp = temp.next
    print('->'.join(res))

def create_single_link_by_tail(arr):
    dummy = ListNode()
    tail_node = dummy
    for cur_num in arr:
        tail_node.next = ListNode(cur_num)
        tail_node = tail_node.next
    return dummy.next



"""
题目: 234. 回文链表
链接: https://leetcode.cn/problems/palindrome-linked-list
思路1:
    1. 利用列表存储链表元素的值，然后进行返回判断是否相等

思路2: (待优化)
    1. 快慢指针：找到链表中点
    2. 反转后半部分链表
    3. 前半段 & 反转后的后半段逐节点比对
    4.（可选）复原链表（工程规范）
"""
if __name__ == "__main__":
    solution = Solution()
    arr = [1,2,2,1]
    head = create_single_link_by_tail(arr)
    print_sinle_link(head)
    res = solution.isPalindrome(head)
    print(res)