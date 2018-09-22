# -*- coding:utf8 -*-
import requests
from pyquery import PyQuery as pq


class biqukan():
    """
        此爬虫只获取一章小说内容
    """
    def __init__(self):
        self.url = "http://www.yuetutu.com/18_18147/6422152.html"
        self.path = '漫漫武仙路-第一章.txt'

    def get_text(self, url):
        response = requests.get(url)
        html = response.text
        doc = pq(html)
        title = doc('h1').text()
        text = doc('#content').text()
        yield title + text

    def write(self, texts):
        for text in texts:
            with open(self.path, 'a', encoding='utf-8') as f:
                f.write(text + '\n\n')

    def main(self):
        texts = self.get_text(self.url)
        self.write(texts)


if __name__ == "__main__":
    b = biqukan()
    b.main()
    print("爬取完毕")
