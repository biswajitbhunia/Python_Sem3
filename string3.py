# -*- coding: utf-8 -*-

s3 =input('Enter new String : ')
if s3.isalpha():
    print('Alphabet')
    if s3.isupper():
        print("UPPER CASE")
    elif s3.islower():
        print('lower case')
elif s3.isdigit():
    print('Digits')

elif s3.isalnum():
    print('Alpha Numeric')
else:
    print('Others')