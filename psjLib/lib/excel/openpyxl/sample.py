from openpyxl import load_workbook

wb = load_workbook(filename = 'C:\\Users\\ff\\PycharmProjects\\psjLib\\data\\excel\\3.보도포장관리_시스템.xlsm', keep_vba=True)
sheet_ranges = wb['2. 대상컬럼']
print(sheet_ranges['A2'].value)