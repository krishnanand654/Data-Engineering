#!/usr/bin/python3
"""reducer4.py"""

import sys
import numpy as np

data={}


# input comes from STDIN
for line in sys.stdin:
    line = line.strip()

    issue, ton = line.split(",")
    try:
        issue = int(issue)
        ton = int(ton)
    except:
        continue
    if issue in data:
        data[issue][0]+=ton
        data[issue][1]+=1
    else:
        data[issue]=[ton,0]


issues=[]
values=[]
total = []
count = []

for k, v in sorted(data.items()):
    avg = v[0]/v[1]
    values.append(avg)
    total.append(v[0])
    count.append(v[1])
    issues.append(int(k))


sum_avg_total = sum(values)/len(data)


print(f"{'Issues':<5} {'Total':<10} {'Count':<10} {'Avg_Weights':<25} {'Impact':<10}")
print("-"*100)

for i in range(len(data)):
    if values[i] > sum_avg_total:
        impact = "High"
    else:
        impact = "Low"
    

    print(f"{issues[i]:<5} {total[i]:<10} {count[i]:<10} {values[i]:<25} {impact:<10}")



#correlation_matrix = np.corrcoef(issues, values)

#correlation_xy = correlation_matrix[0, 1]

#print("Correlation: ", correlation_xy)
