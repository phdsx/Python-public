userlevel=input("请输入现在等级：")
userlevel=int(userlevel)-4
level=range(1,userlevel+1)
maoliang=input('请输入%s级需要猫粮的数字部分：'%userlevel)
maoliang=float(maoliang)
danwei=input('请输入猫粮结尾单位aa/t/b/m/k:')
for i in level:
    maoliang="%.2f"%maoliang
    maoliang=float(maoliang)
    print(userlevel-i+1,"级",maoliang,danwei)
    maoliang=(maoliang/2)
    if maoliang>1:
        pass;
    else:
        if danwei=="aa":
            danwei="t";
        elif danwei=="t":
            danwei="b";
        elif danwei=="b":
            danwei="m";
        elif danwei=="m":
            danwei="k";
        maoliang=maoliang*1000
print(123)