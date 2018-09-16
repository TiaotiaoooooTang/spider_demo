import json
import re
import requests

# 需求：爬取36kr新闻的title、digest、summary、cover
# 流程：
# 1、构建请求信息url和headers
# 2、发送请求，获取响应
# 3、解析响应数据：25行的script标签，使用正则提取数据，分组
# 4、保存新闻数据

class Kr36(object):
    """
    案例总结：
    1、判断响应中是否有数据，不能根据源码的行数。使用搜索关键字
    2、响应中的数据，有脏数据，尝试把数据写入文件，人工查看排错。
    3、正则和json配合使用提取数据；
    4、加载更多页数据是通过ajax进行加载的，但是首页数据是在响应源码中，要区别对待。
3
    """
    def __init__(self):
        self.url = 'https://36kr.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        # 定义下一页的url
        self.ajax_url = 'https://36kr.com/api/search-column/mainsite?per_page=20&page={}'
        self.page = 1

        # 创建文件对象
        self.file = open('news.json','w')

    def get_data(self,url):
        resp = requests.get(url,headers=self.headers)
        return resp.content.decode()

    def parse_data(self,data):
        # 使用正则提取script标签中的json数据
        # <script>var props=(.*?)</script>
        result = re.findall('<script>var props=(.*?)</script>',data)[0]
        # 切割字符串，去除非json数据
        result = result.split(',locationnal={"ur')[0]
        # 把响应直接写入文件
        with open('kr36.json','w')as f:
            f.write(result)

        # 把数据转成字典
        dict_data = json.loads(result)
        # 从响应的字典中提取新闻列表数据
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

    def parse_ajax_data(self,data):
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
        # 1、构建请求信息url和headers
        # 2、发送请求，获取响应
        url = self.url
        data = self.get_data(url)
        # 3、解析响应数据：25行的script标签，使用正则提取数据，分组
        data_list = self.parse_data(data)
        # 4、保存新闻数据
        self.save_data(data_list)
        # 开启循环，加载更多页数据
        while True:
            # 发送ajax请求
            url = self.ajax_url.format(self.page)
            data = self.get_data(url)
            # 解析ajax数据
            ajax_data_list = self.parse_ajax_data(data)
            # 保存数据
            self.save_data(ajax_data_list)

            # 定义循环的终止条件
            if ajax_data_list == []:
                break
            # 页数加1
            self.page += 1


if __name__ == '__main__':
    kr36 = Kr36()
    kr36.run()
