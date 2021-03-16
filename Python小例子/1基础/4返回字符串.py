# -*- encoding : UTF-8 -*-
# Author   ：  phdsx
# 创建时间  ：  2020/5/15 11:02
# 编译器    ：  PyCharm
# 文件名    ：  返回字符串.py
# 所属工程  ：  Python-learning
# 版本号    ：  Ver.
id=1
name='小明'

class Student():
    def __init__(self,id ,name):
        self.id=str(id)
        self.name=name
    def output(self):
        return "id:"+self.id+'\t'+'name:'+name

a=Student(id,name)
b=a.output()
print(b,'\n',ascii(b))