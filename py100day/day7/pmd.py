'''
@Author: your name
@Date: 2020-01-08 16:14:26
@LastEditTime : 2020-01-08 16:16:22
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\day7\pmd.py
'''
import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()