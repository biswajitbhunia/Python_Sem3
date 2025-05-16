# -*- coding: utf-8 -*-
"""
Created on Fri May 16 06:22:02 2025
@author: biswajit
w.a.p. to find the sum of digits
"""

n = eval(input('Enter a number'))
s = 0
while(n>0):
    r = n % 10
    n = n // 10
    s = s + r
    
print('sum of digits: ',s)
print(f'sum of digits:  {s} ')
print('sum of digist: {}'.format(s))