# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     证券从业报名爬虫
   Description :
   Author :       phdsx
   date：          2021/3/16
-------------------------------------------------
   Change Activity:
                   2021/3/16:
-------------------------------------------------
"""
__author__ = 'phdsx'

# -*- coding: utf-8 -*-
import logging
import requests,json
from lxml import html

# To enable the initializer feature (https://help.aliyun.com/document_detail/158208.html)
# please implement the initializer function as below：
# def initializer(context):
#   logger = logging.getLogger()
#   logger.info('initializing')

def handler(event, context):
  logger = logging.getLogger()
  logger.info('hello world')
  serve_key = "你的key"
  send(serve_key)

def send(serve_key):
    url="https://www.sac.net.cn/cyry/kspt/ksbm/"
    r=requests.get(url,verify=False,timeout=50)
    r=r.content
    r=r.decode("utf8")
    tree=html.fromstring(str(r))
    title_list=tree.xpath("//a[@target='_blank']")
    title_list_out = []
    msg = ""
    for each in title_list:
        title_list_out.append(each.text)
        msg+=each.text

    if "2021年3月17日" not in title_list_out[0]:
        text="报名网站有更新"
        content=f'''
        # 现有{len(title_list_out)}条报名信息如下：
        ## {msg}'''
        data={"text":text,"desp":content}
        requests.post(f"https://sc.ftqq.com/{serve_key}.send",data=data)