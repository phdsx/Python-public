def sushu(x):
    if x>1:
        for factor in range(2,x):
            if x%factor==0:
                return print('%d不是素数'%x)
    else:
        return print('1无效')