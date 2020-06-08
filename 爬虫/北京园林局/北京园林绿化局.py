# -*- encoding : UTF-8 -*-
# Author   ：  phdsx
# 创建时间  ：  2020/6/8 15:51
# 编译器    ：  PyCharm
# 文件名    ：  北京园林绿化局.py
# 所属工程  ：  python
# 版本号    ：  Ver.

import requests, json, time, openpyxl


class Webpage():
    def __init__(self):
        self.hd = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

    def get_XZXK(self):
        page_num = []
        for i in range(0, 1031, 10):  # 1031
            page_num.append(i)
        for each in page_num:
            url = f'http://sgs.bjylfw.cn:8000/rest/licence/publicAll?from={each}&max=10&keyword=&startTime=&endTime='
            r = requests.get(url, headers=self.hd)
            self.get_msg(json.loads(r.text))
            time.sleep(3)

    def get_msg(self, dict):
        msg_list = dict.get('payload').get('list')
        for each in range(0, len(msg_list)):
            tar_dict[f'{msg_list[each].get("id")}'] = {'企业名称': f'{msg_list[each].get("sqr")}',
                                                       '文书号': f'{msg_list[each].get("xzxkjdswh")}',
                                                       '决定日期': f'{msg_list[each].get("xkrq")}'}


class Sheet():
    def __init__(self):
        self.wb = openpyxl.load_workbook('行政处罚.xlsx')
        self.ws = self.wb['Sheet1']

    def write_in(self, dict):
        self.row_num = 1
        for id in dict:
            self.ws.cell(self.row_num, 1).value = id
            self.ws.cell(self.row_num, 2).value = dict.get(str(id)).get('企业名称')
            self.ws.cell(self.row_num, 3).value = dict.get(str(id)).get('文书号')
            self.ws.cell(self.row_num, 4).value = dict.get(str(id)).get('决定日期')
            self.row_num += 1

        self.wb.save('行政处罚.xlsx')


if __name__ == '__main__':
    a = Webpage()
    tar_dict = {}
    a.get_XZXK()
    biaoge = Sheet()
    biaoge.write_in(tar_dict)
