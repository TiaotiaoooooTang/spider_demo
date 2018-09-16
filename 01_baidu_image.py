import requests
"""获取百度图片"""
url = 'https://www.baidu.com/img/bd_logo1.png'
response = requests.get(url)
with open('baidu_image.png','wb') as f:
    f.write(response.content)

