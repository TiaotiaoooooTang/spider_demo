import requests
"""url带参数的请求"""
url = 'https://www.baidu.com/s?'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
kw = {'wd':'python'}
response = requests.get(url, headers= headers, params=kw)
print(response.url)
with open('baidu_params.html','w') as f:
    f.write(response.content.decode('utf8'))
