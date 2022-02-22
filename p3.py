"""
题目:输入一个字符串str, 输出第m个只出现过n次的字符，
如在字符串 gbgkkdehh 中,找出第2个只出现1 次的字符，输出结果：d

"""
list = []


def test1(str):
    for i in str:

        num = str.count(i, 0, len(str))
        if num == 1:
            list.append(i)
    print("题目1：" + list[1])


str = 'gbgkkdehh'
test1(str)

"""
判断字符串a=”welcome to my world” 是否包含单词b=”world”
包含返回True，不包含返回 False
"""


def test2():
    message = 'welcome to my world'
    world = 'world'

    if world in message:
        return True
    return False


print(f"题目2：%s" % test2())

"""
输出指定字符串A在字符串B中第一次出现的位置,如果B中不包含A,则输出-1
从 0 开始计数
A = “hello”
B = “hi how are you hello world, hello yoyo !”
"""


def test3():
    A = "hello1"
    B = "hi how are you hello world, hello yoyo !"
    cc = B.find(A)
    print(cc)

