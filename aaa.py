from openpyxl import Workbook
wb=Workbook()
ws=wb.active
ws.title="aaa"
wb.save("sample.xlsx")
wb.close()