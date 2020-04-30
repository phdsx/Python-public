# -*- encoding : UTF-8 -*-
# Author   ：  phdsx
# 创建时间  ：  2020/4/29 10:35
# 编译器    ：  PyCharm
# 文件名    ：  text.py
# 所属工程  ：  Python-learning
# 版本号    ：  Ver.

import requests,json
from lxml import etree

a={'a':122,"b":{'d':233}}

print(a.get('b').get('d'))