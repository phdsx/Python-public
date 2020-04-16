'''
@Author: phdsx
@Date: 2019-11-20 18:37:29
@LastEditTime: 2019-11-20 19:06:57
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\day5\斐波那契数列.py
'''
i=3
a=1
b=1
print(a,end='\t')
print(b,end='\t')
while i<21:
    c=a+b
    a=b
    b=c
    print(b,end='\t')
    i+=1
