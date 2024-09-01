#!/usr/bin/python3
"""reducer3.py"""
import sys
from collections import defaultdict

current_city = None
payment_methods = defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    city, payment_method = line.split(',', 1)

    if city != current_city:
        if current_city:
            # Output the most popular payment method for the previous city
            most_popular_method = max(payment_methods, key=payment_methods.get)
            print(f'{current_city}\t{most_popular_method}')
        
        # Reset for the new city
        current_city = city
        payment_methods = defaultdict(int)
    
    # Increment count for the current city's payment method
    payment_methods[payment_method] += 1

# Output the most popular payment method for the last city
if current_city:
    most_popular_method = max(payment_methods, key=payment_methods.get)
    print(f'{current_city}\t{most_popular_method}')

