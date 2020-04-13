'''
九九乘法表
version：1.0
Author：phdsx
'''


for i in range (1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(i,j,i*j),end='\t')
    print('\n')