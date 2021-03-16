'''
@Author: your name
@Date: 2020-01-08 15:46:22
@LastEditTime : 2020-01-08 15:47:25
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\day7\fib.py
'''
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()