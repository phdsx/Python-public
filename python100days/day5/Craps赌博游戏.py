"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注

Version: 1.0
Author: phdsx
"""

from random import randint

money = 1000

while True:
    print ('您的资产为%.2f元'%money)
    debt=float(input('请输入下注金额：'))
    if 0<debt<=money:
        break

first=randint(1,6)+randint(1,6)
print(first)
if first==7 or first==11:
    print('玩家胜！')
    money += debt
elif first==2 or first==3 or first==12:
    print('庄家胜！')
    money -= debt
else:
    print('开始下一轮！')
    if money>0:
        while True:
            print ('您的资产为%.2f元'%money)
            debt=float(input('请输入下注金额：'))
            if 0<debt<=money:
                break
        num=randint(1,6)+randint(1,6)
        print(num)
        if num== 7:
            print('庄家胜！')
            money-=debt
        elif num==first:
            print('玩家胜！')
            money+=debt
    print('你破产了！')
