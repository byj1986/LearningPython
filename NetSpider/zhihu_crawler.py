# coding=utf-8
# 试验非html形式的url的点击
# 主要是从知乎上随便找一个文章，然后抓取用户的信息


import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


ZhihuQuestionUrl = "https://www.zhihu.com/question/387714111"

WebLoadedParam = "QuestionAnswers-answers"


CommentsAttributes = {
    'class': 'Button ContentItem-action Button--plain Button--withIcon Button--withLabel'}

VoteAttributes = {'class': 'Button VoteButton VoteButton--up'}

# 作者 AuthorInfo-head

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


def getAnswers(soup: BeautifulSoup):
    return soup.findAll('div', attrs={"class": "ContentItem AnswerItem"})


def getComments(soup: BeautifulSoup):
    buttons = soup.findAll('button', CommentsAttributes)
    for button in buttons:
        if button:
            buttonText: str = button.text
            if '条评论' in buttonText:
                print(buttonText)
            elif '赞同' in buttonText:
                print(buttonText)


def getVotes(soup: BeautifulSoup):
    buttons = soup.findAll('button', VoteAttributes)

    for button in buttons:
        if button:
            buttonText: str = button.text
            if '赞同' in buttonText:
                print(buttonText)


if __name__ == "__main__":
    htmlText = getResponse(ZhihuQuestionUrl, WebLoadedParam)
    soup = BeautifulSoup(htmlText, features="lxml")
    # getComments(soup)
    # getVotes(soup)
    # answers = getAnswers(soup)
    # for answer in answers:
    #     getVotes(answer)
    # TODO browser要滚动到底部，直到没有新的回答
    
    print('hello world')
    # print(htmlText)
