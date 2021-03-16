'''
@Author: your name
@Date: 2019-11-20 19:07:56
@LastEditTime: 2019-11-20 19:28:24
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\day5\完美数.py
'''
for i in range(1,10001):
    sum=0
    for factor in range(1,i):
        if i%factor==0:
            sum+=factor
            if sum==i:
                print(i,end="\t")
            else:
                pass
        else:
            pass
        