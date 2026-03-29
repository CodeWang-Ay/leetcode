from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        for i in range(len(lists)):
            temp = lists[i]
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

if __name__ == "__main__":
    arr = [4,2,1,3]
    lists = [[1,4,5],[1,3,4],[2,6]]
    head_list = []
    for cur_arr in lists:
        cur_head = create_single_link_by_tail(cur_arr)
        head_list.append(cur_head)
        print_sinle_link(cur_head)
    solution = Solution()

    res = solution.mergeKLists(head_list)
    print_sinle_link(res)

