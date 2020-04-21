# -*- encoding = utf-8 -*-
#   作者   ： phdsx
# 创建时间  ： 2020/4/21 21:51
# 文件名称  ： 01matplotlib基础绘图.py
# 所属工程  ： Python-learning
# 版本号    ： Ver.

import matplotlib.pyplot as plt
import random

data = []
for i in range(12):
    data.append(random.randint(6, 30))
x = range(2, 26, 2)
y = data

fig = plt.figure(figsize=(12, 6), dpi=100)

plt.plot(x, y)

plt.xticks([i / 2 for i in range(0, 49)][::3])
plt.yticks(range(min(y), max(y) + 1))

# plt.savefig("1.svg")


plt.show()
