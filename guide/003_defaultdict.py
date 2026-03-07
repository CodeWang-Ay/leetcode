from collections import defaultdict

# 1. defaultdict(list)：默认值为空列表（最常用）
dd_list = defaultdict(list)
dd_list["fruit"].append("apple")    # 无"fruit"键 → 自动创建空列表，再追加元素
print(dd_list)                      # defaultdict(list, {'fruit': ['apple']})

# 2. defaultdict(int)：默认值为0（常用于计数）
dd_int = defaultdict(int)
dd_int["count"] += 1            # 无"count"键 → 自动设为0，再加1
print(dd_int)                   # defaultdict(int, {'count': 1})
print(dd_int["test"])           # 输出一个没有的值 默认为1

# 3. defaultdict(set)：默认值为空集合（去重场景）
dd_set = defaultdict(set)
dd_set["nums"].add(1)
dd_set["nums"].add(1)           # 集合自动去重
print(dd_set)                   # defaultdict(set, {'nums': {1}})