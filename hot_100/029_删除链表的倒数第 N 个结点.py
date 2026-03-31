from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        link_len = self.get_len(head)
        # 倒数第N个节点 就是正数第link_len - N + 1节点
        target_n = link_len - n
        if target_n == 0:
            return head.next
        temp = head
        for i in range(target_n-1):
            temp = temp.next
        temp.next = temp.next.next

        return head

    def get_len(self, head):
        temp = head
        link_len = 0
        while temp: 
            link_len += 1
            temp = temp.next

        return link_len
    
    # 推荐思路 快慢指针
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy

        for i in range(n + 1):
            fast = fast.next 
        
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
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
题目: 19. 删除链表的倒数第 N 个结点
链接: https://leetcode.cn/problems/remove-nth-node-from-end-of-list
思路:
    1. 先建 dummy 虚拟头（防止删头节点特判）
    2. 快指针先走 n+1 步
    3. 快慢指针再同速往后走
    4. 快走到末尾 null 时，慢指针刚好在「要删节点的前驱」
    5. 直接 slow.next = slow.next.next 跳过节点
为什么 n+1？
要让慢指针停在前驱，才能删掉下一个。
"""
if __name__ == "__main__":
    solution = Solution()
    arr = [1,2,3,4,5]
    # n = 2
    n = 5

    head = create_single_link_by_tail(arr)
    print_sinle_link(head)
    merge_head = solution.removeNthFromEnd(head, n)
    print_sinle_link(merge_head)