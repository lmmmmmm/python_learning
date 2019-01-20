import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--proxy-server=127.0.0.1:8080')

browser = webdriver.Chrome()
username = 'yjlyjl_1'
password = 'ylm101314..'


def search():
    WebDriverWait(browser, 10)
    browser.get('https://www.taobao.com')
    browser.maximize_window()
    input_search = browser.find_element_by_id('q')
    submit = browser.find_element_by_css_selector('#J_TSearchForm > div.search-button > button')
    input_search.send_keys('美食')
    submit.click()
    qr_code = browser.find_element_by_id('J_QRCodeImg')
    if qr_code:
        # 切换到账号密码登录,并登录
        login()


def login():
    browser.find_element_by_id('J_Quick2Static').click()
    time.sleep(6)
    browser.find_element_by_id('TPL_username_1').send_keys(username)
    time.sleep(6)
    browser.find_element_by_id('TPL_password_1').send_keys(password)
    if browser.find_element_by_id('nc_1_n1z'):
        unlock()
    time.sleep(6)
    browser.find_element_by_id('J_SubmitStatic').click()


def unlock():
    bar_element = browser.find_element_by_id('nc_1_n1z')
    ActionChains(browser).drag_and_drop_by_offset(bar_element, 257, 0).perform()


def main():
    search()


if __name__ == '__main__':
    main()
