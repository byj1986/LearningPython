# coding=utf-8
# 试验非html形式的url的点击
# 主要是从知乎上随便找一个文章，然后抓取用户的信息


import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


ZhihuQuestionUrl = "https://www.zhihu.com/question/387714111"

if __name__ == "__main__":
    pass