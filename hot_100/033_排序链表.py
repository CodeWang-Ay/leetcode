from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        nums = []
        temp = head
        while temp:
            nums.append(temp.val)
            temp = temp.next
        print(nums.sort())
        new_head = self.create_single_link_by_tail(nums)
        return new_head
    
    def create_single_link_by_tail(self, arr):
        dummy = ListNode(0)
        tail_node = dummy
        node_list = []
        for cur_num in arr:
            tail_node.next = ListNode(cur_num)
            tail_node = tail_node.next
            node_list.append(tail_node)

        return dummy.next

def print_sinle_link(head):
    temp = head
    res = []
    while temp:
        res.append(str(temp.val))
        temp = temp.next
    print(' -> '.join(res))


def create_single_link_by_tail(arr):
    dummy = ListNode(0)
    tail_node = dummy
    node_list = []
    for cur_num in arr:
        tail_node.next = ListNode(cur_num)
        tail_node = tail_node.next
        node_list.append(tail_node)

    return dummy.next
"""
题目: 148. 排序链表
链接: https://leetcode.cn/problems/sort-list/description
思路:
    思路. 先取数, 排序, 构造新的单链表(消耗空间)
"""
if __name__ == "__main__":
    arr = [4,2,1,3]
    head = create_single_link_by_tail(arr)
    solution = Solution()
    print(print_sinle_link(head))
    res = solution.sortList(head)
    print_sinle_link(res)

