# 一共26哥英文字母
# ord() 函数可以返回单个字符的 Unicode/ASCII 编码值（英文字符的 Unicode 编码和 ASCII 码是一致的），示例：
# chr() 可以把数字转回对应的字符
def str_trans_num(char):
    return ord(char)

def num_trans_str(num):  
    return chr(num)


"""
总结
英文字符不能直接用 int() 转换（会报错），需通过 ord() 转成对应的 ASCII 码（数字）；
ord(字符) 取 ASCII 码，chr(数字) 转回字符，是英文字符和数字互转的核心函数；
算法题中常用 ord(c) - ord('a') 把 'a'-'z' 转成 0-25 的索引，方便计算。
"""
if __name__ == "__main__":
    print(f"a: {ord('a')}")         # 97
    print(f"z: {ord('z')}")         # 122

    print(f"A: {ord('A')}")         # 65
    print(f"Z: {ord('Z')}")         # 90


    print(f"97: {chr(97)}: type{type(chr(97))}")    # str
    print(chr(122))
    print(chr(65))
    print(chr(90))
    pass
