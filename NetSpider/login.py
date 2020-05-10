# coding=utf-8
# 尝试从百度登录


import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

BaiduUrl = "https://www.baidu.com/"

username = "byj1986@163.com"
password = "abcdef1"

WebLoadedParam = "wrapper"
LoginButton = "tj_login"
LoginPopupWindow = "TANGRAM__PSP_4__foreground"
UsernameButton = "TANGRAM__PSP_10__footerULoginBtn"
UsernameInput = "TANGRAM__PSP_10__userName"
PasswordInput = "TANGRAM__PSP_10__password"
LoginSubmit = "TANGRAM__PSP_10__submit"

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


if __name__ == "__main__":
    htmlText = getResponse(BaiduUrl, WebLoadedParam)
    loginPopup = browser.find_elements_by_name(LoginButton)[1]
    print(loginPopup)
    if loginPopup:
        loginPopup.click()
        wait.until(ec.presence_of_element_located((By.ID, LoginPopupWindow)))
        userLogin = browser.find_elements_by_id(UsernameButton)[0]
        if userLogin:
            userLogin.click()
            userInput = browser.find_elements_by_id(UsernameInput)[0]
            userInput.send_keys(username)

            pwdInput = browser.find_elements_by_id(PasswordInput)[0]
            pwdInput.send_keys(password)
            loginSubmit = browser.find_elements_by_id(LoginSubmit)[0]
            loginSubmit.click()
            # 百度需要手动验证登录，所以自动登录是不行的，但是验证了selenium直接操作dom元素
