"""
已知一个字符串为 “hello_world_yoyo”, 如何得到一个队列 [“hello”,”world”,”yoyo”]
"""

test = 'hello_world_yoyo'
list = test.split('_')
print("练习1结果：%s"% str(list))

"""
有个列表 [“hello”, “world”, “yoyo”]如何把把列表里面的字符串联起来，得到字符串 “hello_world_yoyo”
"""
list2 = ['hello', 'world', 'yoyo']
test2 = "_".join(list2)
print("练习2结果：{}".format(test2))


"""
把字符串 s 中的每个空格替换成”-”
"""
test3 = 'We are happy.'
s=test3.replace(' ','-')
print("练习3结果："+s)
