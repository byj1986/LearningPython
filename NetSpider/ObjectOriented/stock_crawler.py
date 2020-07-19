# coding=utf-8

import json
from bs4 import BeautifulSoup
from crawler_base import crawler_base
from datetime import date, datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class stock_crawler(crawler_base):

    until = ec.presence_of_element_located((By.ID, "page"))
    HostUrl = "http://data.eastmoney.com/stockcomment/stock/"

    def __init__(self):
        crawler_base.__init__(self)

    def getStockUrl(self, stockId: str) -> str:
        return self.HostUrl+stockId+'.html'

    def getReporttime(self, soup: BeautifulSoup):
        reportDateTime = None
        results = soup.find_all('div', attrs={"class": "panel_more time"})
        if results and len(results) > 0:
            reportDateTime = results[0].text
            # reportDateTime = datetime.strptime(results[0].text, '%Y-%m-%d %H:%M')
        return reportDateTime

    def getScore(self, soup: BeautifulSoup):
        score = None
        results = soup.find_all('div', attrs={"class": "score"})
        if results and len(results) > 0:
            if results[0].h2:
                score = results[0].h2.text
        return score

    def getInstituteControl(self, soup: BeautifulSoup):
        instituteControl = None
        results = soup.find_all('div', attrs={"class": "detail_inner"})
        if results and len(results) > 0:
            instituteControl = results[0].span.text
        return instituteControl

    def getOverall(self, stock):
        soup = self.getResponse(self.getStockUrl(stock["id"]), self.until)
        reportTime = self.getReporttime(soup)
        score = self.getScore(soup)
        instituteControl = self.getInstituteControl(soup)
        return {
            # 'stock': stock,
            'id': stock['id'],
            'name': stock['name'],
            'score': score,
            'instituteControl': instituteControl,
            'report': reportTime,
        }


if __name__ == "__main__":
    stockJson = r'C:\Users\byj19\Desktop\stocks.json'
    with open(stockJson, 'r', encoding='utf-8') as stockFile:
        stocks = json.load(stockFile)
        sc = stock_crawler()
        for stock in stocks:
            overall = sc.getOverall(stock)
            print(overall)
    print('done')