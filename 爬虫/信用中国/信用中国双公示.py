# -*- encoding : UTF-8 -*-
# Author   ：  phdsx
# 创建时间  ：  2020/6/11 10:56
# 编译器    ：  PyCharm
# 文件名    ：  信用中国双公示.py
# 所属工程  ：  Python-learning
# 版本号    ：  Ver.

import requests
hd = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
r=requests.get('https://public.creditchina.gov.cn/private-api/typeNameAndCountSearch?keyword=&type=%E8%A1%8C%E6%94%BF%E8%AE%B8%E5%8F%AF&searchState=2&entityType=1%2C2%2C3%2C7&page=2&pageSize=10',headers=hd)
print(r.text)