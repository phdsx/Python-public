def move(n,a='A',b='B',c='C'):
        if n==1:
            print(a,'-->',c)
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

k=1
while k==1:
    n=input('请输入A柱盘子个数：')
    n=int(n)
    print(move(n))
