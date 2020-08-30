# coding=utf-8
import json
import openpyxl

from stockData import getCYWDailyData
from datetime import date, datetime, timedelta

xlsFile = r'D:\Projects\Python\LearningPython\StockMarket\股票主力成本.xlsx'
stockJson = r'D:\Projects\Python\LearningPython\StockMarket\stocks.json'


def getCWY(data, dayType: str) -> float:
    return round(data[dayType], 2)


def getTradeDate(data) -> date:
    tradeDate = datetime.strptime(data['TDate'], '%Y-%m-%dT%H:%M:%S')
    return tradeDate.date()


# def getExcelDate(date: str) -> date:
#     return datetime.strftime(date, '%Y-%m-%d %H:%M:%S')


def getExcelSheet(workBook, sheetName):
    sheet = None
    if sheetName in workBook.sheetnames:
        sheet = workBook[sheetName]
    else:
        sheet = workBook.create_sheet(sheetName)
        # TODO Copy from first column in first workSheet
        
    return sheet


if __name__ == "__main__":
    wb = openpyxl.load_workbook(xlsFile)
    dateStyle = wb.worksheets[0].cell(1, 2)._style

    # Step 1: Get Data for yesterday for one stock
    with open(stockJson, 'r', encoding='utf-8') as stockFile:
        stocks = json.load(stockFile)
        for stock in stocks:
            # print(stock)
            cywData = getCYWDailyData(stock['id'])
            # print(cywData)
            tradeDate = getTradeDate(cywData)
            # print(tradeDate.ctime())
            # print(getTradeDate(cywData))
            stockName = cywData['Name']

            sheet = getExcelSheet(wb, stockName)
            columns = sheet.max_column
            rows = sheet.max_row
            rowCount = sheet.rows
            # lastDate = sheet.cell(1, columns).value.date()
            lastDate = None
            if sheet.cell(1, columns).value:
                lastDate = sheet.cell(1, columns).value.date()

            # get last cell of row 1
            # if last cell equals cywData's date, update the cell
            # else create a new column
            columnNumber = columns+1
            if lastDate and lastDate == tradeDate:
                columnNumber = columns
            # print('Column number is ' + str(columnNumber))

            sheet.cell(1, columnNumber).value = tradeDate
            sheet.cell(1, columnNumber).data_type = 'd'
            sheet.cell(1, columnNumber)._style = dateStyle
            zlcb = float(cywData['ZLCB'])
            zlcb20 = float(cywData['ZLCB20R'])
            zlcb60 = float(cywData['ZLCB60R'])
            roundedZlcb = round(zlcb, 2)
            roundedZlcb20 = round(zlcb20, 2)
            roundedZlcb60 = round(zlcb60, 2)
            # print(zlcb, roundedZlcb)

            sheet.cell(2, columnNumber).value = roundedZlcb
            sheet.cell(5, columnNumber).value = roundedZlcb20
            sheet.cell(8, columnNumber).value = roundedZlcb60
            # break
            # print(getCWY(cywData, 'ZLCB20R'))
            # Step 2: put data and update formula in excel
            # print(cywData)

    # Step 3: save excel
    wb.save(xlsFile)
