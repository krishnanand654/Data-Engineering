#!/usr/bin/python3
"""reducer1.py"""

import sys

data = {}

for line in sys.stdin:
    line = line.strip()

    try:
        zone, regional_zone, ton, refill = line.split(",")
        ton = int(ton)
        refill = int(refill)
    except ValueError:
        continue

    key = (zone, regional_zone)

    if key in data:
        data[key][0] += ton
        data[key][1] += refill * ton
    else:
        data[key] = [ton, refill * ton]


print(f"{'Zone':<10} | {'Regional Zone':<20} | {'Total Supply':>15} | {'Demand':>15} | {'Status':>15}")
print("-" * 90)

for (zone, regional_zone), values in data.items():
    total_weight, value = values
    print(f"{zone:<10} | {regional_zone:<20} | {total_weight:>15} | {value:>15} | {'Demand > Supply' if value>total_weight else 'Supply > Demand' }")

