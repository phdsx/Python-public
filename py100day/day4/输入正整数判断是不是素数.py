'''输入正整数判断是不是素数
version：1.0
author：phdsx
'''

num=int(input("请输入一个正整数："))
for i in range (2,num):
    if num%i==0:
        print('%d不是素数'%num)
        n=0
        break
    else:
        n=1
        continue
if n==1:
    print('%d是素数'%num)