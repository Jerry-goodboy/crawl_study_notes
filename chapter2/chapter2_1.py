# -*- coding:utf8 -*-
import requests
from pyquery import PyQuery as pq


class biqukan():
    """
        此爬虫是在获取一章小说的基础上，添加获取所有章节 url 的方法获取全本小说。
    """
    def __init__(self):
        self.url = "http://www.yuetutu.com/18_18147/"
        self.path = '漫漫武仙路.txt'

    def get_index(self, url):
        html = requests.get(url).text
        doc = pq(html)
        links = doc('.listmain a')
        for link in links.items():
            yield link.attr.href

    def parse_url(self, index):
        for link in index:
            yield self.url + link[10:]

    def get_text(self, urls):
        for url in urls:
            html = requests.get(url).text
            doc = pq(html)
            title = doc('h1').text()
            text = doc('#content').text()
            yield title + text

    def write(self, texts):
        for text in texts:
            with open(self.path, 'a', encoding='utf-8') as f:
                f.write(text + '\n\n')

    def main(self):
        index = self.get_index(self.url)
        urls = self.parse_url(index)
        texts = self.get_text(urls)
        self.write(texts)


if __name__ == "__main__":
    b = biqukan()
    print("正在获取网页，请稍等片刻：......")
    b.main()
    print("爬取完毕")
