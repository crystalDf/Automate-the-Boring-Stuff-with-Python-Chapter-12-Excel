import openpyxl

# wb_formulas = openpyxl.load_workbook('writeFormula.xlsx')
# sheet = wb_formulas.active
# print(sheet['A3'].value)

wb_data_only = openpyxl.load_workbook('writeFormula.xlsx', data_only=True)
sheet = wb_data_only.active
print(sheet['A3'].value)
