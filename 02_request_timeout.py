import requests
from retrying import retry

# 设置重复次数
# @retry(stop_max_attempt_number=3)  # 最多尝试三次
# def get_data():
#     print('1111111')
#     requests.get(url)

url = 'http://www.12306.cn/mormhweb/'
response = requests.get(url,timeout=0.005)
print(response.content.decode())   # requests.exceptions.ConnectTimeout: HTTPConnectionPool(host='www.12306.cn', port=80): Max retries exceeded with url: /mormhweb/ (Caused by ConnectTimeoutError(<urllib3.connection.HTTPConnection object at 0x7f72a8e4c7f0>, 'Connection to www.12306.cn timed out. (connect timeout=0.005)'))
