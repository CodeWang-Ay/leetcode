class DlinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0

        # 虚拟头尾节点，简化边界操作
        self.dummy_head = DlinkedNode(0)
        self.dummy_tail = DlinkedNode(0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:            # 如果不在，则添加
            new_node = DlinkedNode(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            self.size += 1
            # 判断容量是否当前缓存容量是否超出范围
            if self.size > self.capacity:
                del_node = self._remove_tail_node()
                del self.cache[del_node.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)
        
    
    # 1. 添加到节点头部
    def _add_node(self, node:DlinkedNode):
        node.prev = self.dummy_head
        node.next = self.dummy_head.next

        # 这个顺序不能错
        self.dummy_head.next.prev = node
        self.dummy_head.next = node
        
    # 2. 删除指定节点
    def _remove_node(self, node: DlinkedNode):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # 3. 删除尾部节点
    def _remove_tail_node(self):
        delete_node = self.dummy_tail.prev
        self._remove_node(delete_node)
        return delete_node
    
    # 4. 移动一个节点到头部
    def _move_to_head(self, node:DlinkedNode):
        self._remove_node(node)
        self._add_node(node)
    

def print_sinle_link(head):
    temp = head
    res = []
    while temp:
        res.append(str(temp.value))
        temp = temp.next
    print(' -> '.join(res))


if __name__ == "__main__":
    lRUCache = LRUCache(2)
    print_sinle_link(lRUCache.dummy_head.next)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    print_sinle_link(lRUCache.dummy_head.next)
    lRUCache.get(1)
    lRUCache.put(3, 3)
    lRUCache.get(2)  
    lRUCache.put(4, 4)
    lRUCache.get(1)
    lRUCache.get(3)
    lRUCache.get(4)
