# -*- coding: utf-8 -*-

s = input('Enter any Word :')

l = len(s)

print(l)

for i in range(l):
    print(s[i])
    
    
for i in range(l):
    for j in range(i+1):
        print(s[j],end=' ')
    print()