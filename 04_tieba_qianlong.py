# //li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a 帖子xpath
# //li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a
# # https://tieba.baidu.com/f?kw=%E4%B9%BE%E9%9A%86
# # //*[contains(@id,"post_content")]/img  图片xpath
# # //*[@id,"post_content_121110228429"]/img/@src  下载图片xpath
#
import os

import requests
import sys
from lxml import etree

class Tieba(object):

    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E4%B9%BE%E9%9A%86&fr=search'
        self.headers = {
            # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'

        }
        # base_path = sys.path[0] + '/html/'
        # self.file = open(base_path + 'tieba_qianlong.json','w')

    def get_data(self,url):
        response = requests.get(url,headers=self.headers)
        text = response.content
        # print(text)
        return text

    def parse_data(self,data):
        html = etree.HTML(data)
        # print(html)   <Element html at 0x7f70a6a09c88>
        node_list = html.xpath('//li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a')
        # print(node_list)  [<Element a at 0x7f70a6a09d08>, <Element a at 0x7f70a6a09cc8>,,,,,]

        detail_list = []
        for node in node_list:
            temp = {}
            temp['url'] = 'https://tieba.baidu.com' + node.xpath('./@href')[0]
            temp['title'] = node.xpath('./text()')[0]
            detail_list.append(temp)
        next_url = html.xpath("//a[contains(text(),'下一页')]/@href")
        # print('detail_list:',detail_list)
        return detail_list, next_url

    def parse_detail_data(self,detail_list):
        html = etree.HTML(detail_list)
        image_list = html.xpath('//*[contains(@id,"post_content")]/img/@src')
        # print('image_list:',image_list)
        return image_list

    def save_down_image(self,image_list):
        if not os.path.exists('images'):
            os.makedirs('images')

        for url in image_list:
            image = self.get_data(url)
            file_name = 'images' + '/' + url.split('/')[-1]
            with open(file_name, 'wb') as f:
                f.write(image)

    def run(self):
        url = self.url
        while True:
            data = self.get_data(url)
            data_list, next_url = self.parse_data(data)
            for detail in data_list:
                detail_data = self.get_data(detail['url'])
                image_list = self.parse_detail_data(detail_data)
                self.save_down_image(image_list)
            if next_url == []:
                break
            else:
                url  = 'https:' + next_url[0]

if __name__ == '__main__':
    tieba = Tieba()
    tieba.run()




