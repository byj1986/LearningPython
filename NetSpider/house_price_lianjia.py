# coding=utf-8
import lxml.html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

init_data_url = r'http://sh.lianjia.com/ershoufang/'

browser = webdriver.Firefox()
# 浏览器
wait = WebDriverWait(browser, 1000)
# 窗体大小1920, 1080
browser.set_window_size(1920, 1080)


def parser(url, param):
    '''
    请求url, 根据返回的html解析为一个doc
    :param url: 请求的url
    :param param: 代表返回成功的标志
    :return: a single element/document
    '''
    browser.get(url)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, param)))
    html = browser.page_source
    doc = lxml.html.fromstring(html)
    return doc


def get_house_prices():
    try:
        doc = parser(init_data_url, '#js-filter-wrapper')

    except Exception as e:
        print(e)


if __name__ == '__main__':
    print()
    # browser.close()
