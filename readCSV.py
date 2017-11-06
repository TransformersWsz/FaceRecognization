import os
import csv

f = open('train.csv','rb')
f_csv = csv.reader(f)
for item in f_csv:
    print item[1]