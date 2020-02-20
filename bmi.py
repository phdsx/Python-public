i=1

while i > 0:
    height=input("请输入身高（cm）：")
    height=float(height)
    weight=input("请输入体重（kg）：")
    weight=float(weight)

    BMI=weight/(height*height/10000)

    if BMI < 18.5:
        print("您的体重过轻")
    elif BMI<25:
        print("您的体重正常")
    elif BMI<28:
        print("您的体重过重")
    elif BMI<32:
        print("您的体重肥胖")
    else:
        print("您的体重超重")

    k=input("是否退出？（y/n）")
    if k=="y":
        i=0
    else:
        i=i+1
