from urllib.parse import urlencode
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq
import requests
import pymongo

client = pymongo.MongoClient('localhost')
db = client['wechat']

base_url = 'https://weixin.sogou.com/weixin?'
headers = {
    'Cookie': 'SUID=26AE76316119940A000000005C4DBD78; SUV=1548598651162534; ABTEST=0|1548598654|v1; weixinIndexVisited=1; PHPSESSID=jic5s9pi0a8ktdcs05cli3atq2; SNUID=0CEFDBCEE4E664653C655914E4682A67; ppinf=5|1548691675|1549901275|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxOTpjbGljayVFNCVCOCVCNmNsYWNrfGNydDoxMDoxNTQ4NjkxNjc1fHJlZm5pY2s6MTk6Y2xpY2slRTQlQjglQjZjbGFja3x1c2VyaWQ6NDQ6bzl0Mmx1Skp2LXRGeXd5M0t0aUJWb1FlRVVXd0B3ZWl4aW4uc29odS5jb218; pprdig=DOb9fHs-kjzWlhboJ5fAraedJF30P3OVi4_MznJWzZHnR60Ey8smIAYRTcX2NvATpzQ_wpBSTpGQb-yXl0oSCvaKJWBlhi2pg9QYLmDF-gT8HDyowC-JOauP_Ozszs_D6DF2kL1r4bzQOeQiqeia8Eun4WQWEiyQeEjjKIZgbyI; sgid=16-39003644-AVxPKNuG5ZNZsFMdhvkwbzk; JSESSIONID=aaa9ya5xLSLlweLvFv6Hw; ppmdig=1548733269000000eeb4586c094dc30bd989444f8ea19890; IPLOC=CN6501; sct=8',
    'Host': 'weixin.sogou.com',
    'Referer': 'https://weixin.sogou.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

proxy_pool_url = 'http://127.0.0.1:8080/get'
proxy = None


def get_proxy():
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None


max_count = 5


def get_html(url, count=1):
    global proxy
    if count >= max_count:
        print('请求次数过多')
        return None
    try:
        if proxy:
            proxies = {
                'http': 'http://' + proxy
            }
            response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            proxy = get_proxy()
            if proxy:
                count += 1
                return get_html(url)
            else:
                print('get proxy failed')
                return None
    except ConnectionError as e:
        print('Error', e.args)
        proxy = get_proxy()
        count += 1
        return get_html(url, count)


def parse_index(html):
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')


def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html


def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None


def parse_detail(atricle):
    doc = pq(atricle)
    title = doc('.rich_media_title').text()
    content = doc('.rich_media_content').text()
    date = doc('.rich_media_meta rich_media_meta_text').text()
    nickname = doc('.profile_nickname').text()
    wechat = doc('.profile_meta_value').text()
    return {
        'title': title,
        'content': content,
        'date': date,
        'nickname': nickname,
        'wechat': wechat
    }


def save_to_db(data):
    if db['article'].update({'title': data['title']}, {'$set': data}, True):
        print('save to Mongo', data['title'])
    else:
        print('save to Mongo failed', data['title'])


def main():
    keyword = '风景'
    for page in range(1, 101):
        html = get_index(keyword, page)
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                article = get_detail(article_url)
                if article:
                    detail = parse_detail(article)
                    save_to_db(detail)


if __name__ == '__main__':
    main()
