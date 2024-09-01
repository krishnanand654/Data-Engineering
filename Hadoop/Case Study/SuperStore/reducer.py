#!/usr/bin/python3
"""reducer.py"""
import sys

dictionary={}

# input comes from STDIN
for line in sys.stdin:

    line = line.strip()
    branch,income= line.split(',')
    try:
        income = float(income)
    except:
        continue

    if branch in dictionary:
        dictionary[branch]+=income
    else:
        dictionary[branch] = income

data = dict(sorted(dictionary.items(), key = lambda x:x[1], reverse = True))	
for key, value in data.items():
    print(key,value)

