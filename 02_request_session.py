"""session实现模拟登录"""
import requests

url = 'http://www.renren.com/PLogin.do'  # form表单
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
}
post_data = {
    # 'email': '18515960409',
    # 'password': 'tl930409',
    'email': '13120120193',
    'password': '123456shengjun'
}

session = requests.Session()
response = session.post(url, data=post_data, headers=headers)
text = response.content.decode()

import re
print(re.findall('风雨',text))
