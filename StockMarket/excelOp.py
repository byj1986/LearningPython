# coding=utf-8
import json
import openpyxl

from stockData import getCYWDailyData
from datetime import date, datetime, timedelta

xlsFile = r'股票主力成本1.xlsx'
stockJson = r'C:\Users\byj19\Desktop\stocks.json'


def getCWY(data, dayType: str) -> float:
    return round(data[dayType], 2)


def getTradeDate(data) -> date:
    tradeDate = datetime.strptime(data['TDate'], '%Y-%m-%dT%H:%M:%S')
    return tradeDate.date


def getExcelSheet(workBook, sheetName):
    try:
        sheet = workBook[sheetName]
    except KeyError:
        wb.create_sheet(sheetName)
    return sheet


if __name__ == "__main__":
    wb = openpyxl.load_workbook(xlsFile)
    # print(wb.sheetnames)

    # Step 1: Get Data for yesterday for one stock
    with open(stockJson, 'r', encoding='utf-8') as stockFile:
        stocks = json.load(stockFile)
        for stock in stocks:
            cywData = getCYWDailyData(stock['id'])
            # print(cywData)
            stockName = cywData['Code']

            sheet = getExcelSheet(wb, stockName)
            sheet.merge_cells['A1']
            print(sheet.merged_cells.add())
            # sheet[A1]
            # print(sheet)
            # print(sheet.columns)
            # print(wb.sheetnames)
            # wb.sheetnames
            # print(getCWY(cywData, 'ZLCB20R'))
            # Step 2: put data and update formula in excel
            # print(cywData)

    # Step 3: save excel
    # wb.save(xlsFile)
