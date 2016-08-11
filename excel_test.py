import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))

print(wb.get_sheet_names())

sheet = wb.get_sheet_by_name('Sheet3')
print(sheet)

print(type(sheet))

print(sheet.title)

another_sheet = wb.active

print(another_sheet)
