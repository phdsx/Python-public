# -*- encoding : UTF-8 -*-
# Author   ：  phdsx
# 创建时间  ：  2020/6/19 16:18
# 编译器    ：  PyCharm
# 文件名    ：  test.py
# 所属工程  ：  Python-learning
# 版本号    ：  Ver.
import requests
hd = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        }
form={'tableName': 'ZB_XZXK','enterpriseCode':'086135c40d12e66421f53d00df5df6a2','page':'1','row':'10'}
url='http://credit.bjchp.gov.cn/api/webDoublePublicityController/webFindDetailMain.form'
r=requests.get(url,headers=hd,params=form)
print(r.text)