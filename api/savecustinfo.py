from openpyxl import load_workbook

filename = 'D:\\Python_work\\walnuts_api\\api_test\\resources\\test.xlsx'


def writeExcel(sheetname,custinfo):
    wb = load_workbook(filename)
    ws1 = wb.create_sheet(sheetname)  #默认最后一个
    ws1.append(custinfo)
    wb.save(filename)


def readExcel(sheetname):
    '''读取excel'''
    custinfo = []
    wb = load_workbook(filename)
    sheet = wb[sheetname]
    rows = sheet.max_row
    cols = sheet.max_column
    for c in range(1,cols+1):
        custinfo.append(sheet.cell(1, c).value)
    return custinfo


# if __name__ == "__main__":
    # custinfo = ['司勲絏5','15157970391','610301198703282271','65004414861','922091446']
    # app = writeExcel(custinfo)
    # app = readExcel()
    # print(app[0])

