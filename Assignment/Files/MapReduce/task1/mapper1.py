#!/usr/bin/python3
"""mapper.py"""
import sys
# input comes from standard input
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # If the line is not empty
    if line:
        columns = line.split(',')
        if columns:
            zone = columns[4].strip()
            WH_regional_zone = columns[5].strip()
            product_wg_ton = columns[-1].strip()
            refills = columns[6].strip()

            if zone != "zone" and WH_regional_zone != "WH_regional_zone" and product_wg_ton != "product_wg_ton" and refills != "num_refill_req_l3m":
                print('%s,%s,%s,%s' % (zone, WH_regional_zone, product_wg_ton, refills))
