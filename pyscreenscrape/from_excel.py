import openpyxl
# to check if its the right udise code
# to check if it has the details page
# if run twice the data gets appended again(even if presesnt before)

wb_1 = openpyxl.load_workbook('topython.xlsx')
ws_excel = wb_1.active
udise_codes = []
column_a = ws_excel['A']
for cell in column_a:
    udise_codes.append(cell.value)
