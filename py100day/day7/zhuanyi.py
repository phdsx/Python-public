'''
@Author: your name
@Date: 2019-11-28 11:04:45
@LastEditTime: 2019-11-28 11:13:05
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\day7\zhuanyi.py
'''
s1='\'hello\''
s2='\n\\hello\\\n'
print(s1,s2)
s3 = '\141\142\143\x61\x62\x63'
s4 = '\u9a86\u660a'
print(s3,s4)
s5 = r'\141\142\143\x61\x62\x63'
s6 = r'\u9a86\u660a'
print(s5,s6)