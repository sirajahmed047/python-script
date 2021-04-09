# from os import closerange
# from openpyxl import load_workbook
# import webbrowser
# wb = load_workbook(filename = 'Ansible_Cloudform_doc.xlsx')
# sheet = wb['Sheet1']
# print(sheet['B18'].value)


import xlrd, webbrowser

workbook = xlrd.open_workbook('Ansible_Cloudform_doc.xls')
sheet = workbook.sheet_by_name('Sheet1')

# Suppose your URLs are in column 5, rows 2 to 30
url_column = 1
for row in range(4, 31):
    url = sheet.cell_value(row, url_column)
    webbrowser.open_new_tab(url)

