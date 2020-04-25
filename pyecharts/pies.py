# -*- encoding = utf-8 -*-
#   作者   ： phdsx
# 创建时间  ： 2020/4/23 23:08
# 文件名称  ： pies.py
# 所属工程  ： Python-learning
# 版本号    ： Ver.
from pyecharts.charts import Pie
from pyecharts import options as opt
import json
from sys import argv
import time

#script,file=argv
file='friend.json'
#print(file)
#time.sleep(20)
with open(file) as f:
    friend=json.load(f)

Sex={'男':0,"女":0,"不知道":0}
for each in friend:
    a=each.get("Sex")
    if a==1:
        Sex["男"]+=1
    elif a==2:
        Sex['女']+=1
    else:
        Sex['不知道']+=1
pie=(
    Pie()

    .add('',[list(z) for z in zip(list(Sex.keys()),list(Sex.values()))])
    .set_global_opts(title_opts=opt.TitleOpts(title="微信好友性别分析"))
    .set_series_opts(label_opts=opt.LabelOpts(formatter="{b}: {c}"))
)
pie.render()
