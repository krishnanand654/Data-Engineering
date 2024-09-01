#!/usr/bin/python3
"""mapper3.py"""
import sys
# input comes from standard input
for line in sys.stdin:
    # remove leading and trailing whitespace
    word = line.strip().split(',')

    print('%s,%s,%s' % (word[1], word[5], word[7]))
