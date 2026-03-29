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
        templ1 = list1
        templ2 = list2
        while templ1 and templ2:
            if templ1.val <= templ2.val:
                tail_node.next = templ1
                tail_node = tail_node.next
                templ1 = templ1.next
            else:
                tail_node.next = templ2
                tail_node = tail_node.next
                templ2 = templ2.next

        while templ1:
            tail_node.next = templ1
            tail_node = tail_node.next
            templ1 = templ1.next
        while templ2:
            tail_node.next = templ2
            tail_node = tail_node.next
            templ2 = templ2.next

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
