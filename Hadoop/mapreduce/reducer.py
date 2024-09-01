#!/usr/bin/python3
"""reducer.py"""
import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:

    line = line.strip()
    # parse the input we got from mapper.py
    # word & count are seperated by <tab> delimited
    # 1 -> No of splits
    word, count = line.split('\t', 1)

    # convert count (currently a string) to integer data
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here key is word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to stdoutput seperated by tab
            print ('%s\t%s' % (current_word, current_count))
	# making current_word = word
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print ('%s\t%s' % (current_word, current_count))
