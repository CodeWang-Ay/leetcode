from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pre_node = dummy
        lnode = head
        while lnode and lnode.next:
            rnode = lnode.next
            next_lnode = rnode.next

            pre_node.next = rnode
            rnode.next = lnode
            lnode.next = next_lnode

            pre_node = lnode
            lnode = next_lnode

        return dummy.next

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head_node = head.next
        head.next = self.swapPairs(new_head_node.next)
        new_head_node.next = head
        return new_head_node

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
    # arr = [1,2,3,4]
    arr = [1,2,3,4, 5, 6]
    # arr = [1]

    head = create_single_link_by_tail(arr)
    print_sinle_link(head)
    merge_head = solution.swapPairs(head)
    print_sinle_link(merge_head)