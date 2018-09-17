# https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=android&for_mobile=1&callback=jsonp1&start=0&count=18&loc_id=108288&_=0
# https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=linux&for_mobile=1&callback=jsonp1&start=0&count=18&loc_id=108288&_=1537167399837
# https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=linux&start=0&count=18
import sys
import requests
import json

class Douban(object):

    def __init__(self):
        self.url = 'https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=ios&for_mobile=1&start={}&count=18'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            # 反爬
            'Referer': 'https://m.douban.com/tv/american'

        }
        base_path = sys.path[0] + '/html/'
        # print(base_path)
        self.file = open(base_path + 'douban.json','w')
        self.start = 0

    def get_data(self,url):
        response = requests.get(url,headers=self.headers)
        print(response.status_code)
        text = response.content.decode()
        return text

    def parse_data(self,data):
        dict_data = json.loads(data)
        print(dict_data)
        result = dict_data['subject_collection_items']
        data_list = []
        for tv in result:
            temp = {}
            temp['title'] = tv['title']
            temp['url'] = tv['url']
            data_list.append(temp)
        return data_list

    def save_data(self,data_list):
        for data in data_list:
            json_data = json.dumps(data,ensure_ascii=False) + ',\n'
            self.file.write(json_data)

    def __del__(self):
        self.file.close()

    def run(self):
        while True:
            url = self.url.format(self.start)
            data = self.get_data(url)
            data_list = self.parse_data(data)
            self.save_data(data_list)
            self.start += 18
            if data_list == []:
                break

if __name__ == '__main__':
    douban = Douban()
    douban.run()
