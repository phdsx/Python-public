# -*- encoding = utf-8 -*-
#   作者   ： phdsx
# 创建时间  ： 2020/4/21 21:51
# 文件名称  ： 01matplotlib基础绘图.py
# 所属工程  ： Python-learning
# 版本号    ： Ver.

import matplotlib.pyplot as plt
import random
from matplotlib import font_manager
'''
font = {"family": "MicroSoft Yahei",
                  "weight":"bold",
                  "size": "larger"
}
matplotlib.rc(font)
'''
my_font=font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
data = [random.randint(20, 35) for i in range(120)]
x = range(0, 120)
fig = plt.figure(figsize=(30, 6))
plt.plot(x, data)
plt.yticks(range(min(data), max(data) + 1))

shijian = ["10点{}".format(i) for i in range(120)][::30]
plt.xticks(x[::30], shijian, rotation=45,fontproperties=my_font)

plt.show()
