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

sheet = wb.get_sheet_by_name('Sheet1')

print(sheet['A1'])

print(sheet['A1'].value)

cell = sheet['B1']

print(cell.value)

print('Row' + str(cell.row) + ', Column ' + cell.column + ' is ' + cell.value)
print('Cell ' + cell.coordinate + ' is ' + cell.value)

print(sheet['C1'].value)
