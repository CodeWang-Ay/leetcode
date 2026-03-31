from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes_set = set()
        temp = head
        while temp:
            if temp not in nodes_set:
                nodes_set.add(temp)
            else:
                return True             # 说明有环节点
            temp = temp.next
        return False
        
    # 思路1
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
        

def create_cycle_single_link(arr, pos):
    dummy = ListNode(0)
    tail_node = dummy
    cycle_node = None
    for i, cur_num in enumerate(arr):
        tail_node.next = ListNode(cur_num)
        tail_node = tail_node.next
        if i == pos:
            cycle_node = tail_node
    print(f"tail: {tail_node.val}")
    print(f"cycle_node: {cycle_node.val}")
    tail_node.next = cycle_node

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
题目: 141. 环形链表
链接: https://leetcode.cn/problems/linked-list-cycle
思路1(推荐):
    1. 快慢指针, 快2慢1一定会相遇
思路2:
    1. 利用列表存储链表元素的值，判断列表中是否有重复元素

"""
if __name__ == "__main__":
    solution = Solution()
    arr = [3,2,0,-4]
    pos = 1
    head = create_cycle_single_link(arr, pos)
    print_sinle_link(head)
    res = solution.hasCycle(head)
    print(res)