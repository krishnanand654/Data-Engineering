#!/usr/bin/python3
"""mapper6.py"""
from datetime import datetime
import sys


# input comes from standard input
for line in sys.stdin:
    # remove leading and trailing whitespace
    word = line.strip().split(',')
    date = word[10].strip()
    total = word[9].strip()
    if date != "Date" and total != "Total":
        day_of_week = datetime.strptime(date, "%m/%d/%Y").strftime("%A")
        print('%s,%s' % (day_of_week, word[9]))
