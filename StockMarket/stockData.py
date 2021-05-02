# coding=utf-8

import json
import requests


StockDataHost = 'http://data.eastmoney.com/stockcomment/API'


def getStockDataUrl(stockId: any):
    return f"{StockDataHost}/{stockId}.json"


def getCYWDailyData(stockId: str):
    result = requests.get(getStockDataUrl(stockId))
    data = json.loads(result.text.encode('UTF-8'))
    cywData = getCYW(data)
    return cywData


def getCYW(data):
    return data['ApiResults']['zlkp']['cbjg'][0]


if __name__ == "__main__":
    data = getCYWDailyData(600900)
    print(data)
    # print(dataUrl)
