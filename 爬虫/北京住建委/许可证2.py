# -*- encoding = utf-8 -*-
#   作者   ： phdsx
# 创建时间  ： 2020/6/15 22:16
# 文件名称  ： 许可证2.py
# 所属工程  ： Python-learning
# 版本号    ： Ver.

import requests
from bs4 import BeautifulSoup
from lxml import etree


hd = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}
url = 'http://bjjs.zjw.beijing.gov.cn/eportal/ui?pageId=425000'
params = {'currentPage': '1', 'pageSize': '15'}
web_data = ''

r=requests.post(url,headers=hd,params=params)
e= etree.HTML(r.text)
ids=e.xpath('//*[@id="CommonSearchResult"]/table[2]/tbody/tr/td/table[2]/tbody/tr/td[3]/text()')
print(ids)