from queue import Queue

import requests
from lxml import etree

url = 'http://www.czvv.com/huangye/'


class Chuanzong(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }

    def get_kind_url(self,kind_que):
        req = requests.get(url, headers=self.headers)
        req.encoding = 'utf-8'
        html = req.text

        tree = etree.HTML(html)
        kinds_url = tree.xpath('//div[@class="left"]//div[@class="center"]/ul/li/a/@href')
        for urls in kinds_url:
            print(urls)
            kind_que.put(urls)
            print(len(kinds_url))

    def parse_kind_url(self,kind_que):
        while True:
            kind_url = kind_que.get()
            print("还剩余:",kind_que.qsize())
            req = requests.get(kind_url,headers=self.headers)
            req.encoding='utf-8'
            html = req.text
            
            tree = etree.HTML(html)
            print(kind_url)
            contact_url = tree.xpath('//*[@id="Thebox"]/div/div[3]/div[1]/div/div[1]/a/@href')
            for url in contact_url:
                print(url)

kind_queue = Queue()
chuan = Chuanzong()
chuan.get_kind_url(kind_queue)
chuan.parse_kind_url(kind_queue)
