#!/usr/bin/python3
"""reducer9.py"""
import sys
import numpy as np


lst_income = []
lst_rating = []

for line in sys.stdin:
    line = line.strip()
    try:
        total_income, rating = line.split(',')
        total_income = float(total_income)
        rating = float(rating)
        lst_income.append(total_income)
        lst_rating.append(rating)
    except :
        continue  


income = np.array(lst_income)
rating = np.array(lst_rating)

correlation_matrix = np.corrcoef(income, rating)
#print(correlation_matrix[0:1,1:])
corr_x_y = correlation_matrix[0, 1]
print(f"Correlation coefficient: {corr_x_y}")


