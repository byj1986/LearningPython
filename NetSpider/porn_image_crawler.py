# coding=utf-8
import os
import re

import lxml.html
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

init_data_url = r'http://cl.liruqi.info/thread0806.php?fid=15'
page_url = r'&search=&page='
response_success_flag = '#ajaxtable'
browser = webdriver.Firefox()
# 浏览器
wait = WebDriverWait(browser, 1000)
# 窗体大小1920, 1080
browser.set_window_size(1920, 1080)

film_name_pattern = re.compile(r'\w{2,4}-?\d{3,5}')
img_postfix_pattern = re.compile(r'(jpg|jpeg|JPG|JPEG)$')


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


def get_porn_images_by_page(page_number):
    for i in range(page_number):
        pn = str(i + 1)
        request_url = init_data_url + page_url + pn
        print('Search page ' + pn + ' url: ' + request_url)
        get_porn_images(request_url, pn)


def get_porn_images(request_url, page_number):
    try:
        doc = parser(request_url, response_success_flag)
        subjects_raw = doc.xpath('//*[@id="ajaxtable"]/tbody[2]/tr/td[2]/h3[1]/a')
        inner_index = 1
        for subject_raw in subjects_raw:
            if subject_raw.text is not None:
                img_name = film_name_pattern.search(subject_raw.text).group()
                if img_name is not None:
                    hyper_link = subject_raw.get('href')
                    new_url = 'http://cl.liruqi.info/' + hyper_link
                    inner_doc = parser(new_url, '#main')
                    image_urls = inner_doc.xpath('//*[@class="tpc_content do_not_catch"]/img/@src')
                    for image_url in image_urls:
                        if img_postfix_pattern.search(image_url):
                            print('正在下载第' + str(inner_index) + '张, 名称' + img_name + ' 地址：' + image_url)
                            inner_index += 1
                            save_image(image_url, page_number, img_name)
                            break
    except Exception as e:
        print(e)


def save_image(image_url, page_number, file_name):
    '''
    :param image_url:
    :param page_number:
    :param file_name:
    :return:
    '''
    try:
        folder_name = str('image\\' + str(page_number))
        if not os.path.exists(folder_name):
            print('创建文件夹...')
            os.makedirs(folder_name)

        r = requests.get(image_url)
        filename = folder_name + '\\' + str(file_name) + '.jpg'
        with open(filename, 'wb') as fo:
            fo.write(r.content)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    get_porn_images_by_page(3)
    # get_porn_images()
    # browser.close()
