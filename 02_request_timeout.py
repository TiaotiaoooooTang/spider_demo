import requests
from retrying import retry

url = 'http://www.12306.cn/mormhweb/'
response = requests.get(url,timeout=0.5)
print(response.content.decode())