#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the strangeGrid function below.
#
def strangeGrid(r, c):
    if r % 2 == 1:
        r = r / 2;
        answer = 10 * r + 2 * (c - 1)
    else:
         r = (r - 1) / 2;
         answer = 10 * r + 2 * (c - 1) + 1
    return answer
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rc = raw_input().split()

    r = int(rc[0])

    c = int(rc[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()
