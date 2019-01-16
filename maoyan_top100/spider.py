import requests
from requests.exceptions import RequestException
import re
import json
from multiprocessing import Pool


# 获取单页面内容
def get_one_page(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


# 解析单页面内容
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>'
                         + '.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">'
                         + '(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'release_time': item[4].strip()[5:],
            'star': item[5] + item[6]
        }


# 将结果写入文件
def write_to_file(contents):
    with open('maoyan_top100.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(contents, ensure_ascii=False) + '\n')


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    response = get_one_page(url)
    for item in parse_one_page(response):
        write_to_file(item)


if __name__ == '__main__':
    pool = Pool()
    # 多进程运行
    pool.map(main, [i * 10 for i in range(10)])
