"""用cookie判断是否登录人人网"""
# http://www.renren.com/968047958
# Cookie:anonymid=jm4ty0aa-ulps6r; depovince=BJ; _r01_=1; _de=7C29999F6ABEF93417E906AB286F0AF5; ick_login=2cebd873-f58f-4f5a-808a-6ba9f6c1e4a2; ick=c867c9e9-b139-4470-af3b-d1569d4a3907; t=000f5565c8a99a72331788241673bb5d8; societyguester=000f5565c8a99a72331788241673bb5d8; id=968047958; xnsid=1da84186; jebecookies=24316fc6-2a78-42ca-be0d-578ec90fc93e|||||; JSESSIONID=abcL66L_n0A8q6S7awIxw; ver=7.0; loginfrom=null; jebe_key=a4f27e93-7f62-4515-8a31-861e6265353d%7Cce3e23674339d338023d46c6360cea67%7C1537100778549%7C1%7C1537100784795; wp_fold=0
# Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36
# import requests
# """用cookie判斷是否登錄方式一"""
# url = 'http://www.renren.com/968047958'
# headers = {
#     'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
#     'Cookie':'Cookie:anonymid=jm4ty0aa-ulps6r; depovince=BJ; _r01_=1; _de=7C29999F6ABEF93417E906AB286F0AF5; ick_login=2cebd873-f58f-4f5a-808a-6ba9f6c1e4a2; ick=c867c9e9-b139-4470-af3b-d1569d4a3907; t=000f5565c8a99a72331788241673bb5d8; societyguester=000f5565c8a99a72331788241673bb5d8; id=968047958; xnsid=1da84186; jebecookies=24316fc6-2a78-42ca-be0d-578ec90fc93e|||||; JSESSIONID=abcL66L_n0A8q6S7awIxw; ver=7.0; loginfrom=null; jebe_key=a4f27e93-7f62-4515-8a31-861e6265353d%7Cce3e23674339d338023d46c6360cea67%7C1537100778549%7C1%7C1537100784795; wp_fold=0'
#
# }
# response = requests.get(url, headers=headers)
# text = response.content.decode()
# # print(text)
# print(response.status_code)
# import re
# ret = re.findall('新用户60409',text)
# print(ret)


import requests
"""用cookie判斷是否登錄方式二"""
url = 'http://www.renren.com/968047958'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
}
cookies = 'Cookie:anonymid=jm4ty0aa-ulps6r; depovince=BJ; _r01_=1; _de=7C29999F6ABEF93417E906AB286F0AF5; ick_login=2cebd873-f58f-4f5a-808a-6ba9f6c1e4a2; ick=c867c9e9-b139-4470-af3b-d1569d4a3907; t=000f5565c8a99a72331788241673bb5d8; societyguester=000f5565c8a99a72331788241673bb5d8; id=968047958; xnsid=1da84186; jebecookies=24316fc6-2a78-42ca-be0d-578ec90fc93e|||||; JSESSIONID=abcL66L_n0A8q6S7awIxw; ver=7.0; loginfrom=null; jebe_key=a4f27e93-7f62-4515-8a31-861e6265353d%7Cce3e23674339d338023d46c6360cea67%7C1537100778549%7C1%7C1537100784795; wp_fold=0'
cookie = {}
for temp in cookies.split(';'):
    key = temp.split('=')[0]
    value = temp.split('=')[-1]
    cookie[key] = value
print(cookie)

response = requests.get(url, headers=headers, cookies=cookie)
text = response.content.decode()
# print(text)
print(response.status_code)
import re
ret = re.findall('新用户60409',text)
print(ret)