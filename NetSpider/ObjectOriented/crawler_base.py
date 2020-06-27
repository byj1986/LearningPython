
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class crawler_base:
    until = None
    browser = None
    wait = None

    # WebLoadedParam = None
    # InitialUrl = None

    def __init__(self):
        self.browser = webdriver.Firefox()
        # 窗体大小1920, 1080
        self.browser.set_window_size(1920, 1080)
        # 浏览器
        self.wait = WebDriverWait(self.browser, 1000)

    def getResponse(self, url: str, times: int = 3) -> BeautifulSoup:
        """
        """
        self.browser.get(url)

        self.wait.until(self.until)
        # if times > 0:
        #     self.scrollToEnd(target, times)
        html = self.browser.page_source
        return BeautifulSoup(html, features="lxml")
        # return html

    # def scrollToEnd(self, target, times=3):
    #     """
    #     """
    #     for i in range(times):
    #         try:
    #             self.browser.execute_script("window.scrollBy(0, 1000)")

    #             html = self.browser.page_source
    #             # close login popup if shown

    #             # browser.execute_script('arguments[0].scrollIntoView(true);', target)
    #             # target.location_once_scrolled_into_view
    #         except TimeoutException:
    #             pass
    #     return
