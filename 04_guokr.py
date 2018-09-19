# https://www.guokr.com/ask/highlight/
# <a href="/ask/highlight/?page=2">下一页</a>
# https://www.guokr.com/ask/highlight/?page=2
import json
import re
import requests
import sys

"""爬取果壳网的精彩问答的标题和链接"""

class Guokr(object):

    def __init__(self):
        self.url = 'https://www.guokr.com/ask/highlight/'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        base_path = sys.path[0] + '/html/'
        self.file = open(base_path + 'guokr.json', 'w')

    def get_data(self,url):
        response = requests.get(url, headers=self.headers)
        text = response.content.decode()
        # print(text)
        return text

    # '<h2><a target="_blank" href="(.*?)"></a></h2>'
    def parse_data(self,data):
        results = re.findall('<h2><a target="_blank" href="(.*?)">(.*?)</a></h2>',data)
        data_list = []
        for result in results:
            temp = {}
            temp['title'] = result[-1]
            temp['url'] = result[0]
            data_list.append(temp)
        # 解析下一页链接
        # next_url = re.findall('<a href="(/ask/highlight/\?page=\d+)">下一页</a>',data)
        next_url = re.findall('<a href="(/ask/highlight/\?page=\d+)">下一页</a>',data)
        print(next_url)
        return data_list, next_url
    def save_data(self, data_list):
        for data in data_list:
            json_data = json.dumps(data, ensure_ascii=False) + ',\n'
            self.file.write(json_data)

    def __del__(self):
        self.file.close()

    def run(self):
        url = self.url   # 注意：直接将self.url传入get_data,只会循环取到第一页数据
        while True:
            data = self.get_data(url)
            data_list, next_url = self.parse_data(data)
            self.save_data(data_list)
            if next_url == []:
                break
            else:
                url = 'http://www.guokr.com' + next_url[0]

if __name__ == '__main__':
    guokr = Guokr()
    guokr.run()
