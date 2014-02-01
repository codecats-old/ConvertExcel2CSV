#!/usr/bin/env python
import sys
sys.path.insert(0, './xlrd-0.9.2')
import xlrd
import csv
import os

filepath = '/home/t/Desktop'
filepathOutput = '/home/t/Desktop/res'

wb = xlrd.open_workbook(os.path.join(filepath, 'branzowa_baza_firm.xlsx'))
size = len(wb.sheet_names())

for i in range(size):
    sheet = wb.sheet_by_index(i)
    fp = open(os.path.join(filepathOutput, 'result' + str(i) + '.csv'), 'wb')
    wr = csv.writer(fp, quoting=csv.QUOTE_ALL)
    for rownum in xrange(sheet.nrows):
          wr.writerow([unicode(val).encode('utf8') for val in sheet.row_values(rownum)])
fp.close()