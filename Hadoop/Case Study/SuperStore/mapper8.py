#!/usr/bin/python3
"""mapper6.py"""
from datetime import datetime
import sys


# input comes from standard input
for line in sys.stdin:
    # remove leading and trailing whitespace
    word = line.strip().split(',')
    date = word[10].strip()
    product_line = word[5].strip()
    quantity = word[7].strip()
    if date != "Date" and product_line != "Product line" and quantity != "Quantity":
        day_of_week = datetime.strptime(date, "%m/%d/%Y").strftime("%Y-%U")
        print('%s,%s,%s' % (product_line, day_of_week, quantity))
