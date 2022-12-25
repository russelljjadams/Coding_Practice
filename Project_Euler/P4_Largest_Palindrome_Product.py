# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
l = 0
for i in range(100,1000):
    for x in range(100,1000):
        r = i*x
        if str(r) == str(r)[::-1]:
            if r > l:
                l = r
print(l)
 