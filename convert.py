#!/usr/bin/env python
import sys
sys.path.insert(0, './xlrd-0.9.2')
import xlrd
import csv
import os

filepath = './input'
filepathOutput = './output'

onlyfiles = [ f for f in os.listdir(filepath) if os.path.isfile(os.path.join(filepath, f)) ]

for it in onlyfiles:
    wb = xlrd.open_workbook(os.path.join(filepath, it))
    size = len(wb.sheet_names())
    
    for i in range(size):
        sheet = wb.sheet_by_index(i)
        if not os.path.exists(filepathOutput + '/' + it):
            os.makedirs(filepathOutput + '/' + it)
        fb = open(os.path.join(filepathOutput + '/' + it, str(i) + '.csv'), 'wb')
        wr = csv.writer(fb, quoting=csv.QUOTE_ALL)
        for rownum in xrange(sheet.nrows):
            wr.writerow([unicode(val).encode('utf8') for val in sheet.row_values(rownum)])
    fb.close()
