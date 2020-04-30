# -*- encoding : UTF-8 -*-
# Author   ：  phdsx
# 创建时间  ：  2020/4/29 9:12
# 编译器    ：  PyCharm
# 文件名    ：  main.py
# 所属工程  ：  Python-learning
# 版本号    ：  Ver.

import requests, time
from lxml import etree


class Bilibili():
    def __init__(self):
        self.headers = {
            "user-agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
        }

    # 获取网页内容
    def get_newlist(self, url):
        error_time = 0
        while error_time < 3:
            r = requests.get(url, headers=self.headers, timeout=3)
            if r.status_code == 200:
                return r.text
            else:
                error_time += 1
                time.sleep(3)
        return '错误'


i = 1
b = Bilibili()
a = b.get_newlist(rf'https://api.bilibili.com/x/web-interface/newlist?rid=20&type=0&pn={i}&ps=20')
print(a)
