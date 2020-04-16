import re
a=['期刊编号： JKFUN-015','图片数量： 88 张','分 辨 率： 1333X2000','模特姓名：萝莉']
c=[]
for i in a:
    b=re.findall(r'图片数量： (.+) 张',i)
    if b!=[]:
        c.append(b)
print(c)
