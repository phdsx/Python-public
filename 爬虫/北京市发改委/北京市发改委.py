# -*- encoding : UTF-8 -*-
# Author   ：  phdsx
# 创建时间  ：  2020/6/17 12:25
# 编译器    ：  PyCharm
# 文件名    ：  北京市发改委.py
# 所属工程  ：  Python-learning
# 版本号    ：  Ver.

import requests,openpyxl
from lxml import etree

class Webpage():
    def __init__(self):
        self.hd = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
            }
        self.page_num=3

    def get_index_1(self):
        self.url='http://fgw.beijing.gov.cn/fzggzl/yfxz/xzxk_sgs/index.htm'
        self.r = requests.get(self.url, headers=self.hd)
        self.r.encoding = 'utf-8'
        self.doclink=self.get_href()
        for each in self.doclink:
            self.get_detail_page(each)
            self.deal_info()

    def get_index(self,i):
        self.url=f'http://fgw.beijing.gov.cn/fzggzl/yfxz/xzxk_sgs/index_{i}.htm'
        self.r=requests.get(self.url,headers=self.hd)
        self.r.encoding='utf-8'
        return self.r

    def get_href(self):
        self.html = etree.HTML(self.r.text)
        self.linklist = self.html.xpath("/html/body/div[3]/div[2]/div[1]/ul/li/a/@href")
        self.newlinklist=[]
        for each in self.linklist:
            self.newlink='http://fgw.beijing.gov.cn/fzggzl/yfxz/xzxk_sgs'+each[1:]
            self.newlinklist.append(self.newlink)
        return self.newlinklist

    def get_detail_page(self,url):
        self.detail=requests.get(url,headers=self.hd)
        self.detail.encoding='utf-8'
        return self.detail

    def deal_info(self):
        self.html = etree.HTML(self.detail.text)
        title.append(self.html.xpath("/html/body/div[3]/div[2]/div[1]/text()")[0])
        date.append(self.html.xpath("/html/body/div[3]/div[2]/div[4]/p/span[1]/text()")[0].split('：')[1].split(' ')[0])
        company.append(self.html.xpath("/html/body/div[3]/div[2]/div[4]/p/span[3]/text()")[0].split('：')[1])

    def get_info(self,page_num):
        self.get_index_1()
        for i in range(1,int(page_num)):
            self.get_index(i)
            self.get_href()
            for each in self.newlinklist:
                self.get_detail_page(each)
                self.deal_info()

    def test(self):
        for i in range(0,len(date)):
            print(title[i],date[i],company[i],'\n')

class Sheet():
    def __init__(self):
        self.wb = openpyxl.load_workbook('行政许可.xlsx')
        self.ws = self.wb['Sheet1']
        self.ws.cell(1, 1).value='文件名称'
        self.ws.cell(1, 2).value = '发布日期'
        self.ws.cell(1, 3).value = '受文单位'

    def write_in(self):
        try:
            print('开始写入Excel')
            self.row_num = 2
            for i in range(2,len(date)+2):
                self.ws.cell(i, 1).value = title[i-2]
                self.ws.cell(i, 2).value = date[i-2]
                self.ws.cell(i, 3).value = company[i-2]

            self.wb.save('行政许可.xlsx')
            print('保存成功')
        except:
            print('excel错误')


title=[]
date=[]
company=[]
a=Webpage()
a.get_info(3)#输入要爬取的页数
b=Sheet()
b.write_in()
