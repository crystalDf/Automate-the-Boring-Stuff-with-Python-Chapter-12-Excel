import openpyxl
from openpyxl.styles import Font
from openpyxl.styles import Style

wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')

italic_24_font = Font(size=24, italic=True)
# style_obj = Style(font=italic_24_font)
# sheet['A1'].style = style_obj
sheet['A1'].font = italic_24_font
sheet['A1'] = 'Hello world!'

wb.save('styled.xlsx')

font_obj1 = Font(name='Times New Roman', bold=True)
# style_obj1 = Style(font=font_obj1)
# sheet['A1'].style = style_obj1
sheet['A1'].font = font_obj1
sheet['A1'] = 'Bold Times New Roman'

font_obj2 = Font(size=24, italic=True)
# style_obj2 = Style(font=font_obj2)
# sheet['B3'].style = style_obj2
sheet['B3'].font = font_obj2
sheet['B3'] = '24 pt Italic'

wb.save('styles.xlsx')
