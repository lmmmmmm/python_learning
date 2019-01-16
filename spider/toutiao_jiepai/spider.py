import json
import os
import random
import time
import requests
import re
import pymongo
from urllib.parse import urlencode
from requests.exceptions import RequestException
from hashlib import md5
from multiprocessing import Pool

client = pymongo.MongoClient('localhost', connect=False)
db = client['toutiao']

proxies = {'http': 'http://127.0.0.1:8123', 'https': 'http://127.0.0.1:8123'}

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


# 获取页面中每一页中的内容
def get_one_page_index(offset, keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 3,
        'from': 'gallery',
        'pd': ''
    }
    url = 'http://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url, headers=header, proxies=proxies)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("页面请求失败!")
        return None


def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def get_page_detail(url):
    try:
        response = requests.get(url, headers=header, proxies=proxies)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("页面请求失败!", url)
    sleep_time = random.randint(1, 3)
    time.sleep(sleep_time)


def parse_page_detail(html):
    pattern = re.compile('BASE_DATA.galleryInfo.*?title:.*?\'(.*?)\',.*?gallery: JSON.parse\("(.*?)"\),', re.S)
    result = re.search(pattern, html)
    if result:
        title = result.group(1)
        r = result.group(2).replace('\\', '')
        data = json.loads(r)
        if data and len(data.get('sub_images')) > 0:
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            # for image in images:
            # download_image(image)
            return {
                'images': images,
                'title': title
            }


def save_to_mongo(result):
    if db['toutiao_jiepai'].insert(result):
        print('保存到mongodb成功!', result)
        return True
    return False


# response.text 返还结果,response.content 返还二进制
def download_image(url):
    print('正在下载', url)
    try:
        response = requests.get(url, headers=header, proxies=proxies)
        if response.status_code == 200:
            save_image(response.content)
        return None
    except RequestException:
        print("请求图片失败!", url)
    sleep_time = random.randint(1, 3)
    time.sleep(sleep_time)


def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)


def main(offset):
    html = get_one_page_index(offset, '街拍')
    for url in parse_page_index(html):
        if url is not None and not url.endswith('html'):
            html = get_page_detail(url)
            if html:
                result = parse_page_detail(html)
                if result:
                    save_to_mongo(result)


if __name__ == '__main__':
    groups = [x * 20 for x in range(1, 20)]
    pool = Pool()
    pool.map(main, groups)
