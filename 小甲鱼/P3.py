import random

print("game start")
temp=random.randint(0,100)
while True:
    num=int(input("pllease input the number:"))

    if num>temp:
        print("larger")
    elif num<temp:
        print("smaller")
    else:
        print("bungo")
        break
print("game over")