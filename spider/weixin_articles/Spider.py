from urllib.parse import urlencode
from requests.exceptions import ConnectionError
import requests

base_url = 'https://weixin.sogou.com/weixin?'
headers = {
    'Cookie': 'SUID=26AE76316119940A000000005C4DBD78; SUV=1548598651162534; ABTEST=0|1548598654|v1; SNUID=65ED34724246C3337AECA090432AD64B; weixinIndexVisited=1; IPLOC=US; ppinf=5|1548689836|1549899436|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxOTpjbGljayVFNCVCOCVCNmNsYWNrfGNydDoxMDoxNTQ4Njg5ODM2fHJlZm5pY2s6MTk6Y2xpY2slRTQlQjglQjZjbGFja3x1c2VyaWQ6NDQ6bzl0Mmx1Skp2LXRGeXd5M0t0aUJWb1FlRVVXd0B3ZWl4aW4uc29odS5jb218; pprdig=lF6ouCd55Ha4-kcUSYCmmRbGzGewzGG9BvQpVUAGzW1uOuu8RHSdURrnFtNDuigmbmW7DIk1eRnqq0TxCPqBLRSy-v581B-SGYVYZxt2nOnhB_gWLA-6bYTcUwYUegQ06b7SgRYSZioZuPm8ekWoiLuo9omYnjXllKBnC8_Dh7Y; sgid=16-39003644-AVxPIaxzqf8DuFWnCyYAuMU; ppmdig=15486898390000009fd8f1f0809c8bea879a838b47a539df; sct=5',
    'Host': 'weixin.sogou.com',
    'Referer': 'https://weixin.sogou.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

proxy_pool_url = 'http://172.0.0.1:8080/get'
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
    print("当前请求代理", proxy)
    print("当前请求次数", count)
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
            print('302------------>ip被封')
            proxy = get_proxy()
            if proxy:
                print('using proxy', proxy)
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
