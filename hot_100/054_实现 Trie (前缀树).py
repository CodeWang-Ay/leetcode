from typing import Optional, List
from collections import deque

class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # 26个小写字母
        self.is_end = False           # 是否是单词结尾

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not node.children[idx]:                  # 如果当前字符为空
                node.children[idx] = TrieNode()
            node = node.children[idx]                   # 指针移动
        node.is_end = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            idx = ord(char) - ord("a")
            if not node.children[idx]:                  # 如果当前为空
                return False
            node = node.children[idx]

        return node.is_end                          # 最后一个一定要是is_end 为True
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            idx = ord(char) - ord("a")
            if not node.children[idx]:                  # 如果当前为空
                return False
            node = node.children[idx]
        return True                                     # 最后一个是不是is_end不重要


"""
题目: 208. 实现 Trie (前缀树)
链接: https://leetcode.cn/problems/implement-trie-prefix-tree/description/?envType=study-plan-v2&envId=top-100-liked
思路:
Trie 本质是一棵多叉树，每个节点：
    - 有 26 个字母子节点
    - 一个标记 is_end，表示是否是单词结尾
支持三个操作：
    1. insert：插入单词，沿着树走，没有就新建节点
        1. 获取字符， 判断是否为None, 为None则新建节点
        2. 指针移动。node = node.children
        3. node.is_end = True
    2. search：查整个单词是否存在
        1. 获取字符， 判断是否为None, 为None则返回False
        2. 指针移动。node = node.children
        3. 返回最后指针 node.is_end , 因为是要检查是否存在而不是前缀
    3. startsWith：查是否有字符串以该前缀开头
        1. 获取字符， 判断是否为None, 为None则返回False
        2. 指针移动。node = node.children
        3. 返回True

"""
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.search("apple")   
    trie.search("app")    
    trie.startsWith("app") 
    trie.insert("app")
    trie.search("app")     

