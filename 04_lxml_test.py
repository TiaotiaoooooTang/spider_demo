# from lxml import etree
#
# temp = '''
#     <div>
#         <ul>
#             <li class="item-1"><a href="link1.html"></a>
#             </li>
#             <li class="item-1"><a href="link2.html">second item</a>
#             </li>
#             <li class="item-inactive"><a href="link3.html">third item</a>
#             </li>
#             <li class="item-1"><a href="link4.html">fourth item</a>
#             </li>
#             <li class="item-0"><a href="link5.html">fifth item</a>
#             </li>
#         </ul>
#     </div>
# '''
# # 实例化etree对象,支持xpath语法
# html = etree.HTML(temp)
#
# node_list = html.xpath('//ul/li/a')
# print(node_list)
#
# # 可以使用try：except；
# # 可以使用if else
# # for node in node_list:
# #     text = node.xpath('./text()')[0] if len(node.xpath('./text()'))>0 else None
# #     href = node.xpath('./@href')[0]
# #     print(text,href)
#
#     # print(dir(node))
#
#
#
# # print(html.xpath('//ul/li/a/text()'))
# # print(html.xpath('//ul/li/a/@href'))
#
# # print(type(html))
# # print(dir(html))
#
# # print(html.xpath('//ul/li'))
# # print(html.xpath('//ul/li[1]'))
# # print(html.xpath('//ul/li[1]')[0])


class Tieba(object):

    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E4%B9%BE%E9%9A%86&fr=search'
        self.headers = {
            # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'
        }

    def get_data(self, url):
        resp = requests.get(url, headers=self.headers)
        return resp.content

    def parse_data(self, data):
        # print(data)
        # 实例化etree对象
        html = etree.HTML(data)
        node_list = html.xpath('//li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a')
        print(node_list)
        return node_list

    def run(self):
        url = self.url

        data = self.get_data(url)
        detail_list = self.parse_data(data)

if __name__ == '__main__':
    tieba = Tieba()
    tieba.run()
