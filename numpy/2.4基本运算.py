# -*- encoding = utf-8 -*-
#   作者   ： phdsx
# 创建时间  ： 2020/4/20 23:24
# 文件名称  ： 2.4基本运算.py
# 所属工程  ： Python-learning
# 版本号    ： Ver.

import numpy as np

a=np.arange(9).reshape((3,3))
print(a)
print(np.clip(a,2,4))
