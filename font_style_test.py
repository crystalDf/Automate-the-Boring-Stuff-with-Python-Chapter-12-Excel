import openpyxl
from openpyxl.styles import Font
from openpyxl.styles import Style

wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')
italic_24_font = Font(size=24, italic=True)
style_obj = Style(font=italic_24_font)
sheet['A1'].style = style_obj
sheet['A1'] = 'Hello world!'
wb.save('styled.xlsx')
