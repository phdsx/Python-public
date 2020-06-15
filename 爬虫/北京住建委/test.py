
# -*- encoding = utf-8 -*-
#   作者   ： phdsx
# 创建时间  ： 2020/6/15 22:33
# 文件名称  ： test.py
# 所属工程  ： Python-learning
# 版本号    ： Ver.

import requests
from lxml import etree


hd = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
url = 'https://www.zhibo8.cc/'
r=requests.get(url,headers=hd)
e= etree.HTML(r.text)
ids=e.xpath('//*[@id="recommend"]/div[1]/ul/li/a[1]/text()')
print(ids)