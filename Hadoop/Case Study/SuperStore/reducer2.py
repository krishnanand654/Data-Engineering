#!/usr/bin/python3
"""reducer2.py"""
import sys

dictionary={}
count = 0

# input comes from STDIN
for line in sys.stdin:

    line = line.strip()
    product,rating= line.split(',')
    try:
       rating = float(rating)
    except:
        continue

    if product in dictionary:
        dictionary[product][0]+=rating
        dictionary[product][1]+=1
    else:
        dictionary[product] = [rating,1]


data = dict(sorted(dictionary.items(), key = lambda x:x[1], reverse = True))	


for key,value in data.items():
    print(key,value[0]/value[1])

