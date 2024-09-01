#!/usr/bin/python3
"""reducer6.py"""
import sys

d={}

for line in sys.stdin:
    line = line.strip()
    day,total = line.split(',')
    try:
        total = float(total)
    except:
        continue

    if day in d:
        d[day]+=total
    else:
        d[day]=total

data = dict(sorted(d.items(), key = lambda x:x[1], reverse=True))

for k,v in data.items():
    print(k,v)

