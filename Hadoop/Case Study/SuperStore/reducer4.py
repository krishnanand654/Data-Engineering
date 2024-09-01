#!/usr/bin/python3
"""reducer4.py"""
import sys

d={}

for line in sys.stdin:
    line = line.strip()
    branch,product_line,quantity = line.split(',')
    if branch in d:
        if product_line in d[branch]:
            d[branch][product_line] += int(quantity)
        else:
            d[branch][product_line] = int(quantity)
    else:
        d[branch]={}

for k,v in d.items():
    if k != "Branch":
        print(f"\n------Branch {k}------")
        if v:
            [print(k,v) for k,v in v.items()]
        else:
            continue
