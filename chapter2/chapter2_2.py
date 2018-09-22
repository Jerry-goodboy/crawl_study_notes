import json
import requests
from lxml import etree
from requests.exceptions import RequestException
import time


def get_one_page(url):
    """
        这里我们伪造了 User-Agent ，不然猫眼网站是会给我们返回一个 403 跳转的，同时是获取不到内容的。
        同时我们还在 main 函数中构造了 url 的 offset 参数，以达到获取 100 个影评的效果。
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None


# def parse_one_page(html):
#     pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
#                          + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
#                          + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
#     items = re.findall(pattern, html)
#     for item in items:
#         yield {
#             'index': item[0],
#             'image': item[1],
#             'title': item[2],
#             'actor': item[3].strip()[3:],
#             'time': item[4].strip()[5:],
#             'score': item[5] + item[6]
#         }


def parse_one_page(html):
    html = etree.HTML(html)
    nodes = html.xpath('//dl[@class="board-wrapper"]/dd')
    for node in nodes:
        temp = {
            'img': node.xpath('./a/img[2]/@data-src')[0],
            'title': node.xpath('.//p[@class="name"]//text()')[0],
            'star': "".join(node.xpath('.//p[@class="score"]//text()')),
            'releasetime': node.xpath('.//p[@class="releasetime"]//text()')[0],
        }
        yield temp


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
