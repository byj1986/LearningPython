# coding=utf-8
import lxml.html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

# pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com pakegename
data_url = r'http://www.boc.cn/sourcedb/whpj/index.html'
response_success_flag = '#DefaultMain'

# SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
browser = webdriver.Firefox()
# 浏览器
wait = WebDriverWait(browser, 10)
# 窗体大小1920, 1080
browser.set_window_size(1920, 1080)


def parser(url, param):
    """
    请求url, 根据返回的html解析为一个doc
    :param url: 请求的url
    :param param: 代表返回成功的标志
    :return: a single element/document
    """
    browser.get(url)
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, param)))
    html = browser.page_source
    doc = lxml.html.fromstring(html)
    return doc


def get_exchange_data():
    # print('打开主页搜寻链接中...')
    try:
        doc = parser(data_url, response_success_flag)
        option_currency_names = doc.xpath('//*[@id="pjname"]/option/text()')[1:]

        currency_names = doc.xpath('//*[@class="publish"]/div[2]/table/tbody/tr/td[1]/text()')
        for currency_name in currency_names:
            if currency_name in option_currency_names:
                option_currency_names.remove(currency_name)

        # print(option_currency_names)
        currency_exchanges = doc.xpath('//*[@class="publish"]/div[2]/table/tbody/tr/td[3]')
        result_dict = dict()
        index = 0
        for single_currency in currency_names:
            result_dict[single_currency] = currency_exchanges[index].text
            index += 1
        return result_dict
    except Exception as e:
        print(e)


def get_currency_amount(currency_result, source_amount, currency_name):
    # 现钞购入价等于汇率*100
    # 所以计算的时候也*100
    return round((float(source_amount) / float(currency_result[currency_name])) * 100.0, 2)


if __name__ == '__main__':
    currency_result_set = get_exchange_data()
    source_rmb_amount = input('Please input RMB amount: ')
    target_currency_name = input('Please input currency name: ')
    target_currency_amount = get_currency_amount(currency_result_set, source_rmb_amount, target_currency_name)
    print(target_currency_amount)
    browser.close()
