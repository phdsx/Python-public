# -*- encoding : UTF-8 -*-
# Author   ：  phdsx
# 创建时间  ：  2020/4/29 9:12
# 编译器    ：  PyCharm
# 文件名    ：  main.py
# 所属工程  ：  Python-learning
# 版本号    ：  Ver.

import requests, time,json
from lxml import etree


class Bilibili():
    def __init__(self):
        self.headers = {
            "user-agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
        }
        self.video_data={}

    # 获取网页内容
    def get_newlist(self, url):
        error_time = 0
        while error_time < 3:
            r = requests.get(url, headers=self.headers, timeout=3)
            if r.status_code == 200:
                data=json.loads(r.text)
                return data
            else:
                error_time += 1
                time.sleep(3)
        return None

    def get_data(self,url):
        data = self.get_newlist(url).get('data').get("archives")
        return data

    def get_video_info(self,url):
        datas=self.get_data(url)
        for each in datas:
            self.video_data['aid']=each.get('aid')
            self.video_data['tname'] = each.get('tname')
            self.video_data['copyright'] = each.get('copyright')
            self.video_data['title'] = each.get('title')
            self.video_data['pubdate'] = each.get('pubdate')
            self.video_data['ctime'] = each.get('ctime')
            self.video_data['owner'] = [each.get('owner').get('mid'),each.get('owner').get('name')]
            self.video_data['stat'] = each.get('stat')

        return self.video_data

i = 1
b = Bilibili()
a = b.get_video_info(rf'https://api.bilibili.com/x/web-interface/newlist?rid=20&type=0&pn={i}&ps=20')
print(a)
