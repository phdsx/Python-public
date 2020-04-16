import math
from fangcheng import quadratic
i=0
while i==0:
    a=input("请输入a：")
    b=input("请输入b：")
    c=input("请输入c：")

    print('方程的解为:',quadratic(a,b,c))
    k=input('请问是否继续？（y/n）')
    if k== 'n':
        i=1
    else:
        i=0
print("计算结束")
