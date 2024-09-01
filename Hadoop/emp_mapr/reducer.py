#!/usr/bin/python3
"""reducer.py"""
import sys

current_country = None
current_count = 0
country = None
dictionary={}

# input comes from STDIN
for line in sys.stdin:

    line = line.strip()
    # parse the input we got from mapper.py
    # word & count are seperated by <tab> delimited
    # 1 -> No of splits
    country, count = line.split(',', 1)

    # convert count (currently a string) to integer data
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here key is word) before it is passed to the reducer
    if current_country == country:
        current_count += count
    else:
        if current_country:
            # write result to stdoutput seperated by tab
           # print ('%s,%s' % (current_country, current_count))
            dictionary[current_country]= current_count
	# making current_word = word
        current_count = count
        current_country = country
    

# do not forget to output the last word if needed!
if current_country == country:
   # print ('%s,%s' % (current_country, current_count))
   dictionary[current_country]= current_count

data = dict(sorted(dictionary.items(), key = lambda x:x[1], reverse = True))	
for key, value in data.items():
    print(key,value)

