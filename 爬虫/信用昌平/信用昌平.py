# -*- encoding : UTF-8 -*-
# Author   ：  phdsx
# 创建时间  ：  2020/6/19 15:44
# 编译器    ：  PyCharm
# 文件名    ：  信用昌平.py
# 所属工程  ：  Python-learning
# 版本号    ：  Ver.

import requests,json

class Webpage():
    def __init__(self):
        self.hd = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        }
        self.index_url='http://credit.bjchp.gov.cn/api/webDoublePublicityController/webFindDoubleList.form'

    def get_index(self,page_num):
        self.company_list = []
        self.company_code = []
        self.company_num = []
        self.params={'tableName':'zb_xzxk','subTableName':'enterprise','page':str(page_num),'rows':'10'}
        self.r=requests.get(self.index_url,params=self.params)
        self.r.encoding='utf-8'
        self.data=json.loads(self.r.text)
        for i in range(0,10):
            self.company_list.append(self.data.get('data').get('items')[i].get('NAME'))
            self.company_code.append(self.data.get('data').get('items')[i].get('enterpriseCode'))
            self.company_num.append(self.data.get('data').get('items')[i].get('num'))
        self.get_detail()


    def get_detail(self):
        self.url_detail='http://credit.bjchp.gov.cn/api/webDoublePublicityController/webFindDetailMain.form'
        for i in range(0,len(self.company_code)):
            self.params={'tableName': 'ZB_XZXK','enterpriseCode':'086135c40d12e66421f53d00df5df6a2','page':'1','row':str(self.company_num[i])}
            self.r=requests.get(self.url_detail,headers=self.hd,params=self.params)
            self.r.encoding = 'utf-8'
            self.data = json.loads(self.r.text).get('data').get('items')
            self.doc_id=[]
            self.doc_date=[]
            for j in range(0,self.company_num[i]):
                self.doc_id.append(self.data[j].get('WSH'))
                self.doc_date.append(self.data[j].get('JDR'))
            out_data[self.company_list[i]]={'文书号':self.doc_id,'决定日':self.doc_date}



out_data={}
a=Webpage()
a.get_index(1)#输入要爬取的页码，可用range函数取范围，加sleep防屏蔽
print(out_data)#out_data为目标数据

