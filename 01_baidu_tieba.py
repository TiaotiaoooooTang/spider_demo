import requests

"""百度评书贴吧"""
# url = 'https://tieba.baidu.com/f?kw=评书'
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
# response = requests.get(url, headers = headers)
# with open('baidu_tieba_pingshu.html','w') as f:
#     f.write(response.content.decode('utf8'))

class Tieba(object):
    def __init__(self,name,pn):
        self.name = name
        self.url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn='.format(name)
        self.url_list = [self.url + str(x*50) for x in range(pn)]
        # print(self.url_list)
        # for x in range(pn):
        #     self.url + str(x * 50)
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
        }

    def get_data(self,url):
        response = requests.get(url, headers=self.headers)
        text = response.content.decode('utf8')
        return text

    def save_data(self,data,index):
        base_path = sys.path[0] + '/html/'
        file_name = self.name + str(index) + '.html'
        with open(base_path + file_name,'w') as f:
            f.write(data)

    def run(self):
        for url in self.url_list:
            data = self.get_data(url)
            index = self.url_list.index(url)
            self.save_data(data,index)
import sys
print(sys.path[0] + '/html/')
if __name__ == '__main__':
    name = sys.argv[1]
    pn = int(sys.argv[2])
    tieba = Tieba(name,pn)
    tieba.run()






