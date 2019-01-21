import requests
from bs4 import BeautifulSoup

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def get_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = str(response.content, 'utf-8')
        return html


def write_to_file(content):
    print(type(content))
    fileObject = open('data.txt', 'w')
    for c in content:
        fileObject.write(c.text)
        fileObject.write('\n')


def generate_word_cloud():
    f = open(u'data.txt').read()
    wordCloud = WordCloud(background_color="white", font_path='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc',
                          width=1000, height=860, margin=2).generate(f)
    wordCloud.to_file("test.png")
    print('生成词云成功!')


def main(url):
    content = get_content(url)
    soup = BeautifulSoup(content, "lxml")
    html = soup.select('d')
    print(type(html))
    write_to_file(html)


if __name__ == '__main__':
    main('http://comment.bilibili.com/71986702.xml')
    generate_word_cloud()
