"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注

Version:1.0
Author: phdsx
"""

from random import randint
money = 1000

print('您的总资产为%.2f'%money)

debt=float(input("请输入下注金额："))
while debt<=0 or debt>money:
    debt=float(input('请重新输入赌注金额！不要超出范围：'))
#第一轮游戏#
first= randint(1,6)+randint(1,6)
print('本次点数之和为%d'%first)
if first==7 or first==11:
    print('玩家胜！获得赌注%.2f'%debt)
    money+=debt
elif first == 2 or first== 3 or first==12:
    print('庄家胜！损失赌注！')
    money-=debt
else:
    pass
#第二轮往后#
while money>0:
    print('您的资产为：%.2f'%money)
    debt=float(input('请输入赌注金额：'))
    while debt<=0 or debt>money:
        debt=float(input('请重新输入赌注金额！不要超出范围：'))
    num=randint(1,6)+randint(1,6)
    print('本次点数之和为%d'%num)
    if num==7:
        print('庄家胜！')
        money-=debt
    elif num==first:
        print('玩家胜！')
        money+=debt
    else:
        pass
print('你破产了！')