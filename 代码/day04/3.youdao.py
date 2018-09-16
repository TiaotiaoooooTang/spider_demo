import hashlib
import json
import random

import requests
import time


class Youdao(object):
    """
    案例总结：
    1、查找js文件的三种实现形式：数据包对应的初始化文件、标签对应的时间监听、关键字搜索；
    2、在Python代码中模拟页面js实现的加密、编码、随机数、时间戳等功能；
    3、反爬手段：referer和cookie

    """
    def __init__(self,word):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Referer': 'http://fanyi.youdao.com/',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1978658589@119.123.71.44; OUTFOX_SEARCH_USER_ID_NCOO=309666671.88535076; JSESSIONID=aaaFHAdgdzBah_GhJgGvw; ___rl__test__cookies=1535014725969'
        }
        self.word = word
        self.post_data = None
    
    # 生成post请求的表单参数
    def generate_post_data(self):
        """
    S = "fanyideskweb"
    n = 翻译内容
    r = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
    D = "ebSeFb%=XZ%T[KZ)c(sy!"
    o = u.md5(S + n + r + D)

    import hashlib
    sha1/sha256/sha512/md5
        """
        # 生成13位的时间戳
        now_time = int(time.time() * 1000)
        random_num = random.randint(0,9)# 生成0-9随机数
        S = "fanyideskweb"
        n = self.word
        r = str(now_time + random_num)
        D = "ebSeFb%=XZ%T[KZ)c(sy!"
        temp = S + n + r + D
        # 对字符串进行md5编码
        md5 = hashlib.md5()
        md5.update(temp.encode())
        # 转成16进制
        o = md5.hexdigest()

        self.post_data = {
            'i': n,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': r,
            'sign': o,
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTIME',
            'typoResult': False
        }

    def get_data(self):
        resp = requests.post(self.url,headers=self.headers,data=self.post_data)
        return resp.content.decode()

    def parse_data(self,data):
        dict_data = json.loads(data)
        result = dict_data['translateResult'][0][0]['tgt']
        print(result)

    def run(self):
        self.generate_post_data()
        data = self.get_data()
        self.parse_data(data)
    

if __name__ == '__main__':
    import sys
    word = sys.argv[1]
    youdao = Youdao(word)
    youdao.run()



