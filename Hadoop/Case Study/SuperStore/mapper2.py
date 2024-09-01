#!/usr/bin/python3
"""mapper2.py"""
lst=[]
import sys
# input comes from standard input
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(',')
    # increase counters
    print("%s, %s" % (words[5],words[16]))
#    for word in words:
        # write the results to strdout(standard output)
        # tab-delimited; the trivial word count is 1
	# Output of Mapper Job is input to Reducer <--
       # print('%s\t%s' % (word[0], 1))
 #       print(word)
  #      break

