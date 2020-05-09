#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    unqiue = set(ar)
    for i in unqiue:
        count = count + (ar.count(i)//2)
    return count


print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
