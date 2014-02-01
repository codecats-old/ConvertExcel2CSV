#!/usr/bin/env python
import xlrd
import csv
import os
filepath = '/home/t/Desktop'
wb = xlrd.open_workbook(os.path.join(filepath, 'branzowa_baza_firm.xlsx'))
sheet = wb.sheet_by_index(1)
fp = open(os.path.join(filepath, 'result2.csv'), 'wb')
wr = csv.writer(fp, quoting=csv.QUOTE_ALL)
for rownum in xrange(sheet.nrows):
      wr.writerow([unicode(val).encode('utf8') for val in sheet.row_values(rownum)])
fp.close()
