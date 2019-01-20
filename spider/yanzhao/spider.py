import requests
import re
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import pymysql

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

website = 'https://yz.chsi.com.cn'


# 获取内容列表
def get_one_page_index(url):
    try:
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('页面请求出错!')
        return None


# 解析列表中的html
def parse_page_index(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.select('.news-list a')
    time = soup.select('.span-time')[0].string
    pattern = re.compile('href=.*?"(.*?)"', re.S)
    for href in data:
        result = re.search(pattern, str(href))
        url = result.group(1)
        yield {
            'url': website + url,
            'time': time
        }


def get_one_page_detail(url):
    try:
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('内容页请求出错!')
        return None


def parse_page_detail(content, time):
    soup = BeautifulSoup(content, "lxml")
    data = soup.select('#article_dnull')
    title = soup.select('.title-box h2')
    news_time = soup.select('.news-time')
    news_from = soup.select('.news-from')
    if data and len(data) > 0:
        yield {
            'title': title[0].string,
            'news_time': news_time[0].string,
            'news_from': news_from[0].string,
            'in_time': time,
            'content': data[0]
        }


def save_article_to_db(article):
    print('插入mysql数据', article.get('title'))
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='cms')
    title = str(article.get('title'))
    news_time_str = article.get('news_time')
    news_time = str(news_time_str).replace('年', '-').replace('月', '-').replace('日', '')
    source = str(article.get('news_from'))
    cursor = conn.cursor()
    sql = 'insert into cms_news (title,news_time,source,type_id,content) values (%s,%s,%s,%s,%s)'
    cursor.execute(sql, (title, news_time, source, '1', str(article.get('content'))))
    conn.commit()
    cursor.close()
    conn.close


def main(flag, start):
    response = get_one_page_index('https://yz.chsi.com.cn/kyzx/' + str(flag) + '/?start' + str(start))
    if response:
        urls = parse_page_index(response)
        # 列表页面url
        for urlAndtime in urls:
            # 通过列表页面url访问具体的内容
            content = get_one_page_detail(urlAndtime.get('url'))
            # 列表中的时间
            in_time = urlAndtime.get('time')
            if content:
                articles = parse_page_detail(content, in_time)
                for article in articles:
                    save_article_to_db(article)


if __name__ == '__main__':
    main('kydt', 0)
