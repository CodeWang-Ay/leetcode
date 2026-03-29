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