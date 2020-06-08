# -*- encoding : UTF-8 -*-
# Author   ：  phdsx
# 创建时间  ：  2020/5/12 9:47
# 编译器    ：  PyCharm
# 文件名    ：  qrcode.py
# 所属工程  ：  Python-learning
# 版本号    ：  Ver.

from MyQR import myqr

myqr.run(words='https://phdsx.github.io/test',picture='1.jpg',colorized=True)