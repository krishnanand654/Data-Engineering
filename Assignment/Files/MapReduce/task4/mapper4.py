#!/usr/bin/python3
"""mapper3.py"""
import sys

# input comes from standard input
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # If the line is not empty
    if line:
        columns = line.split(',')
        if columns:
            storage_issue = columns[-6].strip()
            product_wg_ton = columns[-1].strip()

            if storage_issue != "storage_issue" and product_wg_ton != "product_wg_ton":
                print('%s,%s' % (storage_issue, product_wg_ton))
