'''
@Author: your name
@Date: 2019-11-25 00:17:34
@LastEditTime: 2019-11-25 00:24:32
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: \python100days\day6\gbs.py
'''
def gcd(x, y):
    """求最大公约数"""
    if x>y:
        (x, y) = (y, x)
    else:
        pass
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)