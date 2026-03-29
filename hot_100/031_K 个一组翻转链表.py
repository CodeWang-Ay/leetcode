from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pre_node = dummy
        lnode = head
        rnode = head
        for i in range(k-1):
            rnode = rnode.next
        while lnode and rnode:
            next_lnode = rnode.next
            next_rnode = next_lnode
            for i in range(k-1):
                if next_rnode:
                    next_rnode = next_rnode.next
                else:
                    next_rnode = None

            pre_node.next = rnode
            # 反转链表
            self.reverse_link(lnode, k)
            lnode.next = next_lnode

            pre_node = lnode
            lnode = next_lnode
            rnode = next_rnode


        return dummy.next


    def reverse_link(self, head, k):
        pre_node = None
        cur_node = head
        l = 0
        while cur_node and l < k:
            next_node = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node
            l += 1
        return pre_node

    

def print_sinle_link(head):
    temp = head
    node_list = []
    res = []
    while temp:
        # if temp not in node_list:
        #     node_list.append(temp)
        # else:
        #     break
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
    arr = [1, 2, 3, 4, 5]
    # arr = [1, 2, 3, 4]
    k = 3

    head = create_single_link_by_tail(arr)
    print_sinle_link(head)
    res = solution.reverseKGroup(head, k)
    # res = solution.reverse_link(head, 2)
    print_sinle_link(res)