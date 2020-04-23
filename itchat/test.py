# -*- encoding = utf-8 -*-
#   作者   ： phdsx
# 创建时间  ： 2020/4/23 21:59
# 文件名称  ： test.py
# 所属工程  ： Python-learning
# 版本号    ： Ver.

import itchat,json


itchat.auto_login(hotReload=True)
friends=itchat.get_friends()
with open('friend.json',"w") as j:
    json.dump(friends,j)
