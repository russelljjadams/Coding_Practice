# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 11:29:28 2022

@author: Russell J Adams
"""
# Find the product abc.

for a in range(3, 1000):
    for b in range (a + 1, 999):
        cSquared = a**2 + b**2
        c = cSquared**0.5

        if a + b + c == 1000:
            product = a * b * c
            print(product)
            break