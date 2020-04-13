import random

num = random.randint(0,100)
guess = int(input("请输入所猜数字："))
while guess != num:
    if guess > num:
        print("大了")
    else:
        print("小了")
    guess = int(input("请重新输入："))
print("恭喜！答对了！")