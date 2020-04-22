# -*- encoding = utf-8 -*-
#   作者   ： phdsx
# 创建时间  ： 2020/4/22 0:20
# 文件名称  ： Bar.py
# 所属工程  ： Python-learning
# 版本号    ： Ver.

from pyecharts.charts import Bar
import random

bar=(
    Bar()
    .add_yaxis("测试",random.randint(0,100))
    .add_xaxis(["A","B","C","D","E"])
)

bar.render()