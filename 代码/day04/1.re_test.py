import re
# 正则：
# 字符：.匹配除换行符以外的任意字符 \转义字符 []列表中某个
# 字符集:\d数值 \D包含空格 \s空白字符 \S \w(a-zA-Z0-9_) \W
# 量词:+ 一个或任意个 * 0个或任意个 ？0个或1个非贪婪 {n}n个

# data = 'a\nb'
# print(re.findall('a\nb',data)) # ['a\nb']
# print(re.findall('a.b',data)) # []
# # 匹配换行符，升级.的功能
# print(re.findall('a.b',data,re.DOTALL)) # ['a\nb']
# 相当于DOTALL模式的简写格式
# print(re.findall('a.b',data,re.S)) # ['a\nb']

# 转义字符:\?\*\+
# 'a\nb==3'
# data = 'a\nb'
# print(len(data)) # 长度3
#
# # r'a\nb==a\\nb'==4
# data = r'a\nb'
# print(len(data)) #

# 匹配手机号,$结尾、^
# re.match('默认从头开始，不需要^，加上$')
# data = '13012345678000'
# print(re.findall('1[3456789]\d{9}$',data))

# data = 'abc_adc_aec'
# print(re.findall('a[bde]c',data)) # ['abc', 'adc', 'aec']

# 字符集
data = 'asf 234 badsaf 324 sdf 234'
# print(re.findall('\d',data)) # ['2', '3', '4', '3', '2', '4', '2', '3', '4']
# print(re.findall('\d+',data)) # ['234', '324', '234']
# print(re.findall('\d*',data))
# print(re.findall('\D',data))

# print(re.findall('\s',data))
# print(re.findall('\W',data))
# print(re.findall('\S',data))
# print(re.findall('\w',data))

# 使用正则模块调用编译对象，一次编译，多次使用，效率相对较高。
# re.findall()每次只需都要编译，效率相对较低
# part = re.compile('\d+')
# print(part.findall(data))


# 分组：只匹配字符串中的指定内容
# print(re.findall(r"a(.*)bc","a\nbc",re.DOTALL)) # ['\n']
# print(re.findall(r"a(.*)b(c)","a\nbc",re.DOTALL)) # [('\n','c')]

# data = 'hello_顺义_world'



