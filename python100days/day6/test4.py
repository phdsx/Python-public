'''
@Author: your name
@Date: 2019-11-25 00:21:47
@LastEditTime: 2019-11-25 00:25:09
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python100days\day6\test4.py
'''
import gbs

x=int(input("x="))
y=int(input("y="))

print("最大公约数为%d"%gbs.gcd(x,y))
print("最小公倍数为%d"%gbs.lcm(x,y))
