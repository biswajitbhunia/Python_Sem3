# -*- coding: utf-8 -*-
s1 ='       hello'
s2 = 'hello          '
s3= '       hello         '

print(s1+'\n'+s2+'\n'+s3)

print('.'*40)
#left strip: eleminate unecessary blank spaces from the left side 
print(s1.lstrip())

print('.'*40)
#left strip: eleminate unecessary blank spaces from the right side 
print(s2.rstrip())

print('.'*40)
#left strip: eleminate unecessary blank spaces from the both side
print(s3.strip())


print(s1.strip()+'\n'+s2.strip()+'\n'+s3.strip())