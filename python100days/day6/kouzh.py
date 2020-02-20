#设x为买到口罩的次数
for x in range(1,11):
    if 10+5*x-(10-x)-10==12:
        print(x)
    else:
        print('%.f次不成立'%x)