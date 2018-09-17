"""cookiejar对象和dict的相互转化"""
import requests

url = 'https://www.baidu.com'

response = requests.get(url)
cookie = response.cookies
print(cookie)

# cookies-->cookiejar
dict_ck = requests.utils.dict_from_cookiejar(cookie)
print(dict_ck)
# cookiejar-->cookies
cookie_jar = requests.utils.cookiejar_from_dict(dict_ck)
print(cookie_jar)