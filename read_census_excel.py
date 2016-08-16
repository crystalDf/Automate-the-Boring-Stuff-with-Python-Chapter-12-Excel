#! python3
# read_census_excel.py - Tabulates population and number of census tracts for
# each county.

import openpyxl
import pprint

print('Opening workbook...')

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
county_data = {}

# TODO: Fill in county_data with each county's population and tracts.
print('Reading rows...')

if __name__ == '__main__':
    for row in range(2, sheet.max_row + 1):
        # Each row in the spreadsheet has data for one census tract.
        state = sheet['B' + str(row)].value
        county = sheet['C' + str(row)].value
        pop = sheet['D' + str(row)].value

# TODO: Open a new text file and write the contents of county_data to it
