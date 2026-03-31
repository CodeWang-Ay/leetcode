from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> bool:
        nodes_set = set()
        temp = head
        while temp:
            if temp not in nodes_set:
                nodes_set.add(temp)
            else:
                return temp             # 说明有环节点
            temp = temp.next
        return None
    
    # 思路1 推荐
    def detectCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                p1 = head
                p2 = slow
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1

        return None

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
题目: 142. 环形链表 II
链接: https://leetcode.cn/problems/linked-list-cycle-ii
思路1(推荐): 
    1：快慢指针判断有没有环（同 141 题）
    slow 走 1 步，fast 走 2 步，直到相遇；遇空则无环。
    2：相遇后，一个指针从头、一个从相遇点，同速一步走，再次相遇 = 环入口

思路2:
    1. 利用列表存储链表元素的值，判断列表中是否有重复元素
    直接返回第一个重复的元素
"""
if __name__ == "__main__":
    solution = Solution()
    arr = [3,2,0,-4]
    pos = 1
    head = create_cycle_single_link(arr, pos)
    print_sinle_link(head)
    res = solution.detectCycle(head)
    print(res.val)