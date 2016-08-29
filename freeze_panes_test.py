import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active
sheet.freeze_panes = 'B2'

wb.save('freeze_example.xlsx')
