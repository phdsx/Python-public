# -*- encoding = utf-8 -*-
#   作者   ： phdsx
# 创建时间  ： 2020/4/26 22:29
# 文件名称  ： 地区.py
# 所属工程  ： Python-learning
# 版本号    ： Ver.
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.charts import Geo
import json
from pyecharts.globals import ChartType, SymbolType

with open('friend.json', 'r') as f:
    friends = json.load(f)

data = {'other': 0, '台湾': 1}
for friend in friends:
    try:
        province = friend.get('Province')

        if data.get(str(province)) == None:
            data[str(province)] = 1
        elif province != '':
            data[str(province)] += 1
        else:
            data['other'] += 1
    except:
        pass
'''
for z in zip(data.keys(),data.values()):
    print(z)

'''
print(data.get(''))
for z in zip(data.keys(), data.values()):
    print(z)
c = (
    Map()

        .add("微信好友", [list(z) for z in zip(data.keys(), data.values())], maptype='china')  # 以列表形式存放数据
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        .set_global_opts(
        title_opts=opts.TitleOpts(title="微信好友地区统计"),
        visualmap_opts=opts.VisualMapOpts(max_=50),  # 设置视觉映射配置项的组件最大值为200，最小值默认为0
    )
        .render("wx.html")
)
