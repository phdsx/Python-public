# -*- encoding : UTF-8 -*-
# Author   ：  phdsx
# 创建时间  ：  2020/4/29 10:35
# 编译器    ：  PyCharm
# 文件名    ：  text.py
# 所属工程  ：  Python-learning
# 版本号    ：  Ver.

import requests
from lxml import etree

r=requests.get(r'https://www.bilibili.com/v/dance/otaku/#/all/default/0/1')
html=etree.HTML(r.text)
print(r.text)
print(html.xpath(r'//*[@id="videolist_box"]/div[2]/ul/li[9]/div/div[2]/a'),1)