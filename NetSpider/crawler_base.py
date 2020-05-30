
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class crawler_base:
    until = ec.presence_of_element_located((By.ID, param))

    def __init__(self, until):
        self.browser = webdriver.Firefox()
        # 浏览器
        self.wait = WebDriverWait(self.browser, 1000)
        # 窗体大小1920, 1080
        self.browser.set_window_size(1920, 1080)

    def getResponse(self, url: str, param, times: int = 3):
        """
        请求url, 根据返回的html解析为一个doc
        :param url: 请求的url
        :param param: 代表返回成功的标志
        :return: a single element/document
        """
        self.browser.get(url)

        target = self.wait.until(self.until)
        if times > 0:
            self.scrollToEnd(target, times)
        html = self.browser.page_source
        return html

    def scrollToEnd(self, target, times=3):
        """
        """
        for i in range(times):
            try:
                self.browser.execute_script("window.scrollBy(0, 1000)")

                html = self.browser.page_source
                # close login popup if shown

                # browser.execute_script('arguments[0].scrollIntoView(true);', target)
                # target.location_once_scrolled_into_view
            except TimeoutException:
                pass
        return


class movie_crawler(crawler_base):


if __name__ == "__main__":
    pass
