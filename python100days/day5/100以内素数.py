'''
@Author: your name
@Date: 2019-11-20 21:19:24
@LastEditTime: 2019-11-20 23:14:55
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python100days\day5\100以内素数.py
'''
i=2
while i<100:
    for factor in range(2,i-1):
        if i%factor==0:
            i+=1
        else:
            pass
    if i<100:
        print(i)
        i+=1
    else:
        break