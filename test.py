#!/usr/bin/env python
import datetime
import os
from datetime import timedelta
from stock import stockImport

sk = stockImport()
#start_date = datetime.date(2016, 12, 20)
#today = datetime.date(2016, 12, 30)
#start_date = datetime.date(2009, 9, 25)
#start_date = datetime.date(2004, 2, 11)


stocks = []
scan_date = datetime.date(2016, 12, 1)
X,Y = sk.loadAllTrainDataByStock("2330", scan_date, 30, 7)
print len(X)
print len(Y)
exit(0)
for root, dirs, files in os.walk("bystock/"):
    for f in files:
        stocks.append(f.split('.')[0])

print stocks
exit(0)
print ("update dataframe from {} to {} ".format(start_date, today))
X = []
Y = []
test_date = datetime.date(2016, 1, 1)
d, r = sk.loadTrainDataByIdFixedRow('2330', test_date, 30, 7)
#print d.tolist()
#print len(d.tolist())
print sum(d.tolist(), [])
#print len(sum(d.tolist(), []))
print r

test_date = datetime.date(2016, 2, 1)
d, r = sk.loadTrainDataByIdFixedRow('2330', test_date, 30, 7)

#print d.tolist()
#print len(d.tolist())
print sum(d.tolist(), [])
#print len(sum(d.tolist(), []))
print r

exit(0)
