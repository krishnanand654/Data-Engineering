#!/usr/bin/python3
"""reducer8.py"""
import sys
from collections import defaultdict

current_product = None
weekly_sales = defaultdict(int)

for line in sys.stdin:
    
    product_line, week, quantity = line.strip().split(',')
    quantity = int(quantity)
        
    if current_product == product_line:
        weekly_sales[week] += quantity
    else:
        if current_product:
            weeks = sorted(weekly_sales.keys())
            for i in range(1, len(weeks)):
               previous_week = weeks[i-1]
               current_week = weeks[i]
               growth = weekly_sales[current_week] - weekly_sales[previous_week]
               print(f"{current_product} \t {current_week}\t{growth}")
        current_product = product_line
        weekly_sales = defaultdict(int)
        weekly_sales[week] = quantity

if current_product == product_line:
    weeks = sorted(weekly_sales.keys())
    for i in range(1, len(weeks)):
       previous_week = weeks[i-1]
       current_week = weeks[i]
       growth = weekly_sales[current_week] - weekly_sales[previous_week]
       print(f"{current_product} \t {current_week}\t{growth}")
