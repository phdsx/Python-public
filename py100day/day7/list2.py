'''
@Author: your name
@Date: 2019-11-28 13:45:43
@LastEditTime: 2019-11-28 13:51:48
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\day7\list2.py
'''
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
list3=sorted(list1,reverse=True)
list4=sorted(list1,key=len,reverse=True)
list1.sort(reverse=True)
print(list1,'\n',list2,"\n",list3,'\n',list4,"\n")