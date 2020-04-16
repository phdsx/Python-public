def f_c(num):
    c = (eval(num[:-1]) - 32) / 1.8
    return c


def c_f(num):
    f = 1.8 * eval(num[:-1]) + 32
    return f


if '__main__':
    while True:
        num = input("请输入需要转换的温度：")
        if num[-1] in ['f', 'F']:

            print("转换后的温度是{:.2f}摄氏度".format(f_c(num)))
        elif num[-1] in ["c", "C"]:

            print("转换后的温度是{:.2f}华氏度".format(c_f(num)))
        else:
            print('输入错误')

        k = input('是否退出y/n:')
        if k == "y":
            break
        else:
            pass
