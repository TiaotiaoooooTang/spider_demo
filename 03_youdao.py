# http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
"""实现有道翻译"""
import hashlib
import json
import random
import time

import requests


class Youdao(object):
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Referer': 'http://fanyi.youdao.com/',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1978658589@119.123.71.44; OUTFOX_SEARCH_USER_ID_NCOO=309666671.88535076; JSESSIONID=aaaFHAdgdzBah_GhJgGvw; ___rl__test__cookies=1535014725969'

        }
        self.word = word
        self.post_data = None

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
        now_time = int(time.time() * 1000)
        random_num = random.randint(0,9)
        S = 'fanyideskweb'
        n = self.word
        r = str(now_time + random_num)
        D = 'ebSeFb%=XZ%T[KZ)c(sy!'
        temp = S + n + r + D
        md5 = hashlib.md5()
        md5.update(temp.encode())
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
        response = requests.post(self.url, headers=self.headers,data=self.post_data)
        return response.content.decode()

    def pares_data(self,data):
        dict_data = json.loads(data)
        result = dict_data['translateResult'][0][0]['tgt']
        print("'{}'翻译的结果为：{}".format(sys.argv[1],result))

    def run(self):
        self.generate_post_data()
        data = self.get_data()
        self.pares_data(data)

if __name__ == '__main__':
    import sys
    word = sys.argv[1]
    youdao = Youdao()
    youdao.run()