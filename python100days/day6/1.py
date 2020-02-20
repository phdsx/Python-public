'''
@Author: your name
@Date: 2019-11-21 00:00:31
@LastEditTime: 2019-11-24 22:42:17
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python100days\day6\1.py
'''
'''
@Author: your name
@Date: 2019-11-21 00:00:31
@LastEditTime: 2019-11-21 00:11:14
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python100days\day6\1.py
'''
"""
输入M和N计算C(M,N)

Version: 0.1
Author: 骆昊
"""

m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fmn = 1
for num in range(1, m - n + 1):
    fmn *= num
print(fm // fn // fmn)