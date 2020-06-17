# -*- encoding : UTF-8 -*-
# Author   ：  phdsx
# 创建时间  ：  2020/5/27 16:40
# 编译器    ：  PyCharm
# 文件名    ：  企业安全网.py
# 所属工程  ：  Python-learning
# 版本号    ：  Ver.
import requests,lxml

headers = {
            "user-agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
        }

r=requests.get('http://www.safehoo.com/Manage/System/Common/201907/1570628.shtml',headers=headers)
r.encoding='utf-8'
print(r.text)