# import requests
# """获取百度首页html（数据不完整）"""
# url = 'https://www.baidu.com'
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
# response = requests.get(url, headers=headers)
# with open('baidu_shouye.html','w') as f:
#     f.write(response.content.decode('utf8'))
# print(response.request.headers)
#
# # print(response.content.decode('utf8'))


import requests
import sys
"""获取新浪首页html"""
url = 'https://www.sina.com.cn/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
response = requests.get(url, headers=headers)
base_path = sys.path[0] + '/html/'
with open(base_path + 'sina_shouye.html','w') as f:
    f.write(response.content.decode('utf8'))
print(response.request.headers)

# print(response.content.decode('utf8'))