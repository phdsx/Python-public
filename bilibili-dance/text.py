# -*- encoding : UTF-8 -*-
# Author   ：  phdsx
# 创建时间  ：  2020/4/29 10:35
# 编译器    ：  PyCharm
# 文件名    ：  text.py
# 所属工程  ：  Python-learning
# 版本号    ：  Ver.

import requests,json
from lxml import etree

i=1
headers={
            "user-agent":"Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
        }
r=requests.get(rf'https://api.bilibili.com/x/web-interface/newlist?rid=20&type=0&pn={i}&ps=20',headers=headers)
print(r.status_code)
data=json.loads(r.text)
print(data.get('data').get("archives"))