# f:auto
# t:auto
# w:苹果
# url = http://fy.iciba.com/ajax.php?a=fy
import requests
import json
"""金山翻译post请求"""
class King(object):
    def __init__(self,kw):
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
        }
        self.post_data = {
            'f': 'auto',
            't': 'auto',
            'w': kw
        }

    def get_data(self):
        response = requests.post(self.url,data=self.post_data,headers=self.headers)
        text = response.content.decode()
        return text

    def parse_data(self,data):
        dict_data = json.loads(data)
        # print(dict_data)   # {'status': 1, 'content': {'from': 'zh-CN', 'to': 'en-US', 'out': 'reticent', 'vendor': 'ciba', 'err_no': 0}}
        try:
            result = dict_data['content']['out']
        except:
            result = dict_data['content']['word_mean'][0]
            # print(dict_data['content'])
            # {'ph_en': 'ˈæpl', 'ph_am': 'ˈæpəl',
            #  'ph_en_mp3': 'http://res.iciba.com/resource/amp3/oxford/0/44/29/44297283b5e4b5b0a991213897f0b14a.mp3',
            #  'ph_am_mp3': 'http://res.iciba.com/resource/amp3/1/0/1f/38/1f3870be274f6c49b3e31a0c6728957f.mp3',
            #  'ph_tts_mp3': 'http://res-tts.iciba.com/1/f/3/1f3870be274f6c49b3e31a0c6728957f.mp3',
            #  'word_mean': ['n. 苹果;苹果树;苹果公司;']}

        print("'{}'的翻译结果为：{}".format(sys.argv[1],result))

    def run(self):
        data = self.get_data()
        self.parse_data(data)

import sys

if __name__ == '__main__':
    kw = sys.argv[1]
    king = King(kw)
    king.run()


