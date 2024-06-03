

import xlsxwriter


wb = xlsxwriter.Workbook('first.xlsx')
ws = wb.add_worksheet(name="ONE")

vals = [12, 14, 25, 29, 19, 35]

ws.write_column('A1', vals)
ws.write_row(8, 0, vals)

wb.close()