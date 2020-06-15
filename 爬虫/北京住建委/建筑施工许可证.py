# -*- encoding = utf-8 -*-
#   作者   ： phdsx
# 创建时间  ： 2020/6/15 20:49
# 文件名称  ： 建筑施工许可证.py
# 所属工程  ： Python-learning
# 版本号    ： Ver.

import requests
from lxml import etree


class Webpage():
    def __init__(self):
        self.hd = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
        self.url = 'http://bjjs.zjw.beijing.gov.cn/eportal/ui?pageId=425000'
        self.params = {'currentPage': '1', 'pageSize': '15'}
        self.web_data = ''

    def gen_params(self, i):
        self.params['currentPage'] = str(i)

    def get_data_info(self):
        self.gen_params(1)
        self.r = requests.post(self.url, headers=self.hd, params=self.params)
        #print(self.r.text)
        return self.r

    def deposit_html(self):
        self.html = etree.HTML(self.get_data_info().text)
        self.permit_ids = self.html.xpath(
            '//*[@id="CommonSearchResult"]/table[2]/tbody/tr/td/table[2]/tbody/tr/td[3]/text()')

        print(self.permit_ids)


a = Webpage()
a.get_data_info()
a.deposit_html()
