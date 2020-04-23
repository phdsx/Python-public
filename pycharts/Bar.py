# -*- encoding = utf-8 -*-
#   作者   ： phdsx
# 创建时间  ： 2020/4/22 0:20
# 文件名称  ： Bar.py
# 所属工程  ： Python-learning
# 版本号    ： Ver.

from pyecharts.charts import Bar
import random
from pyecharts import options as opt
from pyecharts.globals import ThemeType

a = []
for i in range(5):
    a.append(random.randint(0, 100))
bar = (
    Bar(init_opts=opt.InitOpts(theme=ThemeType.ROMANTIC))
        .add_yaxis("测试", a)
        .add_xaxis(["A", "B", "C", "D", "E"])
        .set_global_opts(title_opts=opt.TitleOpts(title="主标题", subtitle="副标题"))
)

bar.render()
