# https://36kr.com/
# https://36kr.com/api/search-column/mainsite?per_page=20&page=2
import requests
import re
import sys
import json

class Kr36(object):
    def __init__(self):
        self.url = 'https://36kr.com/'
        # 加载下一页的url
        self.ajax_url = 'https://36kr.com/api/search-column/mainsite?per_page=20&page={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        self.page = 1
        base_path = sys.path[0] + '/html/'
        self.file = open(base_path + '36kr.json','w')

    def get_data(self,url):
        response = requests.get(url,headers=self.headers)
        text = response.content.decode()
        # print(text)
        return text

    def pares_data(self,data):
        # 使用正则提取script标签中的json数据
        result = re.findall('<script>var props=(.*?)</script>',data)[0]
        result = result.split(',locationnal={"url')[0]
        # with open('36kr.json','w') as f:
        #     f.write(result)
        # print(result)
        dict_data = json.loads(result)
        news_list = dict_data['feedPostsLatest|post']
        data_list = []
        for news in news_list:
            temp = {}
            temp['title'] = news['title']
            temp['summary'] = news['summary']
            temp['cover'] = news['cover']
            data_list.append(temp)
        return data_list
    def save_data(self,data_list):
        for data in data_list:
            json_data = json.dumps(data,ensure_ascii=False) + ',\n'
            self.file.write(json_data)

    def __del__(self):
        self.file.close()

    def pares_ajax_data(self,data):
        dict_data = json.loads(data)
        news_list = dict_data['data']['items']
        data_list = []
        for news in news_list:
            temp = dict()
            temp['title'] = news['title']
            temp['summary'] = news['summary']
            temp['cover'] = news['cover']
            data_list.append(temp)
        return data_list


    def run(self):
        data = self.get_data(self.url)
        data_list = self.pares_data(data)
        self.save_data(data_list)

        while True:
            url = self.ajax_url.format(self.page)
            data = self.get_data(url)
            ajax_data_list = self.pares_ajax_data(data)
            self.save_data(ajax_data_list)

            if ajax_data_list == []:
                break
            self.page += 1


if __name__ == '__main__':
    kr36 = Kr36()
    kr36.run()
