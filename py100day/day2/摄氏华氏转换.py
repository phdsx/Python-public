'''
摄氏温度华氏温度互相转换
version 1.0
Author: phdsx
'''
n=1
while n==1:
    key=int(input('请选择转换方向：1.摄氏度转华氏度；2华氏度转摄氏度'))
    if key==1:
        c=float(input('请输入摄氏温度：'))
        f=32+c*1.8
        print("%.2f摄氏度等于%.2f华氏度"%(c,f))
        i=str(input('是否继续转换（y/n）'))
        if i=='y':
            n=1
        else:
            n=0
    else:
        f=float(input('请输入华氏温度：'))
        c=(f-32)/1.8
        print("%.2f华氏度等于%.2f摄氏度"%(f,c))
        i=str(input('是否继续转换（y/n）'))
        if i=='y':
            n=1
        else:
            n=0