import openpyxl
# THINGS TO DO
# if run twice the data gets appended again(even if presesnt before)

wb_1 = openpyxl.load_workbook('Bilal School UDISE Codes.xlsx')
ws_excel = wb_1.active
udise_codes = []
column_a = ws_excel['A']
for cell in column_a:
    udise_codes.append(cell.value)
