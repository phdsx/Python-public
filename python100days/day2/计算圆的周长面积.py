'''
输入半径计算圆的周长和面积
version：1.0
Author：phdsx
'''

import math

radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('半径为%.2f的圆的周长为%.2f，面积为%.2f'%(radius,perimeter,area))