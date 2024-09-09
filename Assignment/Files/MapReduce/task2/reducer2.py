#!/usr/bin/python3
"""reducer2.py"""

import sys
import numpy as np

data={}
encode = {'Large':3,'Mid':2, 'Small':1}

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()

    capacity, refill = line.split(",")
    try:
        refill = int(refill)
    except:
        continue

    if capacity in data:
        data[capacity][0]+=refill
        data[capacity][1]+=1
    else:
        data[capacity]=[refill,1]

values=[]
sizes=[]

for k, v in data.items():
    avg = v[0]/v[1]
    values.append(avg)
    sizes.append(encode[k])
    print(f"{k} {avg}")


correlation_matrix = np.corrcoef(sizes, values)

correlation_xy = correlation_matrix[0, 1]

print("Correlation between wh_capacity_size and num_refilled:", correlation_xy)



