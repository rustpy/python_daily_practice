import requests
import json
# 接口的url
url = "http://fanyi.baidu.com/v2transapi"

# 接口的参数
params = {
    "from":"en",
    "to":"zh",
    "query": "test"
}

# 发送接口
r = requests.request("post", url, params=params)

# 打印返回结果
print(r.text)

# 其实到上面就已经完了，因为百度不是我自己写的接口，为了让结果看的更加清楚一点，我取来翻译的字段
d = json.loads(r.text)
print(d['liju_result']['tag'])


url = "http://fanyi.baidu.com/v2transapi"
params = {
    "from":"en",
    "to":"zh",
    "query": "student" # 我改了这里
}

r = requests.request("post", url, params=params)

d = json.loads(r.text)
# print(d['liju_result']['tag'])


# 3个数字得加减乘除
basic_math = (123*456 + 300)/100 - 345

# 3个字符串得拼接
str_joint = 'issac' + '.' + 'peng'

# 分辨定义一个单元素得元组和多元素得元组
single_tup = ('a',)
mutply_tup = ('a', 'b', ['A', 'B'])


def tup(tup):
    if len(tup) <= 1:
        print('单元素元组')
    else:
        print('多元素数组')


# 打印一个列表中得元素。尝试将两个列表合并
list1 = [1, 2, 3, 3, 4]
list2 = ['a', 'b', 'c', 'd']
it = iter(list1)
for i in it:
    print(i)
list3 = list1 + list2
list4 = list1.append(list2)
list1[0:0] = list2

# 打印一个字典中得元素。尝试将两个字典合并
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 8, 'e': 7, 'g': 6}
for item in dict1:
    print(item)
for item in dict1.values():
    print(item)
dict3 = {}
dict3.update(dict1)
dict3.update(dict2)
print(dict3)

# 利用集合，将列表[1, 2, 3, 3, 2, 5] 中重复元素去掉
list1 = ["a","a","a","b","b","c","d","d","f"]
temp_list = []
for i in list1:
    if i not in temp_list:
        temp_list.append(i)
print(temp_list)
