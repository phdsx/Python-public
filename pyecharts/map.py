# -*- encoding = utf-8 -*-
#   作者   ： phdsx
# 创建时间  ： 2020/4/26 20:45
# 文件名称  ： map.py
# 所属工程  ： Python-learning
# 版本号    ： Ver.

from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
import pyecharts

c = (
    Map()
    .add("商家A", [('北京',15),('上海',10)], "world") # 以列表形式存放数据
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-世界地图"),
        visualmap_opts=opts.VisualMapOpts(max_=200), # 设置视觉映射配置项的组件最大值为200，最小值默认为0
    )
    .render("map_world.html")
)

'''
geo = pyecharts.Geo("最高气温地理坐标系图", '2018-4-16', title_color='#fff', title_pos='center', width=1200, height=600,
                    background_color='#404a95')
geo.add("最高气温", cities, highs, is_visualmap=True, visual_range=[0, 40], visual_text_color='#fff', symbol_size=5,
        legend_pos='right', is_geo_effect_show=True)

geo.render("Geo-Low.html")
'''