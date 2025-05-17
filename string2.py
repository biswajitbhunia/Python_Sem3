# -*- coding: utf-8 -*-

x = 36

print(x+x)

#Convert Number into String str()

print(str(x)+str(x))

y = '20'

#Convert String into Number int(), str()
print(int(y)+eval(y))

s1 =  'the quick brown fox'

print('Location of "fox" : ', s1.find('fox'))


print("Location of 'fox' : ", s1.find('fox'))

print("Location of 'fox' : ", s1.find('Fox'))



s2 = input('Enter a substring to search: ')
if s2.islower()==False:
    print("Location  : ", s1.index(s2.lower()))
else:
    print("Location : ", s1.index(s2))










