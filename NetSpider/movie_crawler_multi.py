# coding=utf-8
# 主要目的是从http://www.zhuixinfan.com/main.php
# 这个网页抓取一系列的ed2k或者是磁力链接
# 免去每一集都要手动点开网页复制这样的循环操作
# multi可以同时打开N个网页


import os
import re
import win32
import win32.win32clipboard as w
import lxml.html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


MovieHostUrl = "http://www.zhuixinfan.com/"
InitialMovieUrl = "http://www.zhuixinfan.com/viewtvplay-921.html"
WebLoadedParam = "nv_main"

# Step1: 找到table

browser = webdriver.Firefox()
# 浏览器
wait = WebDriverWait(browser, 1000)
# 窗体大小1920, 1080
browser.set_window_size(1920, 1080)


def getResponse(url, param):
    """
    请求url, 根据返回的html解析为一个doc
    :param url: 请求的url
    :param param: 代表返回成功的标志
    :return: a single element/document
    """
    browser.get(url)
    wait.until(ec.presence_of_element_located((By.ID, param)))
    html = browser.page_source
    return html


def validateHref(href: str):
    return href and "main.php?" in href


def getDownloadUrl(soup: BeautifulSoup):
    downloadUrl = None
    dds = soup.find_all('dd', attrs={"id": "emule_url"})
    for dd in dds:
        downloadUrl = dd.text
    return downloadUrl


def getEpisodeUrls(soup: BeautifulSoup):
    resourceUrls = []
    tds = soup.find_all('td')
    for td in tds:
        href = td.a and td.a["href"]
        if validateHref(href):
            resourceUrls.append(MovieHostUrl+href)
    return resourceUrls


if __name__ == "__main__":
    html = getResponse(InitialMovieUrl, WebLoadedParam)
    soup = BeautifulSoup(html, features="lxml")
    resourceUrls = getEpisodeUrls(soup)
    clipBoardText = ""
    w.OpenClipboard()
    for resource in resourceUrls:
        js = 'window.open("%s")' % resource
        browser.execute_script(js)
    wait.until(ec.number_of_windows_to_be(len(resourceUrls)+1))
    for handle in browser.window_handles:
        browser.switch_to.window(handle)
        wait.until(ec.presence_of_element_located((By.ID, WebLoadedParam)))
        resourceSoup = BeautifulSoup(browser.page_source, features="lxml")
        downloadUrl = getDownloadUrl(resourceSoup)
        if downloadUrl:
            clipBoardText += downloadUrl+"\n"
    print(clipBoardText)
    w.SetClipboardData(w.CF_UNICODETEXT, clipBoardText)

    # w.OpenClipboard()
    # clipBoardText = ""
    # for resource in resourceUrls:
    #     resourceUrl = MovieHostUrl+resource

    #     resourceHtml = getResponse(resourceUrl, WebLoadedParam)
    #     resourceSoup = BeautifulSoup(resourceHtml, features="lxml")
    #     downloadUrl = getDownloadUrl(resourceSoup)
    #     clipBoardText += downloadUrl+"\n"
    # w.SetClipboardData(win32con.CF_UNICODETEXT, clipBoardText)
    # w.EmptyClipboard()
    # w.CloseClipboard()
