import openpyxl
from openpyxl.chart import BarChart
from openpyxl.chart import Reference
from openpyxl.chart import Series


wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1, 11):          # create some data in column A
    sheet['A' + str(i)] = i

ref_obj = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)

series_obj = Series(ref_obj, title='First Series')

chart_obj = BarChart()
chart_obj.append(series_obj)
# chart_obj.drawing.top = 50      # set the position
# chart_obj.drawing.left = 100
# chart_obj.drawing.width = 300   # set the size
# chart_obj.drawing.height = 200

sheet.add_chart(chart_obj)

wb.save('sample_chart.xlsx')
