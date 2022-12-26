# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:33:22 2022

@author: Russell J Adams

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import math
from functools import reduce

def smallest_multiple(n):
  # Compute the LCM of all the numbers from 1 to n
  lcm = reduce(lambda x, y: (x*y)//math.gcd(x, y), range(1, n+1))
  
  # Return the LCM
  return lcm

# Test the function
print(smallest_multiple(10))  # should print 2520
print(smallest_multiple(20))  # should print 232792560


