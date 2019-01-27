from urllib.parse import urlencode
from requests.exceptions import ConnectionError
import requests

base_url = 'https://weixin.sogou.com/weixin?'
headers = {
    'Cookie': 'IPLOC=CN6501; SUID=26AE76316119940A000000005C4DBD78; SUV=1548598651162534; ABTEST=0|1548598654|v1; SNUID=65ED34724246C3337AECA090432AD64B; weixinIndexVisited=1; JSESSIONID=aaab_qcBlvvGO9sy7O5Hw; uuidName=1d7e17576a3f4c45b437f767d9be5231; ppinf=5|1548602140|1549811740|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MTEyMHx1bmlxbmFtZTowOnxjcnQ6MTA6MTU0ODYwMjE0MHxyZWZuaWNrOjA6fHVzZXJpZDoxNzoxMzczMDMxOTE0QHFxLmNvbXw; pprdig=ODdNUbHHOr1d308dX9QwtxXsakZTktj3U7YGLxDEu99KJ3F9CmDU49usRcu7dD4_4iTarISUMXFgfedGUCuTkeJ1Cz2vNCiPBWktREsAAfj5YtZc1ai4_F3fK3hkffTncDDCb4ylNWNUEY9gyEYhgrGM_7bogrcjVM9LjaoLzTw; sgid=10-39010654-AVxNyxzymnCc4eMdmXpg61Q; ppmdig=154860216500000007f389ede82d4261be0bb1818a6519b0; sct=3',
    'Host': 'weixin.sogou.com',
    'Referer': 'https://weixin.sogou.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

proxy = None


def get_proxy():
    try:
        response = requests.get('http://127.0.0.1:8080/get')
        if response.status_code == 200:
            return response.text
        else:
            return None
    except ConnectionError:
        return None


max_count = 5


def get_html(url, count=1):
    global proxy
    if count >= max_count:
        print('请求此时过多')
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
            print('302------------>ip被封')
            proxy = get_proxy()
            if proxy:
                print('using proxy')
                return get_html(url)
            else:
                print('get proxy failed')
                return None
    except ConnectionError as e:
        print('Error', e.args)
        proxy = get_proxy()
        count += 1
        return get_html(url, count)


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


def main():
    keyword = '风景'
    for page in range(1, 101):
        html = get_index(keyword, page)
        print(html)


if __name__ == '__main__':
    main()
