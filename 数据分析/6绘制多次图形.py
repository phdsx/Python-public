# -*- encoding = utf-8 -*-
#   作者   ： phdsx
# 创建时间  ： 2020/4/28 0:12
# 文件名称  ： 6绘制多次图形.py
# 所属工程  ： Python-learning
# 版本号    ： Ver.

import random
from matplotlib import pyplot as plt
from matplotlib import font_manager

a=[]
b=[]
for i in range(10,30):
    a.append(random.randint(0,5))
    b.append(random.randint(0, 5))

x=range(10,30)
my_font=font_manager.FontProperties(fname=r'C:\Windows\Fonts\MSYHL.TTC')
#设置图形大小
plt.figure(figsize=(18,8),dpi=80)

plt.plot(x,a,label='自己',color='pink',linestyle=':')
plt.plot(x,b,label='同桌',color='cyan',linestyle='--',linewidth=9)
#设置xy刻度
x_label=[f'{i}岁' for i in x]
plt.xticks(x,x_label,fontproperties=my_font,rotation=45)
plt.yticks(range(0,7))

#绘制网格
plt.grid(alpha=0.4)

#添加图例
plt.legend(prop=my_font,loc='upper center')

plt.show()