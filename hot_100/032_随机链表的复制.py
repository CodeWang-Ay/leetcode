from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head: 
            return []
        dummy = Node(0)
        tail = dummy

        cur_node = head
        node_map = {}
        node_list = []
        l = 0
        while cur_node:
            node_map[cur_node] = l
            tail.next = Node(cur_node.val)
            tail = tail.next
            cur_node = cur_node.next
            node_list.append(tail)
            l += 1
             

        cur_node = head
        tail = node_list[0]
        while cur_node:
            if cur_node.random: 
                random_index = node_map[cur_node.random]
                tail.random = node_list[random_index]
            else:
                tail.random = None

            cur_node = cur_node.next
            tail = tail.next
        return dummy.next


def print_sinle_link(head):
    temp = head
    random_list = []
    res = []
    while temp:
        res.append(str(temp.val))
        if temp.random:
            random_list.append(str(temp.random.val))
        else:
            random_list.append(str("None"))
        temp = temp.next
    print(' -> '.join(res))
    print(' -> '.join(random_list))


def create_random_link_by_tail(arr):
    dummy = Node(0)
    tail_node = dummy
    node_list = []
    for cur_num in arr:
        tail_node.next = Node(cur_num[0])
        tail_node = tail_node.next
        node_list.append(tail_node)

    temp = dummy.next
    for cur_num in arr:
        random_index = cur_num[-1]
        if random_index != None:
            temp.random = node_list[random_index]
        else:
            temp.random = None
        temp = temp.next

    return dummy.next


"""

"""
if __name__ == "__main__":
    solution = Solution()
    # arr = [1,2,3,4]
    arr = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    # arr = [1, 2, 3, 4]
    k = 3
    head = create_random_link_by_tail(arr)
    print(f"head: {print_sinle_link(head)}")
    res = solution.copyRandomList(head)
    # print_sinle_link(head)
    # res = solution.reverseKGroup(head, k)
    # # res = solution.reverse_link(head, 2)
    print_sinle_link(res)